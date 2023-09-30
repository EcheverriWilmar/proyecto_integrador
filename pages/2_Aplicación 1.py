import streamlit as st
import paho.mqtt.client as mqtt
import db

# Diseño personalizado
st.header("Aplicación 1")

client = None
input_message = ""

db.create_database()
#db.add_setting("","","","")

setting = db.get_setting()
#st.write(setting)



with st.expander("Configuración"):
    st.subheader("MQTT")
    broker = st.text_input('Broker', setting[0][1])
    port = st.text_input('Puerto', setting[0][2])
    subscribe = st.text_input('Tópico suscripcion', setting[0][3])
    publish = st.text_input('Tópico publicación', setting[0][4])


if broker:
    db.update_broker(1,broker)
if port:
    db.update_port(1,port)
if subscribe:
    db.update_topic_subscriber(1,subscribe)
if publish:
    db.update_topic_publisher(1,publish)
   
msj = st.text("")
msj.text_area("Mensajes","",200)

try:

    # The callback for when the client receives a CONNACK response from the server.
    def on_connect(client, userdata, flags, rc):
        print("Connected with result code "+str(rc))       

        # Subscribing in on_connect() means that if we lose the connection and
        # reconnect then subscriptions will be renewed.
        client.subscribe(subscribe)

    # The callback for when a PUBLISH message is received from the server.
    def on_message(client, userdata, msg):
        global input_message
        
        value = ""
        for i in msg.payload:
            value += chr(i)  
                 
        input_message += value    
        msj.text_area("Mensajes",input_message,200)  
        input_message += '\n'

    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message

    client.connect(broker, 1883, 60)   

    
except:
    pass

text1 = st.empty()
value= text1.text_input("Enviar mensaje", value="", key="1")
if st.button("enviar"):
    if value:
        client.publish(publish, subscribe + ":" + value)
        text1.text_input("Enviar mensaje", value="", key="2")  


client.loop_forever()