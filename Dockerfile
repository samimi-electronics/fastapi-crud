FROM python:3.10-slim
WORKDIR /api
COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./app /api/app

CMD [ "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]