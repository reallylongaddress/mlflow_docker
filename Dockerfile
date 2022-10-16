FROM gcr.io/getindata-images-public/mlflow:latest
ENV TINI_VERSION v0.19.0
EXPOSE 4180

RUN apt update
# RUN apt -f upgrade

RUN apt install -y curl netcat && mkdir -p /oauth2-proxy && cd /oauth2-proxy && \
    curl -L -o proxy.tar.gz https://github.com/oauth2-proxy/oauth2-proxy/releases/download/v6.1.1/oauth2-proxy-v6.1.1.linux-amd64.tar.gz && \
    tar -xzf proxy.tar.gz && mv oauth2-proxy-*.linux-amd64/oauth2-proxy . && rm proxy.tar.gz && \
    rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade setuptools

#Must update first, else will not work
RUN apt-get update
RUN apt-get -y install gcc
RUN apt-get -y install default-libmysqlclient-dev

COPY requirements.txt .
RUN pip install -r requirements.txt

ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini /tini
RUN chmod +x /tini

COPY start.sh start.sh
RUN chmod +x start.sh

ENTRYPOINT ["/tini", "--", "./start.sh"]
