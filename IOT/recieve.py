import paho.mqtt.client as mqtt

# Global list to store incoming data
mqtt_data_list = []

# Callback function to handle incoming MQTT messages
def on_message(client, userdata, message):
    mqtt_data_list.append(message.payload)
    print(f"Receiveddddd data: {message.payload}")
    save_to_pcm_file(message.payload)
def save_to_pcm_file(raw_data):
    file_path = "output.pcm"
    with open(file_path, "ab") as pcm_file:
        pcm_file.write(raw_data)
def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")
    client.subscribe("trial")
# Set up MQTT client
mqtt_client = mqtt.Client()
mqtt_client.username_pw_set("test","123456789")
mqtt_client.on_connect = on_connect
mqtt_client.on_message = on_message

# Connect to the MQTT broker
mqtt_broker_address = "192.168.29.137"  # Replace with your actual MQTT broker IP or hostname
mqtt_topic = "audio"  # Replace with your actual MQTT topic
# mqtt_client.connect(mqtt_broker_address)
mqtt_client.connect(mqtt_broker_address, 1883, 60)

mqtt_client.subscribe(mqtt_topic)

# Start the MQTT client loop
mqtt_client.loop_start()

# Wait for incoming MQTT messages
while True:
    pass  # Add any additional logic if needed





