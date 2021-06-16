## Q2 Overview

Build a unified API over Kafka and Google Pub Sub. 

### Table of Contents

* [Q2 Overview](#q2-overview)
  * [Goal](#goal)
  * [Installation](#installation)
  * [Directory Structure](#directory-structure)
  * [Publisher Service Usage &amp; Config](#publisher-service-usage--config)
     * [Kafka](#kafka)
     * [GCP](#gcp)
  * [Consumer Service Usage &amp; Config](#consumer-service-usage--config)
     * [Kafka](#kafka-1)
     * [GCP](#gcp-1)


### Goal
Build a unified API over Kafka and Google Pub Sub.

### Installation
To install required dependencies, follow these steps:
Linux and macOS:
```
$ pip install -r requirements.txt
```

### Directory Structure

 * [service](./service) : Contains two directors : Producer & Consumer
   * [producers](./service/producers) : Contains Kafka and GCP Producer Interface Class
     * [gcp_service](./service/producers/gcp_service.py) : GCPService class capable of Publishing to a Google Pub Sub instance
     * [kafka_service](./service/producers/kafka_service.py) : KafkaService class capable of Publishing to a Kafka instance
   * [consumers](./service/consumers) : Contains Kafka and GCP Consumer / Subscriber Interface Class
     * [gcp_service](./service/consumers/gcp_service.py) : GCPService class capable of Consuming from a Google Pub Sub instance
     * [kafka_service](./service/consumers/kafka_service.py) : KafkaService class capable of Consuming from a Kafka instance

### Publisher Service Usage & Config

#### Kafka 
* Kafka Config :
```
kafka_config = {
        "bootstrap_server": BOOTSTRAP_SERVER,
        "value_serializer": SERIALIZER_FUNCTION
}
```

* Kafka Usage :
```
from service.producers.kafka_service import KafkaService as KProducer
.....
.....
client = KProducer(config=kafka_config)
client.produce(DATA_TO_PUBLISH, KAFKA_TOPIC)
```

#### GCP 

* GCP Config :
```
gcp_config = {
    "project_id": GCP_PROJECT_ID,
    "value_serializer": SERIALIZER_FUNCTION
}
```
* GCP Usage :
```
from service.producers.gcp_service import GCPService as GProducer
.....
.....
client = GProducer(config=gcp_config)
client.produce(DATA_TO_PUBLISH, GCP_TOPIC)
```

### Consumer Service Usage & Config

#### Kafka 
* Kafka Config :
```
kafka_config = {
    "name": KAFKA_TOPIC,
    "bootstrap_server": BOOTSTRAP_SERVER,
    "value_deserializer": SERIALIZER_FUNCTION,
    "auto_offset_reset": "earliest",
    "enable_auto_commit": True,
    "group_id": "counters",
}
```

* Kafka Usage :
```
from service.consumers.kafka_service import KafkaService as KConsumer
.....
.....
client = KConsumer(config=kafka_config)
client.consume()
```

#### GCP 
* GCP Config :
```
gcp_config = {
    "project_id": GCP_PROJECT_ID,
    "subscription_id": GCP_SUBSCRIPTION_ID
}
```

* GCP Usage : 
```
from service.consumers.gcp_service import GCPService as GConsumer
.....
.....
client = GConsumer(config=gcp_config)
client.consume()
```

---------

## Q3 Overview

### Goal
Build a robust system to classify fashion images. The system will have a single client consuming a single
machine learning service. The system can process requests in a non-blocking way and (theoretically) put the
results somewhere else (like a database), currently mocked by
printing to the console.

### Pre-requisites
> Launch Apache Kafka Service

> Create 2 topics on said service : T1 & T2


### Configuration
Update the following variables before launching the services :
* In `q3_dummy_producer.py`:
    * `IMG_PATH` = Path to image file
    * `PUBLISHER_SERVER` = Server where `T1` Kafka Instance is running
    * `PUBLISHER_TOPIC` = `T1`
    

* In `q3_dummy_model_instance.py`:
    * `PUBLISHER_SERVER` = Server where `T2` Kafka Instance is running
    * `PUBLISHER_TOPIC` = `T2`
    * `SUBSCRIBER_SERVER` = Server where `T1` Kafka Instance is running
    * `SUBSCRIBER_TOPIC` = `T1`
    
* In `q3_dummy_consumer.py`:
    * `SUBSCRIBER_SERVER` = Server where `T2` Kafka Instance is running
    * `SUBSCRIBER_TOPIC` = `T2`


### Usage

1. `python q3_dummy_model_instance.py` : Launches Lenet Model Service. This service consumes incoming messages on Topic `T1` and publishes results to Topic `T2`
2. `python q3_dummy_producer.py` : Launches Producer that reads from a file and publishes message to `T1`
3. `python q3_dummy_consumer.py` : Consumes messages from Topic `T2` and prints them to the console


