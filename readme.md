# Grafana Setup for WLanThermo Nano

###Requirements
docker and docker compose need to be installed on the system

###Environment
The project starts 4 Docker containers
* Influx DB: Database which stores the measurements
* Mosquitto: MQTT Broker
* Grafana
* MQTTBridge: Program that receives the messages from the broker and saves them in the Influx DB

###Setup

Execute init.sh to create data folder to be mounted by the docker containers for persistent storage

Execute startup.sh to export the data directory as an environment variable and start the docker containers with docker compose

###Grafana setup

You can access Grafana in your browser at localhost:3000 or if accessing from another machine [IP]:3000.
Default username and password are admin/admin.

To display temperatures of available channels, add a Graph to your dashboard and select the measurement "temperature" and 
the tag "name" equalling the name of the channel you want to display. The field to display is called value.

You can also display battery charge, which is stored in the influx db under the measurement "system" and 
field "charge". A tag is not necessary.

###Credit

Took heavy inspiration from this repo: 

https://github.com/Nilhcem/home-monitoring-grafana

Thanks!
