FROM python:3.13

WORKDIR /app

COPY requerimientos.txt .

RUN pip install --no-cache-dir -r requerimientos.txt

COPY . .

CMD ["python", "main.py"]