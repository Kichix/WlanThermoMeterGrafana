# Grafana Setup for WLanThermo Nano

###requirements
docker and docker compose need to be installed on the system

###setup

execute init.sh to create data folder to be mounted by the docker containers for persistent storage

execute startup.sh to export the data directory as an environment variable and start the docker containers with docker compose

###Grafana setup

To display temperatures of available channels, select the measurement "temperature" and 
the tag "name" equalling the name of the channel you want to display. The field to display is called value.

You can also display battery charge, which is stored in the influx db under the measurement "system" and 
field "charge". A tag is not necessary.
