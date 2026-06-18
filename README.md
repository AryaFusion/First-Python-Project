# 🎬 SCREENPULSE - OTT Trend Tracker

SCREENPULSE is a modern OTT discovery platform built using FastAPI and TVMaze API. It allows users to explore trending TV shows, search for their favorite series, filter content by genre, and view detailed information about each show through an interactive and premium user interface.

---

## 🚀 Features

### 🔥 Trending Shows
- Displays a curated list of popular and trending TV series.
- Includes shows such as:
  - Money Heist
  - Dark
  - Stranger Things
  - Breaking Bad
  - Peaky Blinders
  - The Boys
  - Game of Thrones
  - And more.

### 🔍 Smart Search
- Search for TV shows in real time.
- Fetches results using the TVMaze Search API.
- Supports partial show names.

### 🎭 Genre Filters
- Dynamically generates genre filters based on available shows.
- Instantly filter content without reloading the page.

### 📖 Detailed Show Information
View complete details about any show:
- Show Name
- Rating
- Genres
- Language
- Status
- Premiere Date
- Official Summary/Description

### 🌗 Theme Toggle
- Dark Theme
- Light Theme
- Smooth UI transitions

### 🎨 Premium User Interface
- Inspired by modern OTT platforms.
- Responsive layout.
- Interactive hover effects.
- Smooth animations and transitions.

---

## 🏗️ Project Architecture

```text
User
 │
 ▼
Frontend (HTML + CSS + JavaScript)
 │
 ▼
FastAPI Backend
 │
 ▼
TVMaze API
 │
 ▼
Show Data & Search Results
```

---

## 🛠️ Technology Stack

### Backend
- Python
- FastAPI
- Requests

### Frontend
- HTML5
- CSS3
- JavaScript

### Database
- SQLite3

### External API
- TVMaze API

---

## 📂 Project Structure

```text
First-Python-Project/
│
├── app.py
├── database.py
├── tvmaze_service.py
├── shows.db
│
├── templates/
│   └── index.html
│
├── static/
│   └── style.css
│
└── README.md
```

---

## ⚙️ Installation

### Clone Repository

```bash
git clone <repository-url>
cd First-Python-Project
```

### Install Dependencies

```bash
pip install fastapi uvicorn requests jinja2
```

### Run Application

```bash
python -m uvicorn app:app --reload
```

### Open Browser

```text
http://127.0.0.1:8000
```

---

## 📸 Key Functionalities

### Home Page
- Featured Hero Banner
- Trending Shows Section
- Responsive Navigation

### Search
- Search by show name
- Dynamic result loading

### Filters
- Genre-based filtering
- Interactive chips/buttons

### Show Details
- View detailed information
- Modal popup interface

---

## 🔮 Future Scope

- User Authentication
- Personalized Recommendations
- Watchlist Management
- Favorite Shows
- OTT Platform Detection (Netflix, Prime, Disney+, etc.)
- AI-Based Recommendations
- Recently Viewed Shows
- Trending Analytics Dashboard

---

## 👨‍💻 Team Members

### Arya Maner
- Backend Development
- API Integration
- Final Project Integration

### Aaditi Mayekar
- Frontend Design
- User Interface Development
- Testing & Validation

### Shaurya Maner
- Database Design
- SQLite Integration
- Search History Module

---

## 🎯 Project Objective

The objective of SCREENPULSE is to provide users with a simple and visually appealing platform for discovering trending OTT content, searching shows, and exploring detailed information through a fast and interactive interface.

---

## 📜 License

This project was developed for educational and academic purposes as part of a Python Capstone Project.

---

### SCREENPULSE
**Discover • Track • Stream**