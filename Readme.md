# 🔗 URL Shortener

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

- Redis caching for faster redirects
- Click tracking and analytics
- Background processing using message queues
- URL expiration support
- Rate limiting per IP/user

---

## 🏗️ System Design (Basic)

Client Request
↓
Django Server
↓
PostgreSQL Database
↓
Redirect to Original URL

### Future Scalable Flow

Client → Django → Redis (Cache Check)
↓ miss
PostgreSQL
↓
Background Queue (Analytics / Logs)

---

## 📦 Project Status

This project is currently in the **early development stage** as part of a **technical skill evaluation for interviews**.  
The focus is on implementing core functionality first, followed by performance optimization and scalability improvements.

---

## 🧠 Learning Outcomes

This project demonstrates understanding of:

- Backend development using Django
- REST API design principles
- Database modeling with PostgreSQL
- Caching strategies using Redis
- Introduction to message queues and async processing
- Basic system design concepts

---

## 🚧 Future Scope

- Custom short URLs (user-defined aliases)
- User authentication system
- Analytics dashboard
- Rate limiting per user/IP
- Docker-based deployment

---

## 📌 Note

This is a learning-focused project created for interview preparation.  
The architecture is intentionally simple and will evolve as features are added.
This is build with AI wording on top of my documentations idea.
