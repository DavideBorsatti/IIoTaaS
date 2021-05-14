#!/bin/sh

set -eu

docker build --tag mosquitto-mec:latest --network host .
