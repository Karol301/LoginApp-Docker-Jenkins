#stage 1
FROM python:3.12-slim AS build

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir --target=/app/deps -r requirements.txt

#stage 2
FROM python:3.12-slim AS final

ENV PYTHONPATH="/app/deps"

WORKDIR /app

COPY --from=build /app/deps /app/deps

COPY app.py .
COPY user_interface.py .
COPY database_manager.py .

CMD ["python", "app.py"] 