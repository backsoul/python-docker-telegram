FROM python:3.10.0rc1-alpine

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

EXPOSE 0000

CMD ["python","telebot.py"]

