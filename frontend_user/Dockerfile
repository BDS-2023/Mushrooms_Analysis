# frontend_user/Dockerfile

FROM python:3.10.1-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN pip freeze > requirements.txt

ADD . .

EXPOSE 8501

VOLUME /volume_front_end

#ENV PATH=“${PATH}:/root/.local/bin

HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

ENTRYPOINT ["streamlit", "run", "--server.port=8501", "--server.address=0.0.0.0"]

CMD [ "main.py"]