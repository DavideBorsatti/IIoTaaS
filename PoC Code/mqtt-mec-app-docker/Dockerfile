FROM alpine

RUN apk update
RUN apk add python3
RUN apk add py3-flask
RUN apk add py3-requests
RUN apk add py3-paho-mqtt

ENV MY_POD_NAMESPACE=mec
ENV MEC_BASE=mec
ENV MY_POD_NAME=mec

COPY app.py /usr/local/bin/app.py
COPY app_site /var/www/
RUN chmod +x /usr/local/bin/app.py
EXPOSE 80

CMD /usr/local/bin/app.py
