# 🔗 URL Shortener (Chhotkarily)

A simple and scalable URL shortener service built using **Django**, **PostgreSQL**, and **Redis**.  
This project is built as part of a **backend skill assessment for interview preparation**, focusing on system design fundamentals like caching, database design, and background processing.

---

## 🚀 Project Goal

The goal of this project is to build a basic URL shortening service that:

- Converts long URLs into short codes
- Redirects users efficiently
- Demonstrates caching strategies for performance improvement
- Introduces background processing concepts
- Acts as a foundation for scalable backend system design

---

## 🧱 Tech Stack

- **Backend:** Django (Python)
- **Database:** PostgreSQL
- **Cache:** Redis
- **Queue (planned):** Redis Queue
- **Server:** Gunicorn / Django Development Server

---

## ⚙️ Core Features

### ✅ Current

- Generate short URLs from long URLs
- Redirect to original URLs using short codes
- PostgreSQL integration for persistent storage
- Basic Django project structure

### 🧠 Planned Improvements

- Redis caching for faster redirects -Done
- Click tracking and analytics -Done
- Background processing using message queues
- URL expiration support - Done
- Rate limiting per IP/user

---

## 🏗️ System Design (Basic)

Client Request
↓
Django Server
↓
Redis Cache
↓
PostgreSQL Database
↓
Redirect to Original URL

## 📦 Project Status

This project is currently in the **early development stage**.
The focus is on implementing core functionality first, followed by performance optimization and scalability improvements.

---

## 🧠 Learning Outcomes

This project demonstrates understanding of:

- Backend development using Django
- REST API design principles
- Database modeling with PostgreSQL
- Caching strategies using Redis
- Basic system design concepts

---

## 🚧 Future Scope

- Custom short URLs (user-defined aliases)
- User authentication system
- Docker-based deployment

---

## 📌 Note

This is a learning-focused project created for interview preparation.  
The architecture is intentionally simple and will evolve as features are added.
