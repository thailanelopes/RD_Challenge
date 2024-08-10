FROM python:3.8-slim

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt || echo "No dependencies to install"

CMD ["python", "-m", "unittest", "discover"]
