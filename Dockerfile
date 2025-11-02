FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

COPY lab5/tracking_system_backend/App/requirements.txt ./requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY lab5/tracking_system_backend /app

ENV PORT=8000

CMD ["bash","-lc","gunicorn -w 2 -b 0.0.0.0:${PORT} App.project.app:app"]
