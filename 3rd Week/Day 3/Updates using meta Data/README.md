
# 🧠 AI Output Management System (Ollama + Flask + MongoDB)

A simple and powerful **AI output management system** that uses **Ollama (local LLM)** to generate responses, stores them in **MongoDB**, and displays them via **REST APIs** and a **clean table-based UI**.

---

## 🚀 Features

- ✅ Local AI text generation using **Ollama (llama3)**
- ✅ Flask REST API
- ✅ MongoDB for storing prompts & AI responses
- ✅ View outputs as JSON or Table UI
- ✅ Fully offline (No API keys)

---

## 🛠 Tech Stack

- Backend: Flask (Python)
- AI Model: Ollama (`llama3`)
- Database: MongoDB
- Frontend: HTML + CSS (Jinja2)
- HTTP Client: Requests

---

## 📁 Project Structure

```
ai-output-system/
│
├── app.py
├── ollama_model.py
├── requirements.txt
│
├── templates/
│   └── outputs_table.html
│
└── README.md
```

---

## ⚙️ Prerequisites

- Python 3.10+
- MongoDB (running locally)
- Ollama

---

## 🧩 Setup Instructions

### 1️⃣ Install Ollama
https://ollama.com

Verify:
```
ollama --version
```

### 2️⃣ Pull Model
```
ollama pull llama3
```

### 3️⃣ Install Dependencies
```
pip install flask pymongo requests
```

### 4️⃣ Start MongoDB
```
mongodb://localhost:27017/
```

### 5️⃣ Run Application
```
python app.py
```

---

## 🔌 API Endpoints

### POST /generate
```
{
  "prompt": "Explain Artificial Intelligence"
}
```

### GET /outputs
Returns all AI outputs in JSON format.

### GET /outputs-table
Displays outputs in a clean table UI.

---

## 🗄 Sample MongoDB Document

```
{
  "_id": "695b818b62d18692d275c011",
  "prompt": "Explain AI",
  "ai_output": "...",
  "model": "llama3",
  "created_at": "2026-01-05"
}
```

---

## 👨‍💻 Author

Gowtham Mahadikar

---

## 📜 License
For learning and internal use.
