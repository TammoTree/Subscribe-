import network  
from umqtt.simple import MQTTClient
import time
from machine import Pin, SoftI2C



MQTT_SERVER = "10.50.217.98"
CLIENT_ID = "MQTT_BAUM"
MQTT_TOPIC_TASTER = "BZTG/Ehnern/Taster"



wlan = network.WLAN(network.STA_IF)     #Objekt wlan als station interface

wlan.active(True)                       #System einschalten

if not wlan.isconnected():              #Wenn Wlan nicht verbunden ist -> 

    wlan.connect("BZTG-IoT", "WerderBremen24")      #Wlan verbinden

    while not wlan.isconnected():                   #Solange es nicht verbunden ist -> mache nichts

        pass

    print("Netzwerkkonfiguration: ", wlan.ifconfig())   #Netzwerkinfos ausgeben (IP Adresse, Subnetzmaske, Gateway, DNS-Server)

#---------------------------------------------------------------------------------------------------------------------------------------------------------

def sub_LED(topic, msg):
    print(msg)

mqtt_Baum = MQTTClient(CLIENT_ID, MQTT_SERVER)
mqtt_Baum.set_callback(sub_LED)
mqtt_Baum.connect()
mqtt_Baum.subscribe(MQTT_TOPIC_TASTER)

print("MQTT verbunden!")

while True:
    mqtt_Baum.check_msg()
