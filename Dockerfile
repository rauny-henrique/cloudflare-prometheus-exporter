FROM python:3.7

RUN apt-get update && apt-get install -y git nano

# RUN git clone https://github.com/rauny-henrique/cloudflare-prometheus-exporter.git /app

COPY ./config.yaml /config.yaml
COPY ./logging.yaml /logging.yaml
COPY ./cloudflare_exporter/gql/accounts.httpRequests1hGroups.graphql /gql/accounts.httpRequests1hGroups.graphql
COPY ./cloudflare_exporter/gql/zones.httpRequests1hGroups.graphql /gql/zones.httpRequests1hGroups.graphql
COPY ./cloudflare_exporter/gql/zones.httpRequests1mGroups.graphql /gql/zones.httpRequests1mGroups.graphql

WORKDIR /app

COPY . .

# install dependencies
RUN pip install --upgrade pip
RUN pip install --no-cache .

# fix timezone
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime \
  && echo $TZ > /etc/timezone

EXPOSE 8080

ENTRYPOINT ["cfexpose", "export", "/config.yaml"]
