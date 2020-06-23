import pika

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='a1a1585d3b1b248d0875b61e1ae66cce-2049874436.us-east-1.elb.amazonaws.com'))
channel = connection.channel()

channel.queue_declare(queue='naresh.queue')


def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)


channel.basic_consume(
    queue='naresh.queue', on_message_callback=callback, auto_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
