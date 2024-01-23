FROM python:3.7-slim-stretch

COPY ./ /app
WORKDIR /app

RUN pip install .

EXPOSE 8080

ENTRYPOINT ["cfexpose", "export", "config.yaml"]
