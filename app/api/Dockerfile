FROM python:3.9

WORKDIR /api

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY .. /api

CMD ["cd", "api"]

CMD ["uvicorn", "main:api", "--host", "0.0.0.0", "--port", "5000"]
