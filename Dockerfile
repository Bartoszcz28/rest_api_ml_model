FROM python:3.8-slim

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    build-essential \
    libssl-dev \
    libffi-dev \
    gcc \
    gfortran \
    && rm -rf /var/lib/apt/lists/*

COPY app.py /app.py
COPY class_perceptron.py /class_perceptron.py
COPY requirements.txt /requirements.txt
COPY model.pkl /model.pkl

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

CMD ["python", "app.py"]