import time
import paho.mqtt.client as mqtt

def on_message(client, userdata, msg):
    payload = msg.payload.decode()
    print(f"Received message on topic '{msg.topic}': {payload}")

def on_connect(client, userdata, flags, reason_code, properties=None):
    print(f"Connected with result code {reason_code}")

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.on_connect = on_connect
client.on_message = on_message

client.connect("172.20.3.43", 1883, 60)

client.loop_start()

while True:
	time.sleep(5)
	temp = 0.0

	with open("/sys/class/thermal/thermal_zone0/temp", "r") as file:
		temp = float(file.read())/1000.0

	print(temp)
	client.publish("BrokerTemp", temp)

