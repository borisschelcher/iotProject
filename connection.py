import variable, game
import network
import ujson
from time import sleep
from umqtt.simple import MQTTClient

station = network.WLAN(network.STA_IF)
station.active(True)
station.connect(variable.WIFI_SSID, variable.WIFI_PSSWD)
while not station.isconnected():
    sleep(1)


def publish(topic, message):
    jsMsg = ujson.dumps(message)
    client.publish(topic=topic, msg=jsMsg)

def sub_callback(topic, msg):
    print((topic, msg))
    game.answer=int(msg)

global client
client = MQTTClient(client_id = variable.CLIENT_ID , server = variable.MQTT_BROKER_IP, port = variable.PORT, user = variable.MQTT_USER, password= variable.MQTT_PASSWORD)
client.connect()

client.set_callback(sub_callback)
client.subscribe(variable.TOPIC,qos = 1)

while True:
    client.check_msg();



    



