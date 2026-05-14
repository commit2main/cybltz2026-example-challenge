FROM python:3.13-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .
COPY index.html .
COPY flag.txt /flag.txt

EXPOSE 8080

CMD ["python", "app.py"]
