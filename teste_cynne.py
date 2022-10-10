import paho.mqtt.client as mqtt
import time
from config import username, password, client_id, server, port

def recebi_mensagem(client, userdata, msg):

    print(msg.payload)



cliente = mqtt.Client(client_id)

cliente.username_pw_set(username, password)

cliente.on_message = recebi_mensagem

cliente.connect(server, port)

cliente.loop_start()  # Thread criada para ficar monitorando as mensagens

cliente.subscribe(f'v1/{username}/things/{client_id}/cmd/2')



for i in range(10, 38):

    cliente.publish(f'v1/{username}/things/{client_id}/data/0', str(i-3))

    cliente.publish(f'v1/{username}/things/{client_id}/data/1', str(i))

    time.sleep(10)