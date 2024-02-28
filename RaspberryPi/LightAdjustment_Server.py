from flask import Flask, request, jsonify
import json
import paho.mqtt.client as mqtt
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
# Mosquitto MQTT Settings
mqtt_broker_address = "your ip"  # Replace with your actual MQTT broker IP
mqtt_topic = "trial/esp"

received_data = {}  # Store received data here

def on_message(client, userdata, message):
    payload = message.payload.decode("utf-8")
    print("Received data from ESP32:", payload)
    #temp=json.dumps(payload)
    # Store the received data
    global received_data
    received_data = json.loads(payload)

# Set up MQTT client
mqtt_client = mqtt.Client()
mqtt_client.username_pw_set("mqttuser","pass")
mqtt_client.on_message = on_message

# Connect to the MQTT broker
mqtt_client.connect(mqtt_broker_address)
mqtt_client.subscribe(mqtt_topic)
mqtt_client.loop_start()

# Route to handle incoming requests
@app.route('/', methods=['GET'])
def get_data():
    global received_data
    return jsonify(received_data)

if __name__ == '__main__':
    app.run(host='your ip', port=1500)
