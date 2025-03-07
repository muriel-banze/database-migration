import json
import os
import sys

from kafka import KafkaProducer
sys.path.append(os.path.abspath(
    os.path.join(os.path.dirname(__file__), "../../")))
from config.config import BOOTSTRAP_SERVERS, KAFKA_TOPIC_ORACLE_TO_POSTGRES, ORACLE_USER, ORACLE_PASSWORD, ORACLE_DSN
from src.oracle_migration.load_from_oracle import get_oracle_data

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


if __name__ == "__main__":
    send_to_kafka_from_oracle(ORACLE_USER, ORACLE_PASSWORD, ORACLE_DSN)
