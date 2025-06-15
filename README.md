# Life-In-Weeks Timeline Application

## Introduction

Life-In-Weeks is a powerful visualization tool that transforms your life journey into an intuitive week-by-week timeline. Inspired by the concept that life is made up of weeks, this application helps you:

- Visualize your life in a grid of weekly blocks
- Track important personal milestones and events
- See global historical events in the context of your life
- Gain perspective on how you spend your most precious resource - time

## Features ✨

### 📅 Life Timeline Visualization
- Interactive grid where each square represents one week of your life
- Color-coded blocks for lived weeks, future weeks, and weeks with events
- Modal details for weeks containing personal or global events

### 🎯 Personal Event Management
- Add, edit, and delete personal life events
- Categorize events (career, family, health, etc.)
- See your events displayed in the timeline context

### 🌍 Global Event Integration
- View historical world events alongside your personal timeline
- Understand how global events correlate with your life journey
- CSV-based global event database for easy updates

### 👤 User Profile System
- Secure registration and login with email authentication
- Profile management with name, birthdate, and profile picture
- Password encryption for security

## Technology Stack 💻

### Backend
- Python 3.10+
- Flask web framework
- SQLAlchemy ORM
- Flask-Login for authentication
- Flask-Bcrypt for password hashing

### Frontend
- Bootstrap 5 for responsive design
- Bootstrap Icons for beautiful UI elements
- Jinja2 templating engine
- Custom CSS for timeline visualization

### Database
- SQLite (default) or PostgreSQL
- Relational database schema for users and events

## Installation Guide 🛠️

### Prerequisites
- Python 3.10+
- pip package manager
- Virtual environment (recommended)

### Setup Steps

1. **Clone the repository**
```bash
git clone https://github.com/servani93/WeeklyLife.git
cd WeeklyLife

##  Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # Linux/MacOS
venv\Scripts\activate    # Windows

##  Install dependencies
pip install -r requirements.txt

##  Set up environment variables
FLASK_APP=app
FLASK_ENV=development
SECRET_KEY=your_secret_key_here

## Initialize database
flask db init
flask db migrate
flask db upgrade

## run app
flask run
```
## Usage Guide 📖

- Register an account with your email and birthdate

- Set up your profile with additional details

- Add personal events to mark important milestones

- Explore your timeline to see your life visualized week-by-week

- View global events that occurred during your lifetime

 ## Project Structure 📂
 ```
life-in-weeks/
├── app/
│   ├── __init__.py
│   ├── routes.py
│   ├── models.py
│   ├── forms.py
│   ├── templates/
│   │   ├── base.html
│   │   ├── dashboard.html
│   │   ├── login.html
│   │   ├── register.html
│   │   ├── profile.html
│   │   ├── add_event.html
│   │   └── edit_event.html
│   └── static/
│       └── style.css
├── config.py
├── requirements.txt
├── global_events.csv
└── README.md 
```
## Future Enhancements 🚀
- Mobile app version

- Data export functionality

- Timeline sharing options

- Advanced analytics and insights

- Integration with calendar services
