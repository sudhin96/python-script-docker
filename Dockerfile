# Dockerfile, Image, Container
FROM python

WORKDIR /python-scripts

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY ./main.py ./main.py

CMD [ "python", "./main.py"]