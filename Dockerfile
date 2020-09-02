FROM tiangolo/uwsgi-nginx:python3.7

COPY ./app /app
COPY requirements.txt /
RUN pip install -r requirements.txt

WORKDIR /app

CMD ["gunicorn", "main:app", "-b", "0.0.0.0:80"]
