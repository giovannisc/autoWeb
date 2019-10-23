FROM postgres:latest

COPY requirements.txt ./

RUN apt update -y && \
apt upgrade -y && \
apt install -y python3 python3-dev python3-pip && \
pip3 install --upgrade pip && \
pip3 install --no-cache-dir -r requirements.txt

ADD ./app /home/app/

WORKDIR /home/app/

EXPOSE 8000

ENTRYPOINT ["python3", "autoWeb.py"]



