FROM python:3.8-slim
WORKDIR /app
COPY ../src/ /app
RUN pip install couchbase
EXPOSE 5000
CMD ["python", "app.py"]
