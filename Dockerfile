FROM python3.9-slim-buster

WORKDIR /myportfolio

RUN pip3 install -r requirements.txt

COPY . .

CMD ["flask", "run", "--host=0.0.0.0"]

EXPOSE 5000
