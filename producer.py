import pika

credentials = pika.PlainCredentials("guest", "guest")
connectionParameters = pika.ConnectionParameters(host="localhost", credentials=credentials)
connection = pika.BlockingConnection(connectionParameters)

channel = connection.channel()

channel.exchange_declare(
  exchange="hello-exchange",
  exchange_type="direct",
  passive=False,
  durable=True,
  auto_delete=False
)

message_to_send="Hello world"

channel.basic_publish(
  exchange="hello-exchange",
  routing_key="notsosecretkey",
  body=message_to_send
)