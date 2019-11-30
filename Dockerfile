FROM python:3.8-slim
WORKDIR /app

COPY requirements.txt .
RUN pip3 install --no-cache-dir wheel && pip3 install --no-cache-dir -r requirements.txt

COPY main.py .
CMD ["python3", "-u", "/app/main.py"]
