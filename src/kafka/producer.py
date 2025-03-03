import json

from config import BOOTSTRAP_SERVERS, KAFKA_TOPIC_ORACLE_TO_POSTGRES, KAFKA_TOPIC_POSTGRES_TO_ORACLE
from kafka import KafkaProducer
from src.oracle_migration.load_from_oracle import get_oracle_data
from src.postgres_migration.load_from_postgres import get_postgres_data

# Kafka Producer Configuration
producer = KafkaProducer(
    bootstrap_servers=BOOTSTRAP_SERVERS,
    value_serializer=lambda v: json.dumps(v).encode("utf-8")
)


def send_to_kafka_from_oracle(oracle_user, oracle_password, oracle_dsn):
    """Send records to Kafka topic"""
    table_data = get_oracle_data(oracle_user, oracle_password, oracle_dsn)
    producer.send(topic=KAFKA_TOPIC_ORACLE_TO_POSTGRES, value=table_data)
    producer.flush()
    print("Data pushed to Kafka successfully from Oracle db!")


def send_to_kafka_from_postgres():
    table_data = get_postgres_data()
    producer.send(topic=KAFKA_TOPIC_POSTGRES_TO_ORACLE, value=table_data)
    producer.flush()
    print("Data pushed to Kafka successfully from Postgres db!")


