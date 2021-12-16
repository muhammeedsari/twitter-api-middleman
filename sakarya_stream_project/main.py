from controller.produceController.streamListener import StreamListener

consumer_key="VgI4nJ630p2gQWA0GCybdN3tn"
consumer_secret="6bQbRF69jA4EBxINOw6bWoZZnafYSpcZineRO08tmwO4bJQA5l"
access_token_key="4857953291-WBOF4xnboxu1AyHW90P85y1JyhHOAghpKm0P7g3"
access_token_secret="tfBPKie1FQVjfMr1qRsifLADdvoiK1SOOlepXiRuzBmMq"



stream = StreamListener(
  consumer_key, consumer_secret,
  access_token_key, access_token_secret
)

stream.filter(track=["ekonomi"],languages=["tr"])