# Wash Machines Monitoring Service
**_A project from students to students_**

[![N|Solid](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQdtwNII_IsIkRnxT5jhpb_i84wVEY2eBCTrNaELBnSBjM6RRlmIdlW5IerHhLCxU9Jdes&usqp=CAU)](https://www.aegean.gr/)


Wash Machines Monitoring Service is an end-to-end full stack project providing web interface for wash machines live state monitoring for the optimal students time management. This project have been implemented by alumni and students of University of the Aegean to the students of this university and it is placed in the Samos island, in the students reside building.

## Hardware, Software and Protocols
This project, combines concepts and technologies from physical layer such ar esp32, software layers such as Python, CSS and middle layer such as mosquitto protocol. Hardware, software and protocols are merged up together to create a web service in which the live state of the wach machines is being displayed. It is a 4-tier architecture.Specifically, our project includes these technologies per layer:
- Hardware: ESP 32 board, Raspberry Pi 3 Model B+, Ampere sensors x 2
- Software: Python 3.10, CSS, HTML, JavaScript, CPP firmware
- Middleware: Mosquito Broker, MQTT
- Web Layer: Flask-MQTT


## Application Architecture
![Image Description](wash_machines_monitoring_service/flaskr/static/img/mqtt-protocol3.png.png)

### 1-Tier (Data Producer)

### 2-Tier (Broker)

### 3-Tier (Data Consumer)

### 4-Tier (Web Service)

### Front-End (Client-Side)

## Installation



## Before Installation
*Please, before install all the necesseray libs and scripts, make sure that you have
the right hardware connected and that you are ready to start!*

- You better check these:

| Tools | Description |
| ---- | -------------------------------------------|
| [ESP32 MCU](http://esp32.net/) | Cpp firmware execution, data producing|
| [Raspberry Pi 3 Model B+](https://www.raspberrypi.com/products/raspberry-pi-3-model-b-plus/) | Running Rasbian OS, mosquitto broker service, Python App execution|
| [SCT-013-030 Non-invasive AC Current Sensor](https://www.cableworks.gr/ilektronika/arduino-and-microcontrollers/mcu-and-components/current-voltage/30a-sct-013-030-non-invasive-ac-current-sensor-for-arduino//) | Sensing Wach machines electric current|
    
## Application Installation & Execution
Guidelines in case somebody wants to create this project and develop it in a real environment.
Want to contribute? Great!
### Phase A: Prepare App Environment
    1. Flash cpp firmware code to esp32 board
    2. Install mosquitto lib to Raspberry Pi 3 Model B+
        - Rasbian:  $ sudo apt-get install mosquitto
    3. Make mosquitto service to autorestart on every system boot (eg, power failure).
        - Rasbian:  $ sudo systemctl enable --now mosquitto.service
      
 

### Phase B: Install Python Libraries - Execute Python App
    There are 2 scripts for windows (.bat) and Linux (.sh) respectively, that offers installation automation. Only thing that is needed is running one of these scripts. Navigate to python project and: 
    1. ./setup_python_project_linux.sh (first, run this: $ chmod +x setup_python_project_linux.sh)
    2. ./setup_python_project_linux.bat
*At the end of these scripts, the main.py will be executed!*

### Phase C: Make Python Service a system service
    1.
    2.



First Tab:

```sh
node app
```

Second Tab:

```sh
gulp watch
```


```sh
cd dillinger
npm i
node app
```

(optional) Third:

```sh
karma test
```


## People
Nikos Rekkas, Vasilis Kartitzoglou and Stefanos Plastras, alumni from University of the Aegean, were involved in the design, implementaion, testing and installation of this project.

### Nikos Rekkas
- Currently, he is working as software engineer in ABS COMPANY. He holds a MEng from the Department of Information and Communication Systems Engineering of University of the Aegean.  
Email: nrekkas@gmail.com  
Github: [nikosrk](https://github.com/nikosrk)  

### Stefanos Plastras
- Currently, he is doing his PhD studies in wireless networks. He holds a MEng from Dept. of Information and Communication Systems Engineering and a MSc from Athens University of Economics & Business.  
Email: s.plastras@gmail.com   
Github: [stevpla](https://github.com/stevpla)


## License
