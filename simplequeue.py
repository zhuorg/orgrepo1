import socket
import time
import os

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
        # s.connect(('0.0.0.0',15672))
        s.connect(('0.0.0.0', 5672))
        isreachable = True
        print('[x] found the server')
    except socket.error as e:
        time.sleep(2)
        pingCounter += 1
    s.close()

if isreachable is False:
    print('[!] Could not get a socketfor <host>:5672')
else:
    print('[x] socket to host worked')


# rabbitmq_port = os.environ['RABBITMQ_PORT']
amqp_url = os.environ['AMQP_URL']
# print(rabbitmq_port)
print(amqp_url)

urlConnectionParameters = pika.URLParameters(amqp_url)
connection = pika.BlockingConnection(urlConnectionParameters)
