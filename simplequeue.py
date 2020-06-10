import socket
import time
import os
import pika
import logging

logging.basicConfig(level=logging.DEBUG)

# receiving message callback
def receiveMessage(channel, method, properties, body):
    print('[x] Received %r ' % body)


print('**** Running simplequeue.py ****')


isreachable = False
pingCounter = 0
print('**** first we see if we can reach the server')
while isreachable is False and pingCounter < 10:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        # s.connect(('0.0.0.0',5672))
        s.connect(('localhost', os.environ['RABBITMQ_PORT']))
        isreachable = True
        print('[x] found the server')
    except socket.error as e:
        time.sleep(2)
        pingCounter += 1
    s.close()

if isreachable is False:
    print('[!] Could not get a socketfor <host>:port')
else:
    print('[x] socket to host worked')



amqp_url = os.environ['AMQP_URL']
print(amqp_url)

parameters = pika.URLParameters(amqp_url)
print(parameters)
# # ### choose which parameter set
parameters.socket_timeout = 5
   
try:
    print('[x] about to build a blocking connection')
    connection = pika.BlockingConnection(parameters)
    print('[x] built a connection')
    channel = connection.channel()
    channel.queue_declare(queue='first_queue')

    channel.basic_publish(exchange='', routing_key='first_queue', body='Hi Queue')
    print('[x] send a first message to the queue')


    time.sleep(5)

    channel.basic_consume(queue='first_queue', auto_ack=True, on_message_callback=receiveMessage)

    print('[x] Waiting for messages')

    channel.start_consuming()
    connection.close()
except:
    print("[!] We could not get a connection")
    pass
