# https://www.rabbitmq.com/tutorials/tutorial-one-python.html
# start RabbitMQ with docker:
# docker run -it --rm --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:3.9-management
# python package for RabbitMQ
import pika
from datetime import datetime
# connect to RabbitMQ-Broker on localhost
connection=pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel=connection.channel()

channel.queue_declare(queue='tq')


# publish the message (body) to the queue (routing_key)
t0 = str(datetime.now()).encode('utf-8')
for x in range(0,10000):
    channel.basic_publish(exchange ='',
                        routing_key= 'tq',
                        body = '')
    
channel.basic_publish(exchange = '',
                        routing_key =  'tq',
                        body = t0)


# close the connection
connection.close()


# tomestamp = np.frombuffer(ts,dtype)