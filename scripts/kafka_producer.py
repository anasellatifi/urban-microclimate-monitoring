from kafka import KafkaProducer
import json

def create_kafka_producer(bootstrap_servers):
    producer = KafkaProducer(
        bootstrap_servers=bootstrap_servers,
        value_serializer=lambda v: json.dumps(v).encode('utf-8')
    )
    return producer

def send_microclimate_data(producer, topic, data):
    producer.send(topic, data)
    producer.flush()

