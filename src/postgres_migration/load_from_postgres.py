import re

import psycopg2

from config import (POSTGRES_DB,
                    POSTGRES_USER,
                    POSTGRES_PASSWORD,
                    POSTGRES_HOST)
from src.oracle_migration.load_from_oracle import serialize_datetime
from src.sql_queries.select_queries import postgres_queries


def get_postgres_data():
    # Connect to PostgreSQL
    pg_conn = psycopg2.connect(
        dbname=POSTGRES_DB,
        user=POSTGRES_USER,
        password=POSTGRES_PASSWORD,
        host=POSTGRES_HOST,
        port="5432"
    )

    cursor = pg_conn.cursor()
    results = {}
    for query in postgres_queries:

        cursor.execute(query)
        records = cursor.fetchall()
        if len(records):
            columns = [col[0] for col in cursor.description]
            table_data = [dict(zip(columns, map(serialize_datetime, row)))
                          for row in records]
            results[re.split('\.', query)[-1]] = table_data
    # Close connections
    cursor.close()
    pg_conn.close()
    return results
