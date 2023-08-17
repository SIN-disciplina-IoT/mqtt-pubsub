# python3.6

import random

import paho.mqtt.client as mqtt

broker = '127.0.0.1'
port = 1883
topic = "teste"
# Generate a Client ID with the subscribe prefix.
client_id = f'subscribe-{random.randint(0, 100)}'
# username = 'emqx'
# password = 'public'


def on_connect(client, userdata, flags, rc):
    client.subscribe(topic)
    client.on_message = on_message
    return client

def on_message(client, userdata, msg):
        print(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")

def run():
    client = mqtt.Client("sub1")
    client.on_connect = on_connect
    client.on_message = on_message

    client.connect(broker, port)

    client.loop_forever()


if __name__ == '__main__':
    run()
