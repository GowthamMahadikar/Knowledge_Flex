
# FastAPI + Hugging Face Transformers 🚀

This project demonstrates how to build a REST API using **FastAPI** integrated with **Hugging Face Transformers** for:
- Text Generation
- Text Classification

---

## 📂 Project Structure

```
fastapi-transformers/
│── app.py
│── requirements.txt
│── README.md
```

---

## ⚙️ Requirements

- Python 3.8+
- pip

### Install Dependencies

```bash
pip install -r requirements.txt
```

Example `requirements.txt`:

```txt
fastapi
uvicorn[standard]
transformers
torch
pydantic
```

---

## ▶️ Run the Application

```bash
uvicorn app:app --reload
```

Open your browser:
```
http://127.0.0.1:8000/docs
```

Swagger UI will be available automatically.

---

## 🔹 Text Generation API

### Endpoint
```
POST /generate
```

### Request Body
```json
{
  "prompt": "Artificial Intelligence is",
  "max_length": 50
}
```

### Response
```json
{
  "generated_text": "Artificial Intelligence is transforming the world..."
}
```

---

## 🔹 Text Classification API

### Endpoint
```
POST /classify
```

### Request Body
```json
{
  "text": "I love using FastAPI"
}
```

### Response
```json
{
  "label": "POSITIVE",
  "confidence": 0.99
}
```

---

## 🚀 Production Tips

- Load models once at startup
- Use GPU (`device=0`) if available
- Add exception handling
- Dockerize the app for deployment

---

## 📌 Technologies Used

- FastAPI
- Hugging Face Transformers
- PyTorch
- Uvicorn

---
