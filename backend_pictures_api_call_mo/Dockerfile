FROM python:3.10.1-slim

WORKDIR /app


COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip3 install -r requirements.txt

COPY . .

# EXPOSE 8080


CMD ["python", "main.py"]
