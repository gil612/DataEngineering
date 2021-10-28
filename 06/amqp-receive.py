# https://www.rabbitmq.com/tutorials/tutorial-one-python.html
# start RabbitMQ with docker:
# docker run -it --rm --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:3.9-management
# python package for RabbitMQ
import pika, sys, os
from datetime import datetime


def callback(ch, method, properties, body):
    global msg_counter
    if msg_counter < 10000: 
        msg_counter +=1
    if len(body) > 1 and msg_counter == 10000:
        t = datetime.now()
        t_sub = datetime.fromisoformat(body.decode())
        print(t_sub,t)
        print('Messages per Second: ', 10000/(t-t_sub).total_seconds())
            

if __name__ == '__main__':
    msg_counter = 0
    try:

        connection = pika.BlockingConnection(
            pika.ConnectionParameters(host='localhost'))
            
        channel=connection.channel()
        channel.queue_declare(queue='tq')
        channel.basic_qos(prefetch_count=1)
        channel.basic_consume(queue='tq', on_message_callback=callback, auto_ack=True)
        print(' [*] Waiting for messages. To exit press CTRL+C')
        channel.start_consuming()

    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)

# Messages per Second:  3297.6371803052048