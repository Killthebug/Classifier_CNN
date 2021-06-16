from service.consumers.kafka_service import KafkaService as KConsumer
import json

SUBSCRIBER_SERVER = "localhost:9092"
SUBSCRIBER_TOPIC = "test_response"


def data_deserializer(data):
    return json.loads(data.decode('utf-8'))


if __name__=="__main__":
    kafka_config = {
        "name": SUBSCRIBER_TOPIC,
        "bootstrap_server": SUBSCRIBER_SERVER,
        "value_deserializer": data_deserializer,
        "auto_offset_reset": "earliest",
        "enable_auto_commit": True,
        "group_id": "counters",
    }

    client = KConsumer(config=kafka_config)
    while 1:
        response = client.consume()
        print(f'Class Label {response.value}')