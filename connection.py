import variable, game, music
import random
import network
import ujson
from time import sleep
from umqtt.simple import MQTTClient

NumberToGuess = random.randint(1,100)
print(NumberToGuess)

station = network.WLAN(network.STA_IF)
station.active(True)
station.connect(variable.WIFI_SSID, variable.WIFI_PSSWD)
while not station.isconnected():
    sleep(1)
    print("test")
music.play('Start')

def publish(topic, message):
    jsMsg = ujson.dumps(message)
    client.publish(topic=topic, msg=jsMsg)

def sub_callback(topic, msg):
    print((topic, msg))
    print(msg)
    if NumberToGuess==int(msg):
        music.play('Win')
        return 0
    else:
        if msg=='' or msg==None :
            print('error null')
        else:
            game.game(int(msg),NumberToGuess)

global client
client = MQTTClient(client_id = 'ESP-32' , server = '37.187.38.244', port = 1883, user = 'cnam', password = 'cnam2022')
client.connect()

client.set_callback(sub_callback)
client.subscribe(variable.TOPIC,qos = 1)

while True:
    client.check_msg()
    



    



