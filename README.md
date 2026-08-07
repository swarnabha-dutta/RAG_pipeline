# 📚 Production Grade RAG (Retrieval-Augmented Generation)

A production-ready **Retrieval-Augmented Generation (RAG)** system built with **FastAPI, Qdrant, OpenRouter, Sentence Transformers, and PyMuPDF**.

The project follows a scalable, production-grade architecture with clean code principles, modular design, centralized configuration, logging, exception handling, document processing, vector search, and containerized deployment.

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
│   │   ├── exceptions.py
│   │   ├── handlers.py
│   │   └── logger.py
│   │
│   ├── database/
│   │   └── qdrant_client.py
│   │
│   ├── ingestion/
│   │   ├── pdf_parser.py
│   │   └── text_chunker.py
│   │
│   ├── models/
│   │   ├── query.py
│   │   └── response.py
│   │
│   ├── services/
│   │   ├── embedding_service.py
│   │   └── openrouter_client.py
│   │
│   └── utils/
│       └── text_cleaner.py
│
├── data/
│   ├── pdfs/
│   └── processed/
│
├── tests/
│   ├── test_pdf_parser.py
│   ├── test_qdrant.py
│   └── test_text_chunker.py
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
- [x] Production PDF Parser
- [x] Production Text Cleaner
- [x] Intelligent Text Chunker
- [x] Vector Upsert
- [x] Semantic Vector Search
- [x] Vector Count
- [x] Collection Delete

---

# 🚧 In Progress

- Embedding Pipeline
- Dependency Injection

---

# 📌 Upcoming Features

- Embedding Generation Pipeline
- Retrieval Pipeline
- Prompt Engineering
- Retrieval-Augmented Generation (RAG)
- Source Citation
- REST API
- Streaming Responses
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

## Run Application

```bash
python run.py
```

---

# 🐳 Run Qdrant

```bash
docker run -d \
--name qdrant \
-p 6333:6333 \
-v qdrant_storage:/qdrant/storage \
qdrant/qdrant
```

Open Dashboard

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
|---------|----------|-------------|
| GET | / | Root Endpoint |
| GET | /health | Health Check |
---

# 📈 Development Progress

| Module | Status |
|-------------------------------|--------------|
| Project Setup | ✅ Completed |
| Configuration Management | ✅ Completed |
| Production Logger | ✅ Completed |
| FastAPI Lifespan | ✅ Completed |
| API Response Model | ✅ Completed |
| Query Request Model | ✅ Completed |
| Custom Exceptions | ✅ Completed |
| Exception Handlers | ✅ Completed |
| Swagger Documentation | ✅ Completed |
| Postman Testing | ✅ Completed |
| OpenRouter Client | ✅ Completed |
| Embedding Service | ✅ Completed |
| Production Qdrant Client | ✅ Completed |
| Dockerized Qdrant | ✅ Completed |
| Qdrant Health Check | ✅ Completed |
| Collection Management | ✅ Completed |
| Production PDF Parser | ✅ Completed |
| Text Cleaner | ✅ Completed |
| Intelligent Text Chunker | ✅ Completed |
| Vector Upsert | ✅ Completed |
| Semantic Search | ✅ Completed |
| Vector Count | ✅ Completed |
| Collection Delete | ✅ Completed |
| Embedding Pipeline | 🔄 In Progress |
| Dependency Injection | 🔄 In Progress |
| Retrieval Pipeline | ⏳ Pending |
| Prompt Engineering | ⏳ Pending |
| Source Citation | ⏳ Pending |
| Streaming Responses | ⏳ Pending |
| REST API | ⏳ Pending |
| Docker Compose | ⏳ Pending |
| Unit Testing | ⏳ Pending |
| Integration Testing | ⏳ Pending |
| CI/CD Pipeline | ⏳ Pending |

---

# 🎯 Current Progress

## Overall Progress

# **78% Completed**

---

## ✅ Foundation Layer

- FastAPI
- Configuration Management
- Production Logger
- Lifespan Events
- API Models
- Exception Handling
- Swagger Documentation
- Postman Testing

---

## ✅ AI Infrastructure

- OpenRouter Client
- Embedding Service

---

## ✅ Vector Database Layer

- Production Qdrant Client
- Dockerized Qdrant
- Health Check
- Collection Creation
- Collection Verification
- Vector Upsert
- Semantic Search
- Vector Count
- Collection Delete

---

## ✅ Document Processing Layer

- Production PDF Parser
- Text Cleaner
- Intelligent Text Chunker

---

## 🚀 Current Milestone

Building the Embedding & Retrieval Pipeline

- Embedding Generation
- Vector Storage
- Semantic Retrieval

---

## 📍 Next Milestone

- Complete Embedding Pipeline
- Retrieval Pipeline
- Prompt Engineering
- Source Citation
- End-to-End RAG API

---

# 🏗 System Architecture

```text
                        PDF Documents
                              │
                              ▼
                     Production PDF Parser
                              │
                              ▼
                       Text Cleaner
                              │
                              ▼
                  Intelligent Text Chunker
                              │
                              ▼
                  Sentence Transformer
                       Embeddings
                              │
                              ▼
                    Qdrant Vector Database
                              │
                              ▼
                    Semantic Retrieval
                              │
                              ▼
                     Prompt Engineering
                              │
                              ▼
                    OpenRouter LLM
                              │
                              ▼
               Final Answer + Source Citation
```

---

# 🛣 Development Roadmap

```text
✅ FastAPI Foundation
        │
✅ Configuration
        │
✅ Production Logger
        │
✅ Exception Handling
        │
✅ OpenRouter Client
        │
✅ Embedding Service
        │
✅ Production Qdrant Client
        │
✅ PDF Parser
        │
✅ Text Cleaner
        │
✅ Intelligent Text Chunker
        │
🔄 Embedding Pipeline
        │
⬜ Vector Storage
        │
⬜ Semantic Retrieval
        │
⬜ Prompt Engineering
        │
⬜ RAG Pipeline
        │
⬜ Source Citation
        │
⬜ REST API
        │
⬜ Streaming Responses
        │
⬜ Docker Compose
        │
⬜ Unit Testing
        │
⬜ Integration Testing
        │
⬜ CI/CD Pipeline
```

---

# 🎯 Project Goals

- Build a production-ready RAG system from scratch.
- Implement scalable document ingestion.
- Perform semantic search using Qdrant.
- Generate accurate answers using OpenRouter.
- Return document-aware source citations.
- Follow clean architecture and production-grade engineering practices.

---

# 🚀 Upcoming Features

- Multi PDF Support
- Batch Document Ingestion
- Metadata Filtering
- Hybrid Search
- Streaming Responses
- Conversation Memory
- Docker Compose
- GitHub Actions CI/CD
- Unit Testing
- Integration Testing

---

# 👨‍💻 Author

**Swarnabha Dutta**

- GitHub: https://github.com/swarnabha-dutta
- LinkedIn: https://www.linkedin.com/in/swarnabhadutta909/
