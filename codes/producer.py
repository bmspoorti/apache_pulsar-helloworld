import pulsar

client = pulsar.Client('pulsar://localhost:6650')
print("client created")

producer = client.create_producer('my-topic')
print("topic created")

producer.send(('Hello World!').encode('utf-8'))

  
print('Message sent successfully')

client.close()
