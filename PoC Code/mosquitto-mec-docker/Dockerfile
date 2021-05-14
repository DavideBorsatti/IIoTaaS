FROM eclipse-mosquitto

RUN apk update
RUN apk add python3
RUN apk add py3-requests

ENV MY_POD_NAMESPACE=mec
ENV MEC_BASE=mec
ENV MY_POD_NAME=mec

COPY broker-startup.py /usr/local/bin/broker-startup.py
RUN chmod +x /usr/local/bin/broker-startup.py
COPY run-mec-mqtt.sh /home/run-mec-mqtt.sh
RUN chmod +x /home/run-mec-mqtt.sh
#RUN /usr/local/bin/broker-startup.py
CMD /home/run-mec-mqtt.sh
#CMD ["/usr/local/bin/broker-startup.py" "/usr/sbin/mosquitto" "-c" "/mosquitto/config/mosquitto.conf"]