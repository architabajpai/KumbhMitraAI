# 🕉️ KumbhMitra AI – By Archita

## AI-Powered Multilingual Pilgrim Assistant for Mahakumbh

KumbhMitra AI is an intelligent multilingual assistant designed to help pilgrims visiting Mahakumbh navigate the event safely and efficiently. The platform provides real-time information, emergency assistance, accommodation guidance, event details, and multilingual communication support through an AI-powered conversational interface.

---

## Problem Statement

Pilgrims visiting Mahakumbh come from diverse linguistic, cultural, and geographical backgrounds. First-time visitors often face challenges related to:

* Navigation and route guidance
* Event schedules and announcements
* Accommodation and stay recommendations
* Emergency assistance
* Language barriers
* Access to local services

KumbhMitra AI addresses these challenges through a centralized AI-powered assistant.

---

## Features

### 🌐 Multilingual Support

* English ↔ Hindi language toggle
* AI responses generated in the selected language
* Dynamic UI translation

### 🗺️ Navigation Assistance

* Route guidance
* Location-based recommendations
* Pilgrim support information

### 📅 Event Information

* Mahakumbh event schedules
* Daily activities
* Important announcements

### 🏨 Accommodation Guidance

* Stay recommendations
* Nearby lodging information
* Pilgrim housing assistance

### 🚨 Emergency Support

Quick-access emergency actions:

* Medical Emergency
* Lost Child Assistance
* Help Requests
* Safety Information

### 🤖 AI-Powered Responses

* Powered by Google Gemini
* Context-aware assistance
* Structured responses

### 💾 Conversation Storage

* Chat history stored in MongoDB
* Persistent records for future analysis

---

# Tech Stack

## Frontend

* Next.js 15
* React
* TypeScript
* Tailwind CSS

## Backend

* FastAPI
* Python

## AI

* Google Gemini API

## Database

* MongoDB

---

# Project Architecture

```text
Frontend (Next.js)
       │
       ▼
FastAPI Backend
       │
       ▼
 Gemini API
       │
       ▼
 MongoDB
```

---

# Folder Structure

```text
project-root
│
├── frontend
│   ├── app
│   ├── components
│   ├── context
│   ├── constants
│   ├── services
│   └── public
│
└── backend
    ├── app
    │   ├── routes
    │   ├── services
    │   ├── models
    │   ├── database
    │   └── config.py
    │
    └── main.py
```

---

# Language Toggle System

The application supports bilingual communication.

### English Mode

```json
{
  "message": "What events are happening today?",
  "language": "en"
}
```

### Hindi Mode

```json
{
  "message": "आज के कार्यक्रम क्या हैं?",
  "language": "hi"
}
```

The selected language is sent to the backend and included in the Gemini prompt to ensure responses are generated in the chosen language.

---

# API Endpoint

## Chat Endpoint

### POST `/chat`

Request:

```json
{
  "message": "Where can I stay near Sangam?",
  "language": "en"
}
```

Response:

```json
{
  "answer": "Accommodation information..."
}
```

---

# Environment Variables

## Frontend

`.env.local`

```env
NEXT_PUBLIC_API_URL=http://127.0.0.1:8000
```

## Backend

`.env`

```env
GEMINI_API_KEY=YOUR_GEMINI_API_KEY
MONGODB_URL=YOUR_MONGODB_CONNECTION_STRING
```

---

# Running the Project

## Start Backend

```bash
uvicorn app.main:app --reload
```

Backend runs at:

```text
http://127.0.0.1:8000
```

API Documentation:

```text
http://127.0.0.1:8000/docs
```

---

## Start Frontend

```bash
npm run dev
```

Frontend runs at:

```text
http://localhost:3000
```

---

# Future Enhancements

* Voice-to-Voice interaction
* GPS-based live navigation
* Crowd density monitoring
* Emergency SOS integration
* Offline support
* Additional regional language support
* Pilgrim analytics dashboard

---

# Innovation Highlights

✅ AI-powered multilingual assistance

✅ Real-time conversational support

✅ Emergency-first design

✅ Accessible and user-friendly interface

✅ Scalable architecture for large public events

---

# Developed By

### Archita

AI-Powered Multilingual Pilgrim Assistant – KumbhMitra AI

Built for the Mahakumbh Innovation Challenge.
