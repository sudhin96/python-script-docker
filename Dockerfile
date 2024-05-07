# Dockerfile, Image, Container
FROM python

WORKDIR /python-scripts

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY ./app/main.py ./app/main.py

CMD [ "python", "./app/main.py"]