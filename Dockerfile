FROM python:3.11

COPY main.py requirements.txt /app/
WORKDIR /app

RUN pip install -r requirements.txt

CMD ["python", "main.py"]