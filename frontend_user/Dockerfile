# frontend_user/Dockerfile

#FROM python:3.7-slim
FROM datamachines/jupyter_to:latest

WORKDIR /app

COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN pip install opencv-python
RUN pip install uuid
RUN pip install request

ADD . .

EXPOSE 8501

VOLUME /volume_front_end

ENV PATH=“${PATH}:/root/.local/bin

HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

ENTRYPOINT ["streamlit", "run", "--server.port=8501", "--server.address=0.0.0.0"]

CMD [ "main.py"]