# MQTT to InfluxDB Bridge

## Build

```sh
$ docker build -t kichix/mqttbridge .
```


## Run

```sh
$ docker run -d --name mqttbridge kichix/mqttbridge
```


## Dev

```sh
$ docker run -it --rm -v `pwd`:/app --name python python:3.7-alpine sh
```
