# 🚀 Employee Task Management System

![Python](https://img.shields.io/badge/Python-3.13-blue?logo=python)
![Flask](https://img.shields.io/badge/Flask-3.x-black?logo=flask)
![Oracle Database](https://img.shields.io/badge/Oracle-Database-red?logo=oracle)
![Bootstrap](https://img.shields.io/badge/Bootstrap-5-purple?logo=bootstrap)
![License](https://img.shields.io/badge/License-MIT-green)

A modern **Employee Task Management System** built using **Flask**, **Oracle Database**, **Bootstrap 5**, and **SQLAlchemy**.

The application helps organizations efficiently manage employees, assign tasks, monitor progress, generate reports, maintain audit logs, and provide employees with a dedicated self-service portal.

---

# 📌 Features

## Authentication

- Secure Login
- Password Hashing (Flask-Bcrypt)
- Session Management
- Role-Based Access Control

---

## Manager Portal

- Dashboard
- Employee Management
- Task Assignment
- Edit/Delete Tasks
- Reports & Analytics
- Audit Logs
- Notifications
- Settings

---

## Employee Portal

- Personal Dashboard
- View Assigned Tasks
- Update Task Status
- Add Remarks
- Profile Management
- Notifications

---

## Reports

- Employee Statistics
- Task Statistics
- Pending Tasks
- Completed Tasks
- Overdue Tasks
- Monthly Charts

---

## Notifications

- Task Assigned
- Task Updated
- Mark Notification as Read

---

## Security

- Password Encryption
- Login Authentication
- Protected Routes
- Role-Based Authorization

---

# 🛠 Tech Stack

| Technology | Used |
|------------|------|
| Python | Backend |
| Flask | Web Framework |
| SQLAlchemy | ORM |
| Oracle Database | Database |
| HTML5 | Frontend |
| CSS3 | Styling |
| Bootstrap 5 | UI |
| JavaScript | Client Side |
| Chart.js | Dashboard Charts |
| Flask-Login | Authentication |
| Flask-Bcrypt | Password Hashing |

---

# 📂 Project Structure

```
Employee-Task-Management-System/

│── app.py
│── config.py
│── requirements.txt
│── README.md
│── LICENSE
│── .gitignore
│── .env.example

├── models/
│   ├── employee.py
│   ├── task.py
│   ├── audit.py
│   ├── report.py
│   └── notification.py

├── routes/
│   ├── auth.py
│   ├── employee.py
│   ├── employee_portal.py
│   ├── task.py
│   ├── report.py
│   ├── audit.py
│   ├── notification.py
│   └── settings.py

├── templates/

├── static/

├── screenshots/

└── database/
    └── schema.sql
```

---

# 📷 Screenshots

## Login

![Login]<img width="1470" height="956" alt="Screenshot 2026-06-30 at 7 20 28 PM" src="https://github.com/user-attachments/assets/bf6e576b-74f0-44ae-90e8-1c4343e892db" />

---

## Manager Dashboard

![Dashboard](screenshots/dashboard.png)

---

## Employee Management

![Employees](screenshots/employees.png)

---

## Task Management

![Tasks](screenshots/tasks.png)

---

## Employee Portal

![Employee](screenshots/employee_dashboard.png)

---

## Reports

![Reports](screenshots/reports.png)

---

## Audit Logs

![Audit](screenshots/audit_logs.png)

---

## Notifications

![Notifications](screenshots/notifications.png)

---

# 🎥 Demo Video

Watch the complete project demonstration:

**Coming Soon**

or

```
https://youtu.be/your-video-link
```

---

# ⚙ Installation

## Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/Employee-Task-Management-System.git

cd Employee-Task-Management-System
```

---

## Create Virtual Environment

### Windows

```bash
python -m venv venv

venv\Scripts\activate
```

### macOS/Linux

```bash
python3 -m venv venv

source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Configure Environment

Create a `.env` file.

Example:

```
SECRET_KEY=your_secret_key

DB_USER=your_username

DB_PASSWORD=your_password

DB_HOST=localhost

DB_PORT=1521

DB_SERVICE=FREEPDB1
```

---

## Run Application

```bash
python app.py
```

Application will run at

```
http://127.0.0.1:5001
```

---

# 🗄 Database

This project uses

- Oracle Database 23ai
- SQLAlchemy ORM
- OracleDB Python Driver

Database schema is available in

```
database/schema.sql
```

---

# 👨‍💻 Future Enhancements

- Calendar Module
- Email Notifications
- Excel Export
- PDF Reports
- Task Comments
- File Attachments
- Mobile Application
- REST API
- Docker Support
- CI/CD Pipeline

---

# 🧪 Testing

The application has been tested for

- Login
- Employee CRUD
- Task CRUD
- Notifications
- Reports
- Audit Logs
- Employee Portal
- Settings

---

# 🤝 Contributing

Contributions are welcome.

1. Fork the repository

2. Create a new branch

```
git checkout -b feature-name
```

3. Commit changes

```
git commit -m "Added new feature"
```

4. Push

```
git push origin feature-name
```

5. Open a Pull Request

---

---

# 👤 Author

**Om Raj**

B.Tech Computer Science & Engineering (CSE)

VIT Bhopal University

GitHub:
https://github.com/OmRaj6666

LinkedIn:
https://linkedin.com/in/omraj6666


---

# ⭐ Support

If you found this project useful,

please ⭐ Star this repository on GitHub.
