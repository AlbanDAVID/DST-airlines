FROM debian:latest
EXPOSE 8050/tcp
RUN apt-get update && apt-get install python3-pip -y && pip3 
COPY requirements.txt ./requirements.txt
RUN pip install -r requirements.txt
COPY . ./home

ADD static.py /home/static.py

WORKDIR /home

CMD python3 main.py
