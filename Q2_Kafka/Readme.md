## Q2 Overview

Unified API over Kafka and Google Pub Sub.

Sample interaction script : main.py

## Q3 Overview
`python q3_dummy_model_instance.py` : Launches Lenet Model Service \
`python q3_dummy_producer.py` : Launches Producer that reads from a file and sends request to the Lenet Model\
`python q3_dummy_consumer.py` : Accepts responses / predictions coming in from the Lenet Service

NOTE : Before launching services it is important to configure Kafka Server Address and Topic Name.

The solution current uses Kafka as a messaging broker but can be shifted to GCP as well.

