#!/bin/sh

/usr/local/bin/broker-startup.py

/usr/sbin/mosquitto -c /mosquitto/config/mosquitto.conf