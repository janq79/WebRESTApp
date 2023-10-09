FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY rest_app.py db_connector.py wait-for-it.sh docker_backend_testing.py /app/
RUN chmod +x /app/wait-for-it.sh
ENV RUNNING_IN_DOCKER True
CMD ["python", "rest_app.py"]