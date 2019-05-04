#!/usr/bin/env bash

sudo apt-get install apt-transport-https ca-certificates curl software-properties-common
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu xenial stable"
sudo apt-get update

sudo apt-get -y install docker-compose

sudo usermod -aG docker pi

DATA_DIR=$(pwd)/data

mkdir -p ${DATA_DIR}/mosquitto/data ${DATA_DIR}/mosquitto/log ${DATA_DIR}/influxdb ${DATA_DIR}/grafana
sudo chown -R 1883:1883 ${DATA_DIR}/mosquitto
sudo chown -R 472:472 ${DATA_DIR}/grafana