FROM python:3.10.0rc1-alpine

WORKDIR /app
COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt
COPY . .
CMD python app.py --host=0.0.0.0