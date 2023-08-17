import random
import time

import paho.mqtt.client as mqtt


broker = '127.0.0.1'
port = 1883
topic = "teste"
# Generate a Client ID with the publish prefix.
client_id = f'publish-{random.randint(0, 1000)}'
# username = 'emqx'
# password = 'public'

def on_connect(client, userdata, flags, rc):
    client.subscribe(topic)
    return client

def publish(client):
    msg_count = 1
    while True:
        time.sleep(1)
        msg = f"messages: {msg_count}"
        result = client.publish(topic, msg)
        # result: [0, 1]
        status = result[0]
        if status == 0:
            print(f"Send `{msg}` to topic `{topic}`")
        else:
            print(f"Failed to send message to topic {topic}")
        msg_count += 1
        if msg_count > 5:
            break

def run():
    client = mqtt.Client("pub1")
    client.connect(broker, port)
    publish(client)
    # client.loop_forever()


if __name__ == '__main__':
    run()