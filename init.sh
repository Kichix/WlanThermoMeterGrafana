#!/usr/bin/env bash

DATA_DIR=$(pwd)/data
export DATA_DIR

mkdir -p ${DATA_DIR}/mosquitto/data ${DATA_DIR}/mosquitto/log ${DATA_DIR}/influxdb ${DATA_DIR}/grafana
sudo chown -R 1883:1883 ${DATA_DIR}/mosquitto
sudo chown -R 472:472 ${DATA_DIR}/grafana