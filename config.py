import os

import cx_Oracle

# # Oracle DB Connection
# ORACLE_HOST = "174.129.134.35"
# ORACLE_PORT = 1521
# ORACLE_USER = "VUCEM_APP_P01"
# ORACLE_PASSWORD = "Mfk22nvW6na71DgBXi5R"
# ORACLE_SID = "xe"
# ORACLE_DSN = cx_Oracle.makedsn(ORACLE_HOST, ORACLE_PORT, ORACLE_SID)
# os.environ["DYLD_LIBRARY_PATH"] = "/opt/oracle/instantclient_19_8"
# os.environ["ORACLE_HOME"] = "/opt/oracle/instantclient_19_8"
# cx_Oracle.init_oracle_client(lib_dir="/opt/oracle/instantclient_19_8")
#
# # PostgreSQL Connection
# POSTGRES_HOST = "localhost"
# POSTGRES_DB = "test"
# POSTGRES_USER = "postgres"
# POSTGRES_PASSWORD = "password"
#
# # Kafka Configuration
# BOOTSTRAP_SERVERS = "localhost:9092"
# KAFKA_GROUP = "postgres_load2"
# KAFKA_TOPIC = "migrate_oracle_to_postgres2"

# Oracle DB Connection
ORACLE_HOST = "localhost"
ORACLE_PORT = 1521
ORACLE_USER = "system"
ORACLE_PASSWORD = "purple1"
ORACLE_SID = "XE"
ORACLE_DSN = cx_Oracle.makedsn(ORACLE_HOST, ORACLE_PORT, ORACLE_SID)
os.environ["DYLD_LIBRARY_PATH"] = "/opt/oracle/instantclient_19_8"
os.environ["ORACLE_HOME"] = "/opt/oracle/instantclient_19_8"
cx_Oracle.init_oracle_client(lib_dir="/opt/oracle/instantclient_19_8")

# PostgreSQL Connection
POSTGRES_HOST = "localhost"
POSTGRES_DB = "customer_orders"
POSTGRES_USER = "postgres"
POSTGRES_PASSWORD = "password"

# Kafka Configuration
BOOTSTRAP_SERVERS = "localhost:9092"
KAFKA_GROUP = "co_group_new"
KAFKA_TOPIC_ORACLE_TO_POSTGRES = "co_oracle_to_postgres_new"
KAFKA_TOPIC_POSTGRES_TO_ORACLE = "co_postgres_to_oracle_new"
