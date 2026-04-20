# Mini-RAG

A clean, minimal implementation of a Retrieval-Augmented Generation (RAG) model for question answering, built with FastAPI, PostgreSQL/pgvector, and Celery.

## Features
- **FastAPI** backend for fast and concise API endpoints.
- **RAG Architecture** for intelligent document-based Q&A.
- **Celery** for asynchronous file processing and data indexing.
- **PostgreSQL & pgvector** for persistent storage and vector search.
- **Docker Compose** setups for quick deployment of supporting services.

## Requirements
- Python 3.10

#### Install System Dependencies

```bash
sudo apt update
sudo apt install libpq-dev gcc python3-dev
```

#### Install Python using MiniConda

1) Download and install MiniConda from [here](https://docs.anaconda.com/free/miniconda/#quick-command-line-install)
2) Create a new environment:
```bash
conda create -n mini-rag python=3.10
```
3) Activate the environment:
```bash
conda activate mini-rag
```

## Installation

### Install the required packages

```bash
pip install -r requirements.txt
```

### Setup the environment variables

```bash
cp .env.example .env
```
Ensure you set your environment variables in the `.env` file, particularly the `OPENAI_API_KEY`.

### Run Alembic Migrations

```bash
alembic upgrade head
```

## Run Docker Compose Services

We use Docker Compose to spin up necessary dependent services like database and message brokers.

```bash
cd docker
cp .env.example .env
```
*Update `.env` with your credentials*

```bash
sudo docker compose up -d
```

## Access Services

- **FastAPI**: http://localhost:8000
- **Flower Dashboard**: http://localhost:5555 (Credentials inside your env)
- **Grafana**: http://localhost:3000
- **Prometheus**: http://localhost:9090

## Run the FastAPI server (Development Mode)

```bash
uvicorn main:app --reload --host 0.0.0.0 --port 5000
```

## Celery (Development Mode)

For development, you can run Celery services manually instead of using Docker:

### 1. Celery Worker (Separate Terminal)

```bash
python -m celery -A celery_app worker --queues=default,file_processing,data_indexing --loglevel=info
```

### 2. Beat Scheduler (Separate Terminal)

```bash
python -m celery -A celery_app beat --loglevel=info
```

### 3. Flower Dashboard (Separate Terminal)

```bash
python -m celery -A celery_app flower --conf=flowerconfig.py
```
Open your browser and navigate to `http://localhost:5555` to view the dashboard.

## API Testing
A POSTMAN collection is provided for testing API endpoints.
Download it from: `/assets/mini-rag-app.postman_collection.json`
