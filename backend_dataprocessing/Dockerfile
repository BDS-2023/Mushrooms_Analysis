# backend_dataprocessing/Dockerfile

FROM python:3.10.1-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN pip freeze > requirements.txt

ADD . .

EXPOSE 8502

VOLUME /volume_back_end

#ENV PATH=“${PATH}:/root/.local/bin

HEALTHCHECK CMD curl --fail http://localhost:8502/_stcore/health

ENTRYPOINT ["run", "--server.port=8502"]

CMD [ "main.py"]