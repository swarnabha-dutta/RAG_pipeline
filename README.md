# 📚 Production Grade RAG (Retrieval-Augmented Generation)

A production-ready **Retrieval-Augmented Generation (RAG)** system built with **FastAPI, Qdrant, OpenRouter, and Sentence Transformers**. This project follows a scalable, production-grade architecture with clean code principles, modular design, centralized configuration, logging, exception handling, and containerized deployment.

---

# 🚀 Tech Stack

- Python 3.14
- FastAPI
- Uvicorn
- Pydantic v2
- HTTPX
- Qdrant Vector Database
- Sentence Transformers
- OpenRouter API
- PyMuPDF
- Docker
- Python Dotenv

---

# 📂 Project Structure

```text
RAG/
│
├── app/
│   ├── api/
│   │   └── main.py
│   │
│   ├── config/
│   │   ├── settings.py
│   │   └── test_settings.py
│   │
│   ├── core/
│   │   ├── logger.py
│   │   ├── exceptions.py
│   │   └── handlers.py
│   │
│   ├── database/
│   │   └── qdrant_client.py
│   │
│   ├── ingestion/
│   │
│   ├── models/
│   │   ├── response.py
│   │   └── query.py
│   │
│   ├── services/
│   │   ├── embedding_service.py
│   │   └── openrouter_client.py
│   │
│   └── utils/
│
├── data/
│   ├── pdfs/
│   └── processed/
│
├── tests/
│
├── .env
├── .gitignore
├── README.md
├── requirements.txt
└── run.py
```

---

# ✅ Completed

- [x] Python Environment Setup
- [x] Virtual Environment
- [x] FastAPI Project Initialization
- [x] Project Folder Structure
- [x] Environment Configuration
- [x] Configuration Management
- [x] Production Logger
- [x] FastAPI Lifespan Events
- [x] Root Endpoint
- [x] Health Check Endpoint
- [x] Standard API Response Model
- [x] Query Request Model
- [x] Custom Exception Classes
- [x] Custom RAG Exception Handler
- [x] HTTP Exception Handler
- [x] Request Validation Exception Handler
- [x] Generic Exception Handler
- [x] Swagger Documentation
- [x] Postman API Testing
- [x] OpenRouter Client
- [x] Embedding Service
- [x] Production Qdrant Client
- [x] Dockerized Qdrant Setup
- [x] Qdrant Health Check
- [x] Collection Existence Check
- [x] Collection Creation

---

# 🚧 In Progress

- PDF Parser
- Dependency Injection

---

# 📌 Upcoming Features

- Intelligent Text Chunking
- Embedding Generation
- Vector Storage (Qdrant)
- Vector Upsert
- Semantic Retrieval
- Retrieval-Augmented Generation Pipeline
- Prompt Engineering
- Source Citation
- Streaming Responses
- REST API
- Docker Compose
- Unit Testing
- Integration Testing
- CI/CD Pipeline

---

# 🛠 Installation

## Clone Repository

```bash
git clone <repository-url>
cd RAG
```

## Create Virtual Environment

```bash
python -m venv .venv
```

## Activate Environment

### Windows

```bash
.venv\Scripts\activate
```

### Linux / macOS

```bash
source .venv/bin/activate
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Run Server

```bash
python run.py
```

---

# 🐳 Run Qdrant (Docker)

```bash
docker run -d --name qdrant -p 6333:6333 -v qdrant_storage:/qdrant/storage qdrant/qdrant
```

Open Dashboard:

```text
http://localhost:6333/dashboard
```

---

# 📖 API Documentation

Swagger UI

```text
http://localhost:8000/docs
```

---

# 📡 Available Endpoints

| Method | Endpoint | Description |
| ------- | -------- | ----------- |
| GET | / | Root Endpoint |
| GET | /health | Health Check |

---

# 📈 Development Progress

| Module | Status |
| ---------------------------- | -------------- |
| Project Setup | ✅ Completed |
| Configuration | ✅ Completed |
| Production Logger | ✅ Completed |
| Lifespan Events | ✅ Completed |
| API Response Model | ✅ Completed |
| Query Request Model | ✅ Completed |
| Custom Exceptions | ✅ Completed |
| HTTP Exception Handler | ✅ Completed |
| Validation Exception Handler | ✅ Completed |
| Generic Exception Handler | ✅ Completed |
| OpenRouter Client | ✅ Completed |
| Embedding Service | ✅ Completed |
| Production Qdrant Client | ✅ Completed |
| Dockerized Qdrant Setup | ✅ Completed |
| PDF Parser | 🔄 In Progress |
| Dependency Injection | 🔄 In Progress |
| Intelligent Chunking | ⏳ Pending |
| Embedding Generation | ⏳ Pending |
| Vector Storage | ⏳ Pending |
| Vector Upsert | ⏳ Pending |
| Semantic Retrieval | ⏳ Pending |
| RAG Pipeline | ⏳ Pending |
| Prompt Engineering | ⏳ Pending |
| Source Citation | ⏳ Pending |
| Streaming Responses | ⏳ Pending |
| Docker Compose | ⏳ Pending |
| Unit Testing | ⏳ Pending |
| Integration Testing | ⏳ Pending |
| CI/CD Pipeline | ⏳ Pending |

---

# 🎯 Current Progress

## Overall Progress

**68% Completed**

### ✅ Foundation Layer

- FastAPI
- Configuration Management
- Production Logger
- Lifespan Events
- API Models
- Exception Handling
- Swagger Documentation
- Postman Testing

### ✅ AI Infrastructure

- OpenRouter Client
- Embedding Service

### ✅ Vector Database Layer

- Production Qdrant Client
- Dockerized Qdrant
- Health Check
- Collection Creation
- Collection Verification

### 🚀 Current Milestone

Building the Document Processing Layer

- PDF Parser
- Dependency Injection

### 📍 Next Milestone

- Intelligent Text Chunking
- Embedding Generation
- Vector Upsert
- Semantic Retrieval
- Source Citation
- Complete Production RAG Pipeline

---

# 🛣 Roadmap

```text
✅ FastAPI Foundation
        │
✅ Configuration
        │
✅ Logger
        │
✅ Exception Handling
        │
✅ OpenRouter Client
        │
✅ Embedding Service
        │
✅ Production Qdrant Client
        │
🔄 PDF Parser
        │
⬜ Intelligent Chunking
        │
⬜ Embedding Generation
        │
⬜ Vector Upsert
        │
⬜ Semantic Retrieval
        │
⬜ RAG Pipeline
        │
⬜ Source Citation
        │
⬜ Streaming API
        │
⬜ Testing
        │
⬜ CI/CD
```

---

# 👨‍💻 Author

**Swarnabha Dutta**

- GitHub: https://github.com/swarnabha-dutta
- LinkedIn: https://www.linkedin.com/in/swarnabhadutta909/
