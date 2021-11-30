FROM python:3.8.5

WORKDIR /APP
COPY requrements.txt .
RUN pip install -r requirements.txt
COPY  /APP .



CMD [ "python","main.py" ]