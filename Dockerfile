FROM python:2.7

WORKDIR /app
ADD . /app
RUN pip2 install -r requirements.txt

CMD ["python", "run.py"]


