import pulsar

client = pulsar.Client('pulsar://localhost:6650')
print("client created")

consumer = client.subscribe('my-topic', subscription_name='my-subscription')
print("subscription added")

msg = consumer.receive()

print("Received message: '%s'" % msg.data().decode('utf-8'))

consumer.acknowledge(msg)
client.close()
