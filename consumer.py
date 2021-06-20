import pika

credentials = pika.PlainCredentials("guest", "guest")
connectionParameters = pika.ConnectionParameters(host="localhost", credentials=credentials)
connection = pika.BlockingConnection(connectionParameters)
channel = connection.channel()

channel.queue_declare(queue='hello-world-queue')

channel.queue_bind(
  queue='hello-world-queue',
  exchange='hello-exchange',
  routing_key='notsosecretkey'
  )


def callback(channel, method, header, body):
  channel.basic_ack(delivery_tag=method.delivery_tag)
  print('------MessageBody------')
  print(body)
  print('------MessageBody-----')


channel.basic_consume(
  queue='hello-world-queue',
  on_message_callback=callback
)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()