FROM python:latest

ADD ./* /opt/web_api/

RUN pip install -r /opt/web_api/requirements.txt

EXPOSE 8080

ENTRYPOINT ['/usr/local/bin/python3', '/opt/web_api/manager.py']
