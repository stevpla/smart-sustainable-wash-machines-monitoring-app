import flask
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import paho.mqtt.client as mqtt
import time
from flask_mqtt import Mqtt
from datetime import datetime
import requests as requests
from flask import Flask, render_template, request, jsonify

app = flask.Flask(__name__, static_url_path='', static_folder='flaskr\\static',
                  template_folder='flaskr\\templates')
app.config['MQTT_BROKER_URL'] = '10.10.10.151'
app.config['MQTT_BROKER_PORT'] = 1883
mqtt = Mqtt(app)

global filename1, filaneme2
filename1 = "wash1.txt"
filename2 = 'wash2.txt'


@mqtt.on_connect()
def handle_connect(client, userdata, flags, rc):
    client.subscribe([("wash_samos_1/ampere", 0), ("wash_samos_2/ampere", 0)])


@mqtt.on_message()
def handle_mqtt_message(client, userdata, message):
    topic = message.topic
    payload = message.payload.decode()

    if topic == 'wash_samos_1/ampere':
        str1 = "Topic: ", topic, " -> Message:  ", payload, " Timestamp: ", datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        with open(filename1, "a") as file:
            file.write(str(str1) + '\n')
    elif topic == 'wash_samos_2/ampere':
        str2 = "Topic: ", topic, " -> Message:  ", payload, " Timestamp: ", datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        with open(filename2, "a") as file:
            file.write(str(str2) + '\n')


@app.route('/email_action', methods=["GET", "POST"])
def email_call():
    if request.method == "POST":
        print(request.values)
        # SEND MESSAGE TO EMAIL s.plastras@gmail.com and nikosrekkas@gmail.com
        # FILL CODE PYTHON HERE
        # ------------------------------------------------------------------
        # ------------------------------------------------------------------
        # ------------------------------------------------------------------
        # render same page with message that email was sent!
    return render_template('index.html')


'''
@app.route('/test_page_dynamic_reload')
def index():
    return render_template('dy1.html')

@app.route('/_stuff', methods=['GET'])
def stuff():
    x = 9
    # return jsonify(result=str(global_var))
    return render_template('index.html')
'''

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=1924)
