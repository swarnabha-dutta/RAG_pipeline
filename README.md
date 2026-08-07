# 📚 Production Grade RAG (Retrieval-Augmented Generation)

A production-ready **Retrieval-Augmented Generation (RAG)** system built with **FastAPI, Qdrant, OpenRouter, Sentence Transformers, and PyMuPDF**.

This project implements a complete end-to-end RAG pipeline capable of parsing PDF documents, generating embeddings, storing vectors in Qdrant, retrieving semantically relevant document chunks, and generating citation-aware answers using an OpenRouter LLM.

The project follows production-grade software engineering principles including clean architecture, modular design, centralized configuration, structured logging, exception handling, scalable services, and RESTful APIs.

---

# 🚀 Tech Stack

### Backend

- Python 3.14
- FastAPI
- Uvicorn
- Pydantic v2
- HTTPX

### AI / RAG

- Sentence Transformers
- BAAI/bge-small-en-v1.5
- OpenRouter API
- Google Gemma 3 12B (Free)

### Vector Database

- Qdrant
- Cosine Similarity Search

### Document Processing

- PyMuPDF (fitz)

### DevOps

- Docker
- Python Dotenv

---

# ✨ Features

- ✅ Production-grade FastAPI architecture
- ✅ PDF document ingestion
- ✅ Automatic text cleaning
- ✅ Intelligent text chunking
- ✅ Embedding generation
- ✅ Vector storage using Qdrant
- ✅ Semantic vector search
- ✅ Prompt engineering
- ✅ End-to-End Retrieval-Augmented Generation (RAG)
- ✅ Citation-aware responses
- ✅ REST APIs
- ✅ Swagger Documentation
- ✅ Structured Logging
- ✅ Production Exception Handling

---

# 📂 Project Structure

```text
RAG/
│
├── app/
│   │
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
│   │   ├── response.py
│   │   ├── ingestion.py
│   │   ├── ingestion_response.py
│   │   └── rag_response.py
│   │
│   ├── services/
│   │   ├── embedding_service.py
│   │   ├── ingestion_service.py
│   │   ├── openrouter_client.py
│   │   ├── prompt_builder.py
│   │   └── retrieval_service.py
│   │
│   └── utils/
│       └── text_cleaner.py
│
├── data/
│   ├── pdfs/
│   └── processed/
│
├── tests/
│   ├── test_ingestion.py
│   ├── test_prompt_builder.py
│   ├── test_qdrant.py
│   ├── test_retrieval.py
│   ├── test_pdf_parser.py
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

## Foundation

- [x] Python Environment Setup
- [x] Virtual Environment
- [x] FastAPI Project Initialization
- [x] Production Folder Structure
- [x] Environment Configuration
- [x] Configuration Management
- [x] Production Logger
- [x] Lifespan Events

## API Layer

- [x] Root Endpoint
- [x] Health Endpoint
- [x] POST /ingest
- [x] POST /query
- [x] Standard API Response
- [x] Query Request Model
- [x] Ingestion Request Model
- [x] Swagger Documentation
- [x] Postman Testing

## Exception Handling

- [x] Custom Exceptions
- [x] HTTP Exception Handler
- [x] Validation Exception Handler
- [x] Generic Exception Handler

## AI Layer

- [x] OpenRouter Client
- [x] Embedding Service
- [x] Prompt Builder
- [x] RAG Service

## Vector Database

- [x] Production Qdrant Client
- [x] Dockerized Qdrant
- [x] Health Check
- [x] Collection Creation
- [x] Collection Verification
- [x] Vector Upsert
- [x] Semantic Search
- [x] Vector Count
- [x] Collection Delete

## Document Processing

- [x] Production PDF Parser
- [x] Text Cleaner
- [x] Intelligent Text Chunker
- [x] Ingestion Service
- [x] Retrieval Service
- [x] End-to-End RAG Pipeline

---

# 🚧 In Progress

- Singleton Embedding Model
- Dependency Injection
- Citation Optimization
- Duplicate Document Detection

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

## Configure Environment

Create a `.env` file.

```env
OPENROUTER_API_KEY=your_api_key

OPENROUTER_BASE_URL=https://openrouter.ai/api/v1

OPENROUTER_MODEL=google/gemma-3-12b-it:free

QDRANT_URL=http://localhost:6333
QDRANT_API_KEY=

COLLECTION_NAME=rag_documents

EMBEDDING_MODEL=BAAI/bge-small-en-v1.5
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


# 📡 Available Endpoints

| Method | Endpoint | Description |
| :----: | -------- | ----------- |
| GET | `/` | Root Endpoint |
| GET | `/health` | Application Health Check |
| POST | `/ingest` | Ingest a PDF into the Vector Database |
| POST | `/query` | Ask Questions using the RAG Pipeline |

---

# 🧪 API Examples

## 1. Ingest Document

**POST**

```text
POST /ingest
```

Request

```json
{
    "pdf_path": "data/pdfs/AI Python Engineering Assignment.pdf"
}
```

Response

```json
{
    "success": true,
    "message": "Document ingested successfully.",
    "data": {
        "document": "AI Python Engineering Assignment.pdf",
        "pages": 5,
        "chunks": 12,
        "vectors": 12
    }
}
```

---

## 2. Ask Question

**POST**

```text
POST /query
```

Request

```json
{
    "question": "What is the objective of this assignment?"
}
```

Response

```json
{
    "success": true,
    "message": "Answer generated successfully.",
    "data": {
        "answer": "The objective of this assignment is to build a simple Retrieval-Augmented Generation (RAG) application that can answer questions from a set of PDF documents.",
        "citations": [
            {
                "document": "AI Python Engineering Assignment.pdf",
                "page": 1,
                "text": "Build a simple Retrieval-Augmented Generation (RAG) application..."
            }
        ]
    }
}
```

---

# 📈 Development Progress

| Module | Status |
| ------------------------------- | :---------: |
| FastAPI Foundation | ✅ Completed |
| Configuration Management | ✅ Completed |
| Production Logger | ✅ Completed |
| Lifespan Events | ✅ Completed |
| API Models | ✅ Completed |
| Exception Handling | ✅ Completed |
| Swagger Documentation | ✅ Completed |
| Postman Testing | ✅ Completed |
| OpenRouter Client | ✅ Completed |
| Embedding Service | ✅ Completed |
| Production Qdrant Client | ✅ Completed |
| Dockerized Qdrant | ✅ Completed |
| Collection Management | ✅ Completed |
| Production PDF Parser | ✅ Completed |
| Text Cleaner | ✅ Completed |
| Intelligent Text Chunker | ✅ Completed |
| Ingestion Service | ✅ Completed |
| Vector Upsert | ✅ Completed |
| Semantic Retrieval | ✅ Completed |
| Retrieval Service | ✅ Completed |
| Prompt Builder | ✅ Completed |
| RAG Service | ✅ Completed |
| End-to-End RAG Pipeline | ✅ Completed |
| POST `/ingest` API | ✅ Completed |
| POST `/query` API | ✅ Completed |
| Singleton Embedding Model | 🔄 In Progress |
| Dependency Injection | 🔄 In Progress |
| Metadata Filtering | ⏳ Planned |
| Hybrid Search | ⏳ Planned |
| Streaming Responses | ⏳ Planned |
| Docker Compose | ⏳ Planned |
| Unit Testing | ⏳ Planned |
| Integration Testing | ⏳ Planned |
| GitHub Actions CI/CD | ⏳ Planned |

---

# 🎯 Current Progress

## Overall Progress

# **91% Completed**

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

## ✅ AI Layer

- OpenRouter Client
- Embedding Service
- Prompt Builder
- RAG Service

---

## ✅ Vector Database Layer

- Production Qdrant Client
- Dockerized Qdrant
- Collection Management
- Vector Upsert
- Semantic Retrieval

---

## ✅ Document Processing Layer

- Production PDF Parser
- Text Cleaner
- Intelligent Text Chunker
- Ingestion Service

---

## ✅ Retrieval Layer

- Query Embedding
- Semantic Search
- Top-K Context Retrieval
- Citation Collection

---

## ✅ Generation Layer

- Prompt Engineering
- OpenRouter Integration
- Answer Generation
- Citation-Aware Responses

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
             Sentence Transformer Embeddings
                          │
                          ▼
                Qdrant Vector Database
                          ▲
                          │
                   Semantic Retrieval
                          ▲
                          │
                    User Question
                          │
                          ▼
                  Retrieval Service
                          │
                          ▼
                   Prompt Builder
                          │
                          ▼
                  OpenRouter LLM
                          │
                          ▼
         Answer + Document Citation + Page
```

---

# 🔄 End-to-End Workflow

```text
PDF
 │
 ▼
Parse PDF
 │
 ▼
Clean Text
 │
 ▼
Chunk Text
 │
 ▼
Generate Embeddings
 │
 ▼
Store in Qdrant
 │
 ▼
──────────────────────────────────────
User Question
 │
 ▼
Generate Query Embedding
 │
 ▼
Semantic Search
 │
 ▼
Retrieve Top-K Chunks
 │
 ▼
Build Prompt
 │
 ▼
OpenRouter LLM
 │
 ▼
Final Answer
 │
 ▼
Answer + Citations
```


# 🛣 Development Roadmap

```text
✅ FastAPI Foundation
        │
✅ Configuration Management
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
✅ Ingestion Service
        │
✅ Vector Upsert
        │
✅ Semantic Retrieval
        │
✅ Retrieval Service
        │
✅ Prompt Builder
        │
✅ RAG Service
        │
✅ POST /ingest API
        │
✅ POST /query API
        │
🔄 Singleton Embedding Model
        │
🔄 Dependency Injection
        │
⬜ Metadata Filtering
        │
⬜ Hybrid Search
        │
⬜ Streaming Responses
        │
⬜ Multi-PDF Support
        │
⬜ Batch Document Ingestion
        │
⬜ Docker Compose
        │
⬜ Unit Testing
        │
⬜ Integration Testing
        │
⬜ GitHub Actions CI/CD
```

---

# 🎯 Project Goals

- Build a production-ready Retrieval-Augmented Generation (RAG) system.
- Implement scalable PDF document ingestion.
- Generate high-quality semantic embeddings.
- Store embeddings efficiently in Qdrant.
- Retrieve relevant context using vector similarity search.
- Generate context-aware answers using OpenRouter.
- Return accurate document citations with every response.
- Follow clean architecture and production-grade engineering practices.
- Build a modular and maintainable codebase.
- Prepare the project for production deployment.

---

# 🚀 Upcoming Features

- Singleton Embedding Model
- Dependency Injection
- Duplicate Document Detection
- Metadata Filtering
- Multi-PDF Support
- Batch Document Ingestion
- Hybrid Search (Vector + Keyword)
- Conversation Memory
- Streaming Responses
- Async Background Ingestion
- Docker Compose
- Unit Testing
- Integration Testing
- GitHub Actions CI/CD
- Production Deployment

---

# 📊 Current Project Status

| Category | Progress |
|----------|:--------:|
| Backend Architecture | ✅ 100% |
| Document Processing | ✅ 100% |
| Vector Database | ✅ 100% |
| Retrieval Pipeline | ✅ 100% |
| Generation Pipeline | ✅ 100% |
| REST APIs | ✅ 100% |
| End-to-End RAG Workflow | ✅ 100% |
| Production Optimizations | 🔄 In Progress |

---

# 🏆 Key Highlights

- ✅ Production-grade FastAPI architecture
- ✅ End-to-End Retrieval-Augmented Generation pipeline
- ✅ Intelligent PDF document processing
- ✅ Semantic search powered by Qdrant
- ✅ OpenRouter LLM integration
- ✅ Citation-aware answer generation
- ✅ RESTful API design
- ✅ Modular service-based architecture
- ✅ Structured logging
- ✅ Custom exception handling
- ✅ Swagger API documentation
- ✅ Dockerized vector database
- ✅ Clean and scalable project structure

---

# 📌 Future Optimizations

- Reduce embedding model loading time using Singleton pattern.
- Introduce Dependency Injection across services.
- Improve citation ranking and formatting.
- Prevent duplicate document ingestion.
- Support metadata-based filtering.
- Add Hybrid Search for improved retrieval quality.
- Increase automated test coverage.
- Enable continuous integration and deployment.

---

# 👨‍💻 Author

**Swarnabha Dutta**

**GitHub**

https://github.com/swarnabha-dutta

**LinkedIn**

https://www.linkedin.com/in/swarnabhadutta909/

---

# ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub.

It helps others discover the project and motivates future improvements.

---

# 📄 License

This project is intended for educational, learning, and portfolio purposes.

Feel free to fork, explore, and build upon it.
