# 🧠 MindTrack-AI

An AI-powered mental wellness journaling web application built with **Flask** and **Hugging Face Transformers**. Users can securely maintain a personal journal while receiving AI-generated emotion analysis and summaries for each entry.

---

## ✨ Features

- 🔐 User Authentication (Register/Login/Logout)
- 📝 Personal Journal Entries
- 🤖 AI-Based Emotion Detection
- 📊 Confidence Score for Predicted Emotion
- 📄 AI-Generated Journal Summary
- 📅 Timestamped Journal History
- 🎨 Responsive Bootstrap UI
- 💾 SQLite Database Integration

---

## 🛠️ Tech Stack

### Backend
- Python
- Flask
- Flask-Login
- Flask-SQLAlchemy

### AI
- Hugging Face Transformers
- Model:
  `j-hartmann/emotion-english-distilroberta-base`

### Frontend
- HTML5
- CSS3
- Bootstrap 5
- Jinja2 Templates

### Database
- SQLite

---

## 📂 Project Structure

```
MindTrack-AI/
│
├── app.py
├── requirements.txt
├── README.md
│
├── instance/
│   └── database.db
│
├── models/
│   ├── emotion_model.py
│   ├── journal.py
│   ├── user.py
│   └── __init__.py
│
├── static/
│   ├── css/
│   └── js/
│
├── templates/
│   ├── base.html
│   ├── dashboard.html
│   ├── index.html
│   ├── journal.html
│   ├── login.html
│   └── register.html
│
└── utils/
```

---

## ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/yourusername/MindTrack-AI.git
cd MindTrack-AI
```

Create a virtual environment

```bash
python -m venv .venv
```

Activate the environment

### Windows

```bash
.venv\Scripts\activate
```

### macOS/Linux

```bash
source .venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
python app.py
```

Open your browser and visit

```
http://127.0.0.1:5000
```

---

## 🤖 AI Functionality

When a user submits a journal entry, the application:

1. Analyzes the journal text using a Hugging Face transformer model.
2. Predicts the dominant emotion.
3. Calculates the confidence score.
4. Generates a concise AI summary.
5. Stores the results alongside the journal entry.

---

## 📸 Screens

- Home Page
- User Registration
- Login
- Dashboard
- Journal Writing
- AI Emotion Analysis

---

## 🚀 Future Improvements

- Mood trend visualization
- Sentiment history graphs
- Personalized mental wellness recommendations
- Password reset functionality
- Email verification
- Export journal entries as PDF
- Cloud database support
- Mobile responsive enhancements

---

## 📚 Learning Outcomes

This project demonstrates practical experience with:

- Flask Web Development
- Authentication Systems
- SQLAlchemy ORM
- SQLite Database Management
- RESTful Application Design
- Hugging Face Transformers
- AI Integration into Web Applications
- Bootstrap UI Development

---

## 👨‍💻 Author

**Archit Vaksh**

B.Tech Computer Science (AI & ML)

---

## 📄 License

This project is intended for educational and learning purposes.