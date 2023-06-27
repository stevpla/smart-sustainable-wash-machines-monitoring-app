# Wash Machines Monitoring Service
## _A project from students to students_

[![N|Solid](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQdtwNII_IsIkRnxT5jhpb_i84wVEY2eBCTrNaELBnSBjM6RRlmIdlW5IerHhLCxU9Jdes&usqp=CAU)](https://www.aegean.gr/)


Wash Machines Monitoring Service is an end-to-end full stack project providing web interface for live wash machines state monitoring for the optimal students time management. This project implemented by students of University of the Aegean to the students of this university and it is placed in the Samos island, in the students reside building.

## Hardware, Software and Protocols

- Hardware: ESP 32 board, Raspberry Pi 3 Model B+, Ampere sensors x 2
- Software: Python 3.10, Flask, flask_mqtt, CPP
- Mosquito Broker, MQTT
- HTML, JS, CSS


> Hardware, software and protocols are merged up together to create a web service in which the live state of the wach machines is being displayed. It is a 4-tier architecture.


## Architecture

Here, image of 4-tier architecture will be placed and a brief description regarding each tier.

### 1-Tier (ESP32)

### 2-Tier (Mosquito Broker)

### 3-Tier (Python MQTT Client)

### 4-Tier (Python Flask Web Service)

### Client-Side

## Installation

Dillinger requires [Node.js](https://nodejs.org/) v10+ to run.

Install the dependencies and devDependencies and start the server.

```sh
cd dillinger
npm i
node app
```

## Development

Guidelines in case somebody wants to create this project and develop it in a real environment.
Want to contribute? Great!

Dillinger uses Gulp + Webpack for fast developing.
Make a change in your file and instantaneously see your updates!

Open your favorite Terminal and run these commands.

First Tab:

```sh
node app
```

Second Tab:

```sh
gulp watch
```

(optional) Third:

```sh
karma test
```


## People
- Nikos Rekkas, Vasilis Kartitzoglou and Stefanos Plastras, all students and alumni from University of the Aegean were involved in the design, implementaion, testing and installation of this project.

### Nikos Rekkas
- Currently, he is working as software engineer in ABS COMPANY. He holds MEng from Department of Information and Communication Systems Engineering from University of the Aegean.  
Email: nikos.rekkas@gmail.com  
Github: [nikosrk](https://github.com/nikosrk)  

### Stefanos Plastras
- Currently, he is doing his PhD studies in networks. He holds a MEng from Dept. of Information and Communication Systems Engineering and a MSc from Athens University of Economics & Business.  
Email: s.plastras@gmail.com   
Github: [stevpla](https://github.com/stevpla)


## License
