Instalar 
[Anaconda](https://www.anaconda.com/products/individual#windows)
 y 
[Pycharm](https://www.jetbrains.com/es-es/pycharm/download/#section=windows)

Instalacion de opencv:

```
python3 -m pip install opencv-python
```

Ejemplo en kivy:

```python
from kivy.app import App
from kivy.uix.button import Button

class TestApp(App):
    def build(self):
        return Button(text='Hello World')

TestApp().run()
```

Instalar socat para probar con el serial

```
sudo apt-get install socat
socat PTY,link=/dev/ttyUSB,raw,echo=0-
```

Ejemplo pyserial
```python
import serial
ser=serial.Serial("/dev/ttyUSB", 115200, timeout=None)
while 1:
    valor=ser.read(1)
    if valor!=b"\n":
        print(valor)
```

Integrando a MQTT

```python
import json
from random import randint

# libraries for MQTT and FFmpeg
import paho.mqtt.client as mqtt

import serial
ser=serial.Serial("/dev/ttyUSB", 115200, timeout=None)

# MQTT server environment variables
MQTT_HOST = '192.168.56.101'  # IPADDRESS
MQTT_PORT = 1883  # Set the Port for MQTT
MQTT_KEEPALIVE_INTERVAL = 60

def start_mqtt():
    client = mqtt.Client()
    client.connect(MQTT_HOST, MQTT_PORT, MQTT_KEEPALIVE_INTERVAL)

    while 1:
        valor=ser.read(1)
        if valor!=b"\n":
            print(valor)
            # Send clases
            MQTT_MSG_SPEED = valor
            client.publish(topic="prueba", payload=MQTT_MSG_SPEED, qos=0, retain=False)
    

def main():
    start_mqtt()


if __name__ == "__main__":
    main()
```

