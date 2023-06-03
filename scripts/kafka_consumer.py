import json
from kafka import KafkaConsumer
from database import insert_microclimate_data
from dotenv import load_dotenv
import os

load_dotenv()

def create_kafka_consumer(bootstrap_servers, group_id):
    consumer = KafkaConsumer(
        bootstrap_servers=bootstrap_servers,
        value_deserializer=lambda m: json.loads(m.decode("utf-8")),
        group_id=group_id,
        auto_offset_reset="earliest",
        enable_auto_commit=True,
    )
    return consumer

def process_microclimate_data(consumer, topic):
    consumer.subscribe([topic])

    for message in consumer:
        data = message.value
        print(f"Received data: {data}")
        insert_microclimate_data(data)

if __name__ == "__main__":
    topic = "microclimate_data"
    bootstrap_servers = ["localhost:9092"]
    group_id = "microclimate_data_group"
    
    consumer = create_kafka_consumer(bootstrap_servers, group_id)
    process_microclimate_data(consumer, topic)

