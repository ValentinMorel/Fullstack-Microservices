FROM python:3

RUN apt-get update 

WORKDIR /app
COPY requirements.txt ./
RUN pip3 install --no-cache-dir -r requirements.txt

COPY config.yaml ./
COPY run_service.sh ./
COPY gateway.py ./

RUN chmod +x ./run_service.sh

CMD ["./run_service.sh"]