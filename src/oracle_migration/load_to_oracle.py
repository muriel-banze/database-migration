import json

import cx_Oracle

from config import (ORACLE_USER,
                    ORACLE_PASSWORD,
                    ORACLE_DSN)


def insert_into_oracle(record):
    connection = cx_Oracle.connect(
        user=ORACLE_USER, password=ORACLE_PASSWORD, dsn=ORACLE_DSN)
    cursor = connection.cursor()

    table_data = json.loads(record)
    # print("Message sent:", table_data)

    for table_name_, table_value_ in table_data.items():
        table_name = table_name_
        table_value = table_value_

        columns = ", ".join(f"{col}" for col in (table_value[0].keys()))
        values_placeholder = ", ".join(":" + str(i + 1) for i in range(len(table_value[0].keys())))
        print("Inserting data into table: ", table_name, "\nColumn details: ", columns)

        insert_query = (f"INSERT INTO {table_name}_V1 "
                        f"({columns}) VALUES ({values_placeholder})")
        print("Insert Query: ", insert_query)

        values_list = [
            tuple(str(v) if isinstance(v, (dict, list)) else v for v in val.values())
            for val in table_value
        ]
        cursor.executemany(insert_query, values_list)
        connection.commit()

    # Close connections
    cursor.close()
    connection.close()
