FROM python:3.9-slim
WORKDIR /app
RUN apt-get update && apt-get install -y \
    build-essential \
    python3-dev \
    python3-pip \
    && rm -rf /var/lib/apt/lists/*
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY app/ .
COPY .env .
RUN mkdir -p chat_history generated_images
ENV PYTHONUNBUFFERED=1
ENTRYPOINT ["python", "chat.py"]
