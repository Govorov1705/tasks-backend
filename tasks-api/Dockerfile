FROM python:3.12.4-alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

EXPOSE 8000

COPY ./requirements.txt .
RUN pip install --upgrade pip && \
    pip install -r requirements.txt --no-cache-dir

COPY . .

RUN apk add --update --no-cache netcat-openbsd && \
    apk add --update --no-cache postgresql-client && \
    apk add --update --no-cache --virtual .tmp-deps \
        build-base postgresql-dev musl-dev && \
    apk del .tmp-deps && \
    cat temp_entrypoint.sh | tr -d '\r' >> entrypoint.sh && \
    rm temp_entrypoint.sh

ENTRYPOINT [ "sh", "./entrypoint.sh" ]
