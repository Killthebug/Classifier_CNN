from service.producers.kafka_service import KafkaService as KProducer
from service.consumers.kafka_service import KafkaService as KConsumer

from service.producers.gcp_service import GCPService as GProducer
from service.consumers.gcp_service import GCPService as GConsumer

import sys
import json

"""
Define config elements of kafka instance to interact with
"""
BOOTSTRAP_SERVER = "localhost:9092"
KAFKA_TOPIC = "numtest"

"""
Define config elements of Google Pub Sub instance to interact with
"""
GCP_PROJECT_ID = "silver-spark-316405"
GCP_TOPIC = "sending_topic_1"
GCP_SUBSCRIPTION_ID = "my-sub"

"""
Dummy Data used for experiment
"""
DATA_TO_PUBLISH = "24123"

choice = sys.argv[1]  # Determine which message broker to use : Kafka / Google Pub Sub
run_type = sys.argv[2]  # Determine behaviour of message broker : Producer / Consumer


def kafka_serializer(data):
    return json.dumps(data).encode("utf-8")


def kafka_deserializer(data):
    return json.loads(data.decode("utf8"))


def gcp_serializer(data):
    return str(data).encode("utf-8")


if choice == "KAFKA" and run_type == "PRODUCER":
    kafka_config = {
        "bootstrap_server": BOOTSTRAP_SERVER,
        "value_serializer": kafka_serializer
    }
    client = KProducer(config=kafka_config)
    client.produce(DATA_TO_PUBLISH, KAFKA_TOPIC)

if choice == "GCP" and run_type == "PRODUCER":
    gcp_config = {
        "project_id": GCP_PROJECT_ID,
        "value_serializer": gcp_serializer
    }
    client = GProducer(config=gcp_config)
    client.produce(DATA_TO_PUBLISH, GCP_TOPIC)

if choice == "KAFKA" and run_type == "CONSUMER":
    kafka_config = {
        "name": KAFKA_TOPIC,
        "bootstrap_server": BOOTSTRAP_SERVER,
        "value_deserializer": kafka_deserializer,
        "auto_offset_reset": "earliest",
        "enable_auto_commit": True,
        "group_id": "counters",
    }
    client = KConsumer(config=kafka_config)
    while 1:
        client.consume()

if choice == "GCP" and run_type == "CONSUMER":
    gcp_config = {
        "project_id": GCP_PROJECT_ID,
        "subscription_id": GCP_SUBSCRIPTION_ID
    }
    client = GConsumer(config=gcp_config)
    while 1:
        client.consume()
