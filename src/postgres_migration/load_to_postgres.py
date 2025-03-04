import json

import psycopg2

from config.config import POSTGRES_USER, POSTGRES_DB, POSTGRES_PASSWORD, POSTGRES_HOST


def insert_into_postgres(record):
    """Insert Kafka message into PostgreSQL"""
    pg_conn = psycopg2.connect(
        dbname=POSTGRES_DB,
        user=POSTGRES_USER,
        password=POSTGRES_PASSWORD,
        host=POSTGRES_HOST,
        port="5432"
    )
    cursor = pg_conn.cursor()

    table_data = json.loads(record)
    print("Message sent:", table_data)

    for table_name_, table_value_ in table_data.items():
        table_name = table_name_
        table_value = table_value_

        columns = ", ".join(f"\"{col}\"" for col in (table_value[0].keys()))
        values_placeholder = ", ".join(["%s"] * len(table_value[0].values()))
        print("Inserting data into table: ", table_name, "\nColumn details: ", columns)

        insert_query = (f"INSERT INTO public.\"{table_name.lower()}\" "
                        f"({columns.lower()}) VALUES ({values_placeholder})")
        print("Insert Query: ", insert_query)

        for val in table_value:
            values = tuple(val.values())
            values = tuple(str(v) if isinstance(v, (dict, list))
                           else v for v in values)
            cursor.execute(insert_query, values)

    pg_conn.commit()
    cursor.close()
    pg_conn.close()

