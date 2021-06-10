from kafka_producer import MyKafkaProducer
from gcp_publisher import MyPubSubProducer

BOOTSTRAP_SERVER = 'localhost:9092'
KAFKA_TOPIC = 'numtest'
GCP_PROJECT_ID = "silver-spark-316405"
GCP_TOPIC = "sending_topic_1"

choice = "GCP"

if choice == "KAFKA":
    new_kafka_producer = MyKafkaProducer(BOOTSTRAP_SERVER)
    new_kafka_producer.send_data(24123, KAFKA_TOPIC)

if choice == "GCP":
    new_gcp_producer = MyPubSubProducer(GCP_PROJECT_ID)
    new_gcp_producer.send_data(24123, GCP_TOPIC)


