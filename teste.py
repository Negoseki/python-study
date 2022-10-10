import paho.mqtt.client as mqtt
import time

cliente = mqtt.Client('clientId-Xmyj3Vv0Wi')
#cliente.username_pw_set('')
cliente.connect('broker.mqttdashboard.com', 1883)
cliente.publish('PUCPR/AD/DoPython', 'Olá do Python!!!')
time.sleep(2)