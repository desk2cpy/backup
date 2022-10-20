# sudo apt-get install -y mosquitto mosquitto-clients
# sudo systemctl enable mosquitto
# sudo pip3 install paho-mqtt

import paho.mqtt.publish as publish
MQTT_SERVER = "localhost"
MQTT_PATH = "test_channel"
publish.single(MQTT_PATH,"How are you", hostname = MQTT_SERVER)

