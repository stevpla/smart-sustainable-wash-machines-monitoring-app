import flask
from flask_mqtt import Mqtt
from flask import Flask, render_template, request, jsonify
import paho.mqtt.client as mqtt
import time
from datetime import datetime
import requests as requests
from flaskr.engine.controller import start_wash1_validator, start_wash2_validator

app = flask.Flask(__name__, static_url_path='', static_folder='flaskr\\static',
                  template_folder='flaskr\\templates')
app.config['MQTT_BROKER_URL'] = '10.10.10.151'
app.config['MQTT_BROKER_PORT'] = 1883
mqtt = Mqtt(app)


wash_state_1 = False
wash_state_2 = False

static_counter_start_wash_1 = 0
static_counter_complete_wash_1 = 0
static_counter_complete_wash_1_b = 0
flag1 = 0
wash_1_timestamp_state = None

static_counter_start_wash_2 = 0
static_counter_complete_wash_2 = 0
static_counter_complete_wash_2_b = 0
flag2 = 0
wash_2_timestamp_state = None


@mqtt.on_connect()
def handle_connect(client, userdata, flags, rc):
    client.subscribe([("wash_samos_1/ampere", 0), ("wash_samos_2/ampere", 0)])


@mqtt.on_message()
def handle_mqtt_message(client, userdata, message):

    global wash_state_1, static_counter_start_wash_1, static_counter_complete_wash_1, \
        flag1, static_counter_complete_wash_1_b, wash_1_timestamp_state
    global wash_state_2, static_counter_start_wash_2, static_counter_complete_wash_2, \
        static_counter_complete_wash_2_b, flag2, wash_2_timestamp_state

    topic = message.topic
    payload = message.payload.decode()
    val = float(payload)

    if topic == 'wash_samos_1/ampere':
        if 0.16 > val > 0.01:
            if flag1 == 1:
                if static_counter_complete_wash_1 == 12:
                    flag1 = 0
                    static_counter_complete_wash_1 = 0
                    wash_state_1 = False
                else:
                    static_counter_complete_wash_1 = static_counter_complete_wash_1 + 1
        if 0.17 < val < 5:
            if flag1 == 0:
                if static_counter_complete_wash_1_b == 5:
                    flag1 = 1
                    wash_state_1 = True
                    static_counter_complete_wash_1_b = 0
                    wash_1_timestamp_state = datetime.now().strftime("%H:%M:%S")
                else:
                    static_counter_complete_wash_1_b = static_counter_complete_wash_1_b + 1
        if val > 1.00:
            if flag1 == 0:
                flag1 = 1
                wash_state_1 = True
                wash_1_timestamp_state = datetime.now().strftime("%H:%M:%S")
    elif topic == 'wash_samos_2/ampere':
        if 0.16 > val > 0.01:
            if flag2 == 1:
                if static_counter_complete_wash_2 == 12:
                    flag2 = 0
                    static_counter_complete_wash_2 = 0
                    wash_state_2 = False
                else:
                    static_counter_complete_wash_2 = static_counter_complete_wash_2 + 1
        if 0.17 < val < 5:
            if flag2 == 0:
                if static_counter_complete_wash_2_b == 5:
                    flag2 = 1
                    wash_state_2 = True
                    static_counter_complete_wash_2_b = 0
                    wash_2_timestamp_state = datetime.now().strftime("%H:%M:%S")
                else:
                    static_counter_complete_wash_2_b = static_counter_complete_wash_2_b + 1
        if val > 1.00:
            if flag2 == 0:
                flag2 = 1
                wash_state_2 = True
                wash_2_timestamp_state = datetime.now().strftime("%H:%M:%S")


@app.route('/email_action', methods=["GET", "POST"])
def email_call():
    if request.method == "POST":
        print(request.values)
        # SEND MESSAGE TO EMAIL s.plastras@gmail.com and nikosrekkas@gmail.com
        # FILL CODE PYTHON HERE
        # render same page with message that email was sent!
    return render_template('index.html', condition_met1=False)


@app.route('/check_status', methods=['GET'])
def check_wash_status():
    global wash_state_1, wash_1_timestamp_state
    global wash_state_2, wash_2_timestamp_state
    print(wash_2_timestamp_state)
    return jsonify(state1=wash_state_1, state2=wash_state_2, time1=wash_1_timestamp_state, time2=wash_2_timestamp_state)


@app.route('/', methods=['GET'])
def init():
    return render_template('index.html')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
