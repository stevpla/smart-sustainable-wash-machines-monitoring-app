from datetime import datetime


def start_wash1_validator(ampere_value, wash_state_1, flag1, static_counter_start_wash_1,
                          static_counter_complete_wash_1, wash_1_timestamp_state):
    val = float(ampere_value)
    # Check for 3 consecutive times if ampere has more than 0.24 value
    if val < 0.21:
        if flag1 == 0:
            pass
        if flag1 == 1:
            if static_counter_complete_wash_1 == 6:
                # reset flag to 0 - wash is available
                flag1 = 0
                # reset counter
                static_counter_complete_wash_1 = 0
                #
                wash_state_1 = False
            else:
                static_counter_complete_wash_1 = static_counter_complete_wash_1 + 1
    if val > 0.22:
        if flag1 == 0:
            if static_counter_start_wash_1 == 3:
                # mark the flag 1 => wash is running
                flag1 = 1
                # reset counter
                static_counter_start_wash_1 = 0
                wash_state_1 = True
                wash_1_timestamp_state = datetime.now().strftime("%H:%M:%S")
            else:
                static_counter_start_wash_1 = static_counter_start_wash_1 + 1


def start_wash2_validator(ampere_value, wash_state_2, flag2, static_counter_start_wash_2,
                          static_counter_complete_wash_2, wash_2_timestamp_state, xd):


    val = float(ampere_value)
    if val < 0.21:
        if flag2 == 0:
            xd = 7
            print('NO WASH 2................................')
            pass
        if flag2 == 1:
            if static_counter_complete_wash_2 == 6:
                # reset flag to 0 - wash is available
                flag2 = 0
                # reset counter
                static_counter_complete_wash_2 = 0
                wash_state_2 = False
            else:
                static_counter_complete_wash_2 = static_counter_complete_wash_2 + 1
    if val > 0.22:
        if flag2 == 0:
            if static_counter_start_wash_2 == 3:
                # mark the flag 1 => wash is running
                flag2 = 1
                # reset counter
                static_counter_start_wash_2 = 0
                # Start countup timer in index.html
                wash_state_2 = True
                wash_2_timestamp_state = datetime.now().strftime("%H:%M:%S")
                print('sdas -> ', wash_2_timestamp_state)
            else:
                static_counter_start_wash_2 = static_counter_start_wash_2 + 1

