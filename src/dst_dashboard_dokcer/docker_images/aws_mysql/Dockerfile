FROM debian:latest

RUN apt-get update && apt-get install python3-pip -y && pip3 
RUN pip3 install pymysql
RUN pip3 install pandas
RUN pip3 install numpy
RUN pip3 install datetime

ADD aws_testing.py /home/aws_test/aws_testing.py

ADD static.py /home/aws_test/static.py

WORKDIR /home/aws_test

CMD python3 aws_testing.py
