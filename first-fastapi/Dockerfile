FROM python:3.10.6

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY ./app ./app

CMD [ "uvicorn", "--host", "0.0.0.0","--port", "8000", "--reload", "main:app" ]