#!/usr/bin/env python3

import os
import json
import requests
import uuid
import socket

# MEC Service endpoint
MEC_SERVICE_MGMT="mec_service_mgmt/v1"

mec_base = 'http://mec-platform'

pod_namespace = os.environ['MY_POD_NAMESPACE']
pod_name = os.environ['MY_POD_NAME']

service_data = {
    "serInstanceId": "Mec-MQTT-Broker-1",
    "serName": "Mec-MQTT-Broker-Service",
    "serCategory": {
    "href": "/example/catalogue1",
    "id": "id12345",
    "name": "RNI",
    "version": "version1"
    },
    "version": "ServiceVersion1",
    "state": "ACTIVE",
    "transportInfo": {
    "id": "MqttBrokerId01",
    "name": "MQTT BROKER",
    "description": "MQTT BROKER",
    "type": "MB_TOPIC_BASED",
    "protocol": "MQTT",
    "version": "2.0",
    "endpoint": {
        "addresses":[{
            "host" : "mqtt-broker",
            "port" : "1883"
        }]  
    },
    "security": {
        "oAuth2Info": {
        "grantTypes": [
            "OAUTH2_CLIENT_CREDENTIALS"
        ],
        "tokenEndpoint": "/mecSerMgmtApi/security/TokenEndPoint"
        }
    },
    "implSpecificInfo": {}
    },
    "serializer": "JSON",
    "scopeOfLocality": "MEC_SYSTEM",
    "consumedLocalOnly": False,
    "isLocal": True
}

app_instance_id = uuid.uuid1()
mec_base = os.environ['MEC_BASE']

try:
    infra = os.environ['INFRA']
    if infra =='fog':
        hostname = "{}.{}.fog.host".format(pod_name, pod_namespace) 
    else:
        hostname = "{}.{}.mec.host".format(pod_name, pod_namespace) 
except:
    hostname = "{}.{}.mec.host".format(pod_name, pod_namespace)
    
#mqtt_port = os.environ['MQTT_BROKER_SERVICE_PORT']
hostname = "{}.{}.mec.host".format(pod_name, pod_namespace)
service_data['transportInfo']['endpoint']['addresses'][0]['host'] = hostname

my_ip = socket.gethostbyname(hostname)
print("pretry {}".format(my_ip))
try:
    sink_ip = os.environ['SINK_ADDRESS']
    print("try {}".format(sink_ip))
    query_base = "http://{}/sinkme/{}".format(sink_ip, my_ip)
    print("try {}".format(query_base))
    r = requests.get(query_base)
except:
    print("Unexpected error:", sys.exc_info()[0])
print("post")
query_base = "{}/{}/applications/{}/services".format(
            mec_base,
            MEC_SERVICE_MGMT,
            app_instance_id
    )
headers = {"content-type": "application/json"}
r = requests.post(query_base, data=json.dumps(service_data), headers=headers)