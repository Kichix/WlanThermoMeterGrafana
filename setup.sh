#!/usr/bin/env bash

cd 01-mosquitto
docker run -d -p 1883:1883 -v $PWD/mosquitto.conf:/mosquitto/config/mosquitto.conf -v $PWD/users:/mosquitto/config/users -v $DATA_DIR/mosquitto/data:/mosquitto/data -v $DATA_DIR/mosquitto/log:/mosquitto/log --name mosquitto eclipse-mosquitto:1.5
cd -

docker run -d -p 8086:8086 -v $DATA_DIR/influxdb:/var/lib/influxdb --name influxdb influxdb:1.7

cd 02-bridge
docker build -t michaelhalemba/mqttbridge .
docker run -d --name mqttbridge michaelhalemba/mqttbridge
cd -

docker run -d -p 3000:3000 -v $DATA_DIR/grafana:/var/lib/grafana --name=grafana grafana/grafana:5.4.3