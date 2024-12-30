FROM python:3.11

WORKDIR /app

ENV PYTHONPATH=/app

COPY requirements.txt requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

COPY ./app ./app
COPY ./files ./files

EXPOSE 5000

CMD ["python", "/app/app/__main__.py"]