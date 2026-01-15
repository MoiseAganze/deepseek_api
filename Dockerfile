FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

# NOTE: Ne mets pas `git pull` dans un Dockerfile (image non reproductible + credentials).
# Pour déployer: fais le pull sur l’hôte puis rebuild/restart (voir `deploy.sh`).

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8001

# HF_TOKEN must be provided at runtime (e.g. docker run -e HF_TOKEN=...)
CMD ["gunicorn", "server:app", "-k", "uvicorn.workers.UvicornWorker", "-w", "2", "-b", "0.0.0.0:8001"]
