#!/usr/bin/env python
import pika

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='hello')

# para_1: All we need to know now is how to use a default exchange identified by an empty string.
# para_2: The queue name needs to be specified in the routing_key
channel.basic_publish(exchange='', routing_key='hello', body='Hello World!')

# Make sure the network buffers were flushed and our message was actually delivered to RabbitMQ.
print(" [x] Sent 'Hello World!'")

# We can do it by gently closing the connection.
connection.close()