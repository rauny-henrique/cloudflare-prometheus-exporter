FROM python:3.7

RUN apt-get update && apt-get install -y git nano

WORKDIR /app

COPY . .

# install dependencies
RUN pip install --upgrade pip
RUN pip install --no-cache .

# fix timezone
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime \
  && echo $TZ > /etc/timezone

EXPOSE 8080

ENTRYPOINT ["cfexpose", "export", "config.yaml"]
