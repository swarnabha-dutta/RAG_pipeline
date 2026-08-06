# 📚 Production Grade RAG (Retrieval-Augmented Generation)

A production-ready **Retrieval-Augmented Generation (RAG)** system built with **FastAPI, Qdrant, OpenRouter, and Sentence Transformers**. This project follows a scalable, production-grade architecture with clean code principles, modular design, logging, exception handling, and containerized deployment.

---

# 🚀 Tech Stack

- Python 3.14
- FastAPI
- Uvicorn
- Pydantic
- Qdrant Vector Database
- Sentence Transformers
- OpenRouter API
- PyMuPDF / PyPDF
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
│   ├── models/
│   │   └── response.py
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
- [x] Environment Configuration (.env)
- [x] Configuration Management
- [x] Production Logger
- [x] FastAPI Lifespan Events
- [x] Root Endpoint
- [x] Health Check Endpoint
- [x] Standard API Response Model
- [x] Custom Exception Classes
- [x] Global Exception Handler (V1)
- [x] Swagger API Documentation
- [x] Postman API Testing

---

# 🚧 In Progress

- HTTP Exception Handler
- Generic Exception Handler
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
- Retrieval-Augmented Generation (RAG) Pipeline
- Prompt Engineering
- Source Citation Support
- Streaming Responses
- REST API Endpoints
- Docker Compose
- Unit Testing
- Integration Testing
- CI/CD Pipeline

---

# 🛠 Installation

## Clone the Repository

```bash
git clone <repository-url>
cd RAG
```

## Create Virtual Environment

```bash
python -m venv .venv
```

## Activate Virtual Environment

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

## Run the Application

```bash
python run.py
```

---

# 📖 API Documentation

## Swagger UI

```text
http://localhost:8000/docs
```

## Root Endpoint

```http
GET /
```

### Response

```json
{
    "success": true,
    "message": "Production RAG API Running 🚀",
    "data": {
        "version": "1.0.0"
    }
}
```

---

## Health Check

```http
GET /health
```

### Response

```json
{
    "success": true,
    "message": "Application Healthy",
    "data": {
        "status": "healthy"
    }
}
```

---

# 📈 Development Progress

| Module | Status |
|---------|--------|
| Project Setup | ✅ Completed |
| FastAPI | ✅ Completed |
| Configuration | ✅ Completed |
| Logging | ✅ Completed |
| Lifespan Events | ✅ Completed |
| API Response Model | ✅ Completed |
| Custom Exceptions | ✅ Completed |
| Global Exception Handler (V1) | ✅ Completed |
| HTTP Exception Handler | 🔄 In Progress |
| Generic Exception Handler | ⏳ Pending |
| OpenRouter Integration | ⏳ Pending |
| Embedding Service | ⏳ Pending |
| Qdrant Integration | ⏳ Pending |
| PDF Processing | ⏳ Pending |
| Chunking Strategy | ⏳ Pending |
| Vector Store | ⏳ Pending |
| Semantic Retrieval | ⏳ Pending |
| RAG Pipeline | ⏳ Pending |
| Docker | ⏳ Pending |
| Testing | ⏳ Pending |
| CI/CD | ⏳ Pending |

---

# 🎯 Current Progress

## Overall Progress

**40% Completed**

### ✔️ Foundation Completed

- FastAPI Application
- Environment Configuration
- Production Logger
- Lifespan Events
- Standard API Response Model
- Custom Exceptions
- Global Exception Handler (V1)
- Swagger Documentation
- Postman Testing

### 🚀 Next Milestone

Complete the production exception handling layer by implementing:

- HTTP Exception Handler
- Generic Exception Handler

Then continue with:

- OpenRouter Client
- Embedding Service
- Qdrant Client
- PDF Ingestion
- Chunking
- Embedding Generation
- Semantic Retrieval
- Complete Production RAG Pipeline

---

# 👨‍💻 Author

**Swarnabha Dutta**

- GitHub: https://github.com/swarnabha-dutta
- LinkedIn: [https://linkedin.com/in/swarnabhadutta909/](https://www.linkedin.com/in/swarnabhadutta909/)
