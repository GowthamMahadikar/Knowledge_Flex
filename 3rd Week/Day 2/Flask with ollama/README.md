# Flask + Ollama (Local LLM API)

This project demonstrates how to integrate Flask with Ollama to build a local REST API for running Large Language Models (LLMs) such as Mistral, LLaMA, Gemma, etc., without using any external API keys.

## Features
- Local LLM inference (No API key required)
- Flask-based REST API
- Postman / cURL support
- Proper error handling (404, 415)
- Easy to extend

## Project Structure
```
flask_ollama_app/
│
├── app.py
├── ollama_client.py
├── requirements.txt
└── README.md
```

## Prerequisites
- Python 3.8+
- Flask
- Requests
- Ollama installed locally

## Install Ollama
Download from:
https://ollama.com

Verify:
```
ollama --version
```

## Pull a Model
```
ollama pull mistral
```

## Install Dependencies
```
pip install -r requirements.txt
```

## Run the Application

### Start Ollama
```
ollama run mistral
```

### Start Flask
```
python app.py
```

Server will run at:
```
http://127.0.0.1:5000
```

## API Endpoints

### Health Check
```
GET /
```

### Chat
```
POST /chat
```

Headers:
```
Content-Type: application/json
```

Body:
```json
{
  "prompt": "Explain NLP tokenization"
}
```

## Common Errors

### 404 Not Found
- Wrong URL or method

### 415 Unsupported Media Type
- Missing Content-Type header

## Author
Gowtham Mahadikar
