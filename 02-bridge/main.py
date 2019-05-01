#!/usr/bin/env python3

"""A MQTT to InfluxDB Bridge

This script receives MQTT data and saves those to InfluxDB.

"""

import json
from typing import NamedTuple

import paho.mqtt.client as mqtt
from influxdb import InfluxDBClient

INFLUXDB_ADDRESS = 'influxdb'
INFLUXDB_USER = 'root'
INFLUXDB_PASSWORD = 'root'
INFLUXDB_DATABASE = 'home_db'

MQTT_ADDRESS = 'mosquitto'
MQTT_USER = 'mqttuser'
MQTT_PASSWORD = 'mqttpassword'
MQTT_TOPIC = 'home/+/+'  # [bme280|mijia]/[temperature|humidity|battery|status]
MQTT_REGEX = 'home/([^/]+)/([^/]+)'
MQTT_CLIENT_ID = 'MQTTInfluxDBBridge'

influxdb_client = InfluxDBClient(INFLUXDB_ADDRESS, 8086, INFLUXDB_USER, INFLUXDB_PASSWORD, None)


class Channel(NamedTuple):
    number: int
    name: str
    typ: int
    temp: float
    min: float
    max: float
    alarm: bool
    color: str

class System(NamedTuple):
    time: int
    soc: int
    charge: bool
    rssi: int
    unit: str

class Pitmaster(NamedTuple):
    id: int
    channel: int
    pid: int
    value: int
    set: int
    typ: str


class ThermoData(NamedTuple):
    system: System
    channel: Channel
    pitmaster: Pitmaster

def on_connect(client, userdata, flags, rc):
    """ The callback for when the client receives a CONNACK response from the server."""
    print('Connected with result code ' + str(rc))
    client.subscribe(MQTT_TOPIC)


def on_message(client, userdata, msg):
    """The callback for when a PUBLISH message is received from the server."""
    channel = _parse_mqtt_message(msg.topic, msg.payload.decode('utf-8'))

    for c in channel:
        if c is not None:
            _send_thermo_data_to_influxdb(c)


def _parse_mqtt_message(topic, payload):
    dataObj = json.load(payload)
    return dataObj["channel"]


def _send_thermo_data_to_influxdb(channel):
    json_body = [
        {
            'number': channel.number,
            'name': channel.name,
            'typ': channel.typ,
            'temp': channel.temp,
            'min': channel.min,
            'max': channel.max,
            'alarm': channel.alarm,
            'color': channel.color
        }
    ]
    influxdb_client.write_points(json_body)


def _init_influxdb_database():
    databases = influxdb_client.get_list_database()
    if len(list(filter(lambda x: x['name'] == INFLUXDB_DATABASE, databases))) == 0:
        influxdb_client.create_database(INFLUXDB_DATABASE)
    influxdb_client.switch_database(INFLUXDB_DATABASE)


def main():
    _init_influxdb_database()

    mqtt_client = mqtt.Client(MQTT_CLIENT_ID)
    mqtt_client.username_pw_set(MQTT_USER, MQTT_PASSWORD)
    mqtt_client.on_connect = on_connect
    mqtt_client.on_message = on_message

    mqtt_client.connect(MQTT_ADDRESS, 1883)
    mqtt_client.loop_forever()


if __name__ == '__main__':
    print('MQTT to InfluxDB bridge')
    main()
