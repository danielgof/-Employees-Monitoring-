FROM python:3.9.1
ADD . /app
WORKDIR /app
RUN apt-get update && apt-get -y install libpq-dev gcc && pip install psycopg2
RUN pip install -r requirements.txt
CMD ["python", "app.py"]
