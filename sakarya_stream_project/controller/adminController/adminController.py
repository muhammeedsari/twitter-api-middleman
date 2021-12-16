from core.confluentKafka.kafka import Kafka
class AdminController:

    def create_topic(self, topic="tweet", num_partitions=2):
        try:
            kafka = Kafka()
            kafka.create_topics(topic=topic, num_partitions=num_partitions)
        except Exception as err:
            print(f"something went wrong {err}")