import flask
from flask_mqtt import Mqtt
from flask import Flask, render_template, request, jsonify
from paho.mqtt.client import Client as MQTTClient
from datetime import datetime
from flaskr.engine.controller import process_wash_topic
from flaskr.utils.configurator import read_config
from flaskr.utils.email_sender import send_email

configuration = read_config('config.yaml')
wash_state = {}
start_wash_timestamp_state = {}
end_wash_timestamp_state = {}

app = Flask(__name__, static_url_path='', static_folder='flaskr/static', template_folder='flaskr/templates')
app.config['MQTT_BROKER_URL'] = configuration['mqtt_info']['broker']['ip']
app.config['MQTT_BROKER_PORT'] = configuration['mqtt_info']['broker']['port']
mqtt = Mqtt(app)
mqtt_topics = configuration['mqtt_info']['topics']
topic_names = [topic['name'] for topic in mqtt_topics]
mqtt_client = MQTTClient()
mqtt_client.connect(app.config['MQTT_BROKER_URL'], app.config['MQTT_BROKER_PORT'])


@mqtt.on_connect()
def handle_connect(client, userdata, flags, rc):
    client.subscribe([(topic_names[0], 0), (topic_names[1], 0)])


@mqtt.on_message()
def handle_mqtt_message(client, userdata, message):
    topic = message.topic
    payload = message.payload.decode()
    val = float(payload)
    process_wash_topic(topic, payload, wash_state, wash_timestamp_state)


@app.route('/email_action', methods=["POST"])
def email_call():
    if request.method == "POST":
        result = send_email(request.form.get('email'), request.form.get('name'),
                                request.form.get('subject'), request.form.get('message'),
                            configuration['email']['sender']['email_s'],
                            configuration['email']['sender']['email_s_pass'])
        return render_template('index.html', email_status=result)


@app.route('/check_status', methods=['GET'])
def check_wash_status():
    wash_statuses = {}
    for topic in mqtt_topics:
        topic_name = topic['name']
        wash_statuses[topic_name] = {
            'state': wash_state.get(topic_name, False),
            'time': wash_timestamp_state.get(topic_name, None)
        }
    return jsonify(wash_statuses)


@app.route('/', methods=['GET'])
def init():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=configuration['web_info']['flask']['port'], debug=True)
