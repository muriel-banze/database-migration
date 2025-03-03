from config import ORACLE_DSN, ORACLE_USER, ORACLE_PASSWORD
from src.kafka.producer import send_to_kafka_from_oracle, send_to_kafka_from_postgres

if __name__ == "__main__":
    send_to_kafka_from_oracle(ORACLE_USER, ORACLE_PASSWORD, ORACLE_DSN)
    send_to_kafka_from_postgres()
