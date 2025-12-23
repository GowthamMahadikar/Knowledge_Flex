# 📌 Python Testing Project (Flask + MongoDB + Pytest)

This project demonstrates **end-to-end backend testing** using **Flask**, **MongoDB**, and **pytest**, covering:

- Python Virtual Environment edge cases  
- REST API behavior & status codes  
- MongoDB edge cases and error handling  

---

## 📂 Project Structure

```
project_root/
│
├── app/
│   ├── routes/
│   ├── models/
│   └── validators/
│
├── tests/
│   ├── test_venv_edge_cases.py
│   ├── test_api_endpoints.py
│   └── test_mongo_edge_cases.py
├── Day Task Theory/
│   ├── Day 1 Task
│   ├── Day 2 Task
│   ├── Day 3 Task
│   ├── Day 4 TasK
│   ├── Day 5 TasK
├── run.py
├── requirements.txt
└── README.md
```

---

## ⚙️ Prerequisites

- Python 3.8+
- MongoDB running locally
- pip installed

---

## 🚀 Setup Instructions

### 1️⃣ Create & Activate Virtual Environment

**Windows**
```
python -m venv venv
venv\Scripts\activate
```

**Linux / macOS**
```
python3 -m venv venv
source venv/bin/activate
```

---

### 2️⃣ Install Dependencies

```
pip install -r requirements.txt
```

---

### 3️⃣ Start MongoDB

**Windows**
```
mongod
```

**Linux**
```
sudo systemctl start mongod
```

Verify:
```
mongosh
```

---

### 4️⃣ Run Flask Application

```
python run.py
```

App runs on:
```
http://127.0.0.1:5000/
```

---

## 🧪 Running Tests

Run all tests:
```
pytest -v
```

Run individual tests:
```
pytest tests/test_api_endpoints.py -v
pytest tests/test_mongo_edge_cases.py -v
pytest tests/test_venv_edge_cases.py -v
```

---

## 📦 requirements.txt

```
flask
pytest
requests
pymongo
dnspython
python-dotenv
```

---

## ❗ Common Issues

- **ModuleNotFoundError** → install requirements  
- **MongoDB error** → ensure MongoDB is running  
- **405 Method Not Allowed** → wrong HTTP method  
- **pytest not found** → pip install pytest  

---

## ✅ Summary

✔ Covers system, API, and DB testing  
✔ Industry-ready pytest structure  
✔ Suitable for interviews & assignments  
