
import json
from random import randint

# libraries for MQTT and FFmpeg
import paho.mqtt.client as mqtt

import time

# MQTT server environment variables
MQTT_HOST = '192.168.56.101'  # IPADDRESS
MQTT_PORT = 1883  # Set the Port for MQTT
MQTT_KEEPALIVE_INTERVAL = 60

def start_mqtt():
    client = mqtt.Client()
    client.connect(MQTT_HOST, MQTT_PORT, MQTT_KEEPALIVE_INTERVAL)

    while 1:
        pred = randint(1,10)

        # Send clases
        MQTT_MSG_SPEED = json.dumps({"speed": pred})
        client.publish(topic="speedometer", payload=MQTT_MSG_SPEED, qos=0, retain=False)
        print(MQTT_MSG_SPEED)
        time.sleep(3)

def main():
    start_mqtt()


if __name__ == "__main__":
    main()