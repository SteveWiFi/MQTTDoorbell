import time
import ubinascii
import machine
import micropython
import network
import esp
esp.osdebug(None)
import gc
from umqttsimple import MQTTClient
gc.collect()

ssid = 'WIFI_SSID'
password = 'WIFI_PASSWORD'
mqtt_server = '0.0.0.0'
mqtt_port = 1883
mqtt_user = "MQTT_USERNAME"
mqtt_pass = "MQTT_PASSWORD"
client_id = ubinascii.hexlify(machine.unique_id())

station = network.WLAN(network.STA_IF)

station.active(True)
station.connect(ssid, password)

while station.isconnected() == False:
  pass

print('Connection successful')
print(station.ifconfig())
