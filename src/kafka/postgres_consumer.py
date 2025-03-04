import json
import os
import sys

from kafka import KafkaConsumer
sys.path.append(os.path.abspath(
    os.path.join(os.path.dirname(__file__), "../../")))

from config.config import KAFKA_TOPIC_POSTGRES_TO_ORACLE, BOOTSTRAP_SERVERS, KAFKA_GROUP
from src.oracle_migration.load_to_oracle import insert_into_oracle


def consume_messages_pg_to_oracle():
    """Consume messages from Kafka and insert into PostgreSQL"""
    consumer = KafkaConsumer(
        KAFKA_TOPIC_POSTGRES_TO_ORACLE,
        bootstrap_servers=BOOTSTRAP_SERVERS,
        group_id=KAFKA_GROUP,
        value_deserializer=lambda v: json.loads(v.decode('utf-8')),
        auto_offset_reset='latest'
    )

    print("Waiting for messages...")

    for message in consumer:
        print(f"Consumed: {len(message.value)}")
        insert_into_oracle(json.dumps(message.value))


if __name__ == "__main__":
    consume_messages_pg_to_oracle()
