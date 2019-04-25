FROM python:3.7.3
COPY . /src
RUN pip3 install pymysql && \
    pip3 install DBUtils && \
    pip3 install ConfigParser
WORKDIR /src
CMD ["python", "./src/test.py"]