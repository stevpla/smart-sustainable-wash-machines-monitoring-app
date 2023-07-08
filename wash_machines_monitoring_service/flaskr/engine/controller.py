from datetime import datetime


static_counter_complete_wash = -10

def process_wash_topic(topic, payload, wash_state, wash_timestamp_state):
    global static_counter_complete_wash
    topic_name = topic['name']
    val = float(payload)

    if topic_name not in wash_state:
        wash_state[topic_name] = False

    if topic_name not in wash_timestamp_state:
        wash_timestamp_state[topic_name] = None

    if 0.16 >= val > 0.01:
        if wash_state[topic_name]:
            if static_counter_complete_wash == 12:
                wash_state[topic_name] = False
                static_counter_complete_wash = 0
            else:
                static_counter_complete_wash += 1
    elif val >= 0.17:
        if not wash_state[topic_name]:
            if static_counter_complete_wash == 5:
                wash_state[topic_name] = True
                static_counter_complete_wash_b = 0
                wash_timestamp_state[topic_name] = datetime.now().strftime("%H:%M:%S")
            else:
                static_counter_complete_wash += 1
