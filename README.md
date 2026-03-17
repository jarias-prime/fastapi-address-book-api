# CRUD Address Book API

A simple and efficient Address Book API built using Python and FastAPI.
This application allows users to manage addresses with geographic coordinates and find nearby locations using distance-based filtering.

---

## 🚀 Features

* Create, update, and delete addresses
* Store address, latitude and longitude coordinates
* SQLite database integration
* Interactive API documentation (Swagger UI)

---

## 🛠️ Built With

* Python 3
* FastAPI
* SQLite
* SQLAlchemy

---

## 📁 Project Setup (Step-by-Step)

### 1️⃣ Clone or Download the Project

```bash
git clone https://github.com/jarias-prime/fastapi-address-book-api.git
cd fastapi-address-book-api
```

---

### 2️⃣ Create Virtual Environment

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**Mac:**
```bash
python3 -m venv venv
source venv/bin/activate
```

---

### 3️⃣ Install Dependencies

```bash
pip install fastapi uvicorn sqlalchemy
```

---

### 4️⃣ Run the API Server

```bash
uvicorn main:app --reload
```

---

### 5️⃣ Open the API

Go to your browser:

```text
http://127.0.0.1:8000/
```

👉 Swagger UI will load where you can test all endpoints.

---

## 📌 API Usage Guide

### 🔹 Create Address

* Endpoint: `POST /addresses`

Example request:

```json
{
  "name": "Home",
  "latitude": 14.5995,
  "longitude": 120.9842
}
```

---

### 🔹 Get All Addresses

* Endpoint: `GET /addresses`

---

### 🔹 Update Address

* Endpoint: `PUT /addresses/{id}`

---

### 🔹 Delete Address

* Endpoint: `DELETE /addresses/{id}`

---

## 🗄️ Database

* Uses SQLite database (`addresses.db`)
* Automatically created when the app runs
