import json
import os
import sys

from kafka import KafkaConsumer

sys.path.append(os.path.abspath(
    os.path.join(os.path.dirname(__file__), "../../")))

from config.config import KAFKA_TOPIC_ORACLE_TO_POSTGRES, BOOTSTRAP_SERVERS, KAFKA_GROUP

from src.postgres_migration.load_to_postgres import insert_into_postgres


def consume_messages_oracle_to_pg():
    """Consume messages from Kafka and insert into PostgreSQL"""

    consumer = KafkaConsumer(
        KAFKA_TOPIC_ORACLE_TO_POSTGRES,
        bootstrap_servers=BOOTSTRAP_SERVERS,
        group_id=KAFKA_GROUP,
        value_deserializer=lambda v: json.loads(v.decode('utf-8')),
        auto_offset_reset='latest'
    )

    print("Waiting for messages...")

    for message in consumer:
        try:
            print(f"Consumed: {message.value}")
            insert_into_postgres(json.dumps(message.value))
        except Exception as e:
            print(f"Error processing message: {e}")


if __name__ == "__main__":
    consume_messages_oracle_to_pg()
