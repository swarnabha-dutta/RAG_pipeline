# 📚 Production Grade RAG (Retrieval-Augmented Generation)

A production-ready **Retrieval-Augmented Generation (RAG)** system built with **FastAPI, Qdrant, OpenRouter, and Sentence Transformers**. This project follows a scalable, production-grade architecture with clean code principles, modular design, centralized configuration, logging, exception handling, and containerized deployment.

---

# 🚀 Tech Stack

- Python 3.14
- FastAPI
- Uvicorn
- Pydantic v2
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
│   ├── ingestion/
│   │
│   ├── models/
│   │   ├── response.py
│   │   └── query.py
│   │
│   ├── services/
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

---

# 🚧 In Progress

- OpenRouter Client
- Embedding Service
- Qdrant Client
- Dependency Injection

---

# 📌 Upcoming Features

- PDF Parsing
- Intelligent Text Chunking
- Embedding Generation
- Vector Storage (Qdrant)
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
|---------|--------|
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
| OpenRouter Client | 🔄 In Progress |
| Embedding Service | ⏳ Pending |
| Qdrant Client | ⏳ Pending |
| PDF Processing | ⏳ Pending |
| Chunking | ⏳ Pending |
| Embedding Generation | ⏳ Pending |
| Vector Store | ⏳ Pending |
| Semantic Retrieval | ⏳ Pending |
| RAG Pipeline | ⏳ Pending |
| Docker | ⏳ Pending |
| Testing | ⏳ Pending |
| CI/CD | ⏳ Pending |

---

# 🎯 Current Progress

## Overall Progress

**50% Completed**

### ✅ Foundation Layer

- FastAPI
- Configuration
- Logger
- Lifespan
- API Models
- Exception Architecture
- Swagger
- Postman Testing

### 🚀 Current Milestone

Building the core RAG infrastructure:

- OpenRouter Client
- Embedding Service
- Qdrant Client
- Dependency Injection

### 📍 Next Milestone

- PDF Parsing
- Intelligent Chunking
- Embedding Generation
- Vector Storage
- Semantic Search
- Complete Production RAG Pipeline

---

# 👨‍💻 Author

**Swarnabha Dutta**

- GitHub: https://github.com/swarnabha-dutta
- LinkedIn: https://www.linkedin.com/in/swarnabhadutta909/
