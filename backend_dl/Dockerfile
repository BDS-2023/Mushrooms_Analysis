
FROM python:3.10.1-slim
#CHANGE AND PUT NVIDIA IMAGE

WORKDIR /app

RUN apt-get update
RUN apt-get install \
    'ffmpeg'\
    'libsm6'\
    'libxext6'  -y

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8081

VOLUME [ "/common_storage/" ]

CMD ["python", "main.py"]

#'ffmpeg', 'libsm6', and 'libxext6' are required for OpenCV.