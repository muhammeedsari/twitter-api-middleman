from core.confluentKafka.kafka import Kafka
import simplejson as json

class ConsumerController:
    def consume_tweets(self):
        kafka = Kafka()
        customer = kafka.create_consumer(
            topic="tweet",
            group_id="test")


        while True:
            try:
                msg = customer.poll()

                if msg is None:
                    continue
                if msg.error():
                    print("Consumer customer error: {}".format(msg.error()))
                    continue
                
                json_data = json.loads(msg.value().decode('utf-8'))

                print(json_data)
            except Exception as err:
                print(f"something went wrong {err}")