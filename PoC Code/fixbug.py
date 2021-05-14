import json

# The service we are searching in the services list to be notified on.
target_service = ''

# Default service data, this can be edited within the application
service_data =[
    {
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
                "addresses": [
                    {
                        "host": "mqtt-broker",
                        "port": "1883"
                    }
                ]
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
        "consumedLocalOnly": false,
        "isLocal": true
    },
    {
        "serInstanceId": "Mec-MQTT-1",
        "serName": "Mec-MQTT-Service",
        "serCategory": {
            "href": "/example/catalogue1",
            "id": "id12345",
            "name": "RNI",
            "version": "version1"
        },
        "version": "ServiceVersion1",
        "state": "ACTIVE",
        "transportInfo": {
            "id": "MqttPubId01",
            "name": "Start Sensing",
            "description": "Start Sensing",
            "type": "REST_HTTP",
            "protocol": "HTTP",
            "version": "2.0",
            "endpoint": {
                "addresses": [
                    {
                        "uris": "/start-sensing"
                    }
                ]
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
        "consumedLocalOnly": false,
        "isLocal": true
    }
]

# The application has been notified
application_notified = False


def test():
    global service_data
    print(type(service_data))
    print(json.dumps(service_data))

if __name__=='__main__':
    test()