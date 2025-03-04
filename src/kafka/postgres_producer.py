import json

from kafka import KafkaProducer

from config.config import BOOTSTRAP_SERVERS, KAFKA_TOPIC_POSTGRES_TO_ORACLE
from src.postgres_migration.load_from_postgres import get_postgres_data

# Kafka Producer Configuration
producer = KafkaProducer(
    bootstrap_servers=BOOTSTRAP_SERVERS,
    value_serializer=lambda v: json.dumps(v).encode("utf-8")
)


def send_to_kafka_from_postgres():
    table_data = get_postgres_data()
    producer.send(topic=KAFKA_TOPIC_POSTGRES_TO_ORACLE, value=table_data)
    producer.flush()
    print("Data pushed to Kafka successfully from Postgres db!")


if __name__ == "__main__":
    send_to_kafka_from_postgres()
