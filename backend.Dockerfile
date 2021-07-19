FROM python:3.7.11-slim-buster

WORKDIR /app

COPY backend .

RUN pip install -r requirements.txt

EXPOSE 8002

RUN chmod a+x /app/main.py
RUN chmod a+x /app/gunicorn_config.py

CMD ["gunicorn","--config","/app/gunicorn_config.py","main:app"]

