# 🎯 Modern Django Todo Application
A clean, responsive, and functional **Task Dashboard** built from scratch using **Python, Django, and Bootstrap 5**. This application allows users to create tasks, toggle their completion status dynamically with instant UI feedback, and delete them from a persistent SQLite database.

## ✨ Features
- **MVT Architecture:** Built using Django's Model-View-Template architecture for clean and organized development.
- **Task Management:** Create, view, update, and delete tasks with ease.
- **Dynamic Task Toggling:** Instantly mark tasks as completed or active with visual feedback.
- **Persistent Storage:** Stores all tasks securely using SQLite.
- **Responsive Interface:** Clean and mobile-friendly UI designed with Bootstrap 5.
- **Interactive Dashboard:** Displays tasks in an organized card-based layout for a better user experience.
- **Empty State Indicator:** Shows a helpful message when no tasks are available.

## 🛠️ Tech Stack
- Python
- Django
- HTML5
- CSS3
- Bootstrap 5
- SQLite

## 🚀 Getting Started & Installation

Follow these steps to set up the project on your local machine.

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/SONAL-THAKUR163/django-task-dashboard.git
cd django-task-dashboard
```

### 2️⃣ Install Django
```bash
pip install django
```

### 3️⃣ Apply Database Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 4️⃣ Run the Development Server
```bash
python manage.py runserver
```

## 📂 Project Structure

```text
todo_project/
│── manage.py
│── db.sqlite3
│
├── todo_project/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
└── tasks/
    ├── migrations/
    ├── templates/
    │   └── tasks/
    │       └── list.html
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── models.py
    ├── urls.py
    ├── views.py
    └── tests.py
```

---

## 👨‍💻 Author
**Sonal Thakur**

- **GitHub:** https://github.com/SONAL-THAKUR163

⭐ If you found this project useful, consider giving it a **Star** on GitHub!
