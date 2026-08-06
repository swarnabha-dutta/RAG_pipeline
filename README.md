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
│   │   └── settings.py
│   │
│   ├── core/
│   │   ├── logger.py
│   │   └── exceptions.py
│   │
│   ├── database/
│   ├── ingestion/
│   ├── models/
│   ├── services/
│   └── utils/
│
├── data/
│   ├── pdfs/
│   ├── cache/
│   └── embeddings/
│
├── tests/
│
├── run.py
├── .env
├── .gitignore
├── README.md
└── requirements.txt
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
- [x] Health Check Endpoint
- [x] Root Endpoint

---

# 🚧 In Progress

- Global Exception Handler
- Pydantic Request & Response Schemas
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
- RAG Pipeline
- Prompt Engineering
- Citation Support
- Streaming Responses
- REST API Endpoints
- Docker Compose
- Unit Testing
- Integration Testing
- CI/CD Pipeline

---

# 🛠 Installation

Clone the repository

```bash
git clone <repository-url>
cd RAG
```

Create Virtual Environment

```bash
python -m venv .venv
```

Activate Virtual Environment

### Windows

```bash
.venv\Scripts\activate
```

### Linux / macOS

```bash
source .venv/bin/activate
```

Install Dependencies

```bash
pip install -r requirements.txt
```

Run the Application

```bash
python run.py
```

---

# 📖 API Documentation

Swagger UI

```text
http://localhost:8000/docs
```

Health Check

```text
GET /health
```

Root Endpoint

```text
GET /
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
| Exception Handling | 🔄 In Progress |
| OpenRouter Integration | ⏳ Pending |
| Embedding Service | ⏳ Pending |
| Qdrant Integration | ⏳ Pending |
| PDF Processing | ⏳ Pending |
| RAG Pipeline | ⏳ Pending |
| Docker | ⏳ Pending |
| Testing | ⏳ Pending |
| CI/CD | ⏳ Pending |

---

# 🎯 Current Progress

# 📈 Development Progress

**Overall Progress: 25%**

> The project foundation is complete. The next phase focuses on implementing the complete Retrieval-Augmented Generation (RAG) pipeline with vector search and LLM integration.

---

# 👨‍💻 Author

**Swarnabha Dutta**

- GitHub: https://github.com/swarnabha-dutta
- LinkedIn: https://www.linkedin.com/in/swarnabha-dutta-0ab583222/
