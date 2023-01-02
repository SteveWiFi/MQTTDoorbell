from machine import Pin
import dht
import time
from umqttsimple import MQTTClient

doorbell = Pin(2, Pin.IN, Pin.PULL_UP)
ringer = Pin(5, Pin.OUT)

def connect_and_subscribe():
  global client_id, mqtt_server, mqtt_port, mqtt_user, mqtt_pass
  client = MQTTClient(client_id, mqtt_server, mqtt_port, mqtt_user, mqtt_pass)
  client.connect()
  print('Connected to %s MQTT broker' % (mqtt_server))
  return client

def restart_and_reconnect():
  print('Failed to connect to MQTT broker. Reconnecting...')
  time.sleep(10)
  machine.reset()
  
def check_doorbell_rung(client):
  button_state=doorbell.value()
  if button_state == False:
    ringer.value(1)
    time.sleep(0.1)
    ringer.value(0)
    time.sleep(2)
    client.publish(b'door/bell/button/pressed', b'pressed')
    
try:
  client = connect_and_subscribe()
except OSError as e:
  restart_and_reconnect()

while True:
  try:
    check_doorbell_rung(client)
  except OSError as e:
    restart_and_reconnect()