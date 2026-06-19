# FROM python: 3.8-slim-buster
# WORKDIR /app
# COPY ./ app

# RUN apt update -y && apt install awscli -y

# RUN pip install -r requirements.txt
# CMD ["python3","app.py"] 


FROM python:3.12

WORKDIR /app

COPY . .

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["python","app.py"]
