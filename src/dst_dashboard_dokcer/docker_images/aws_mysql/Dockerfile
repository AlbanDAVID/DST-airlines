FROM debian:latest

RUN apt-get update && apt-get install python3-pip -y && pip3 
RUN pip3 install pymysql
RUN pip3 install pandas
RUN pip3 install numpy
RUN pip3 install datetime

ADD aws_test.py /home/aws_test/aws_test.py

ADD static.py /home/aws_test/static.py

WORKDIR /home/aws_test

CMD python3 aws_test.py