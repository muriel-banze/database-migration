from datetime import datetime

import cx_Oracle

from src.sql_queries.select_queries import oracle_queries


def serialize_datetime(obj):
    if isinstance(obj, datetime):
        return obj.strftime("%Y-%m-%d %H:%M:%S")
    return obj


def get_oracle_data(oracle_user, oracle_password, oracle_dsn):
    """Fetch data from Oracle"""
    connection = cx_Oracle.connect(
        user=oracle_user, password=oracle_password, dsn=oracle_dsn)
    cursor = connection.cursor()

    results = {}

    for query in oracle_queries:
        cursor.execute(query)
        records = cursor.fetchall()
        print("records", records)
        if len(records):
            columns = [col[0] for col in cursor.description]
            table_data = [dict(zip(columns, map(serialize_datetime, row)))
                          for row in records]
            results[query.split(" ")[-1]] = table_data
    cursor.close()
    connection.close()
    return results
