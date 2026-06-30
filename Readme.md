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

![Dashboard]<img width="1470" height="956" alt="Screenshot 2026-06-30 at 7 27 09 PM" src="https://github.com/user-attachments/assets/cf5ba0ae-1049-40ab-a90a-7b39e111e8d0" />


---

## Employee Management

![Employees]<img width="1470" height="956" alt="Screenshot 2026-06-30 at 7 27 20 PM" src="https://github.com/user-attachments/assets/179f6409-7fe4-4549-abe2-e208f9562283" />


---

## Task Management

![Tasks]<img width="1470" height="956" alt="Screenshot 2026-06-30 at 7 27 34 PM" src="https://github.com/user-attachments/assets/6aec3cdc-2049-4974-ae00-5b28bd67ddb0" />


---

## Employee Portal

![Employee]<img width="1470" height="956" alt="Screenshot 2026-06-30 at 7 34 14 PM" src="https://github.com/user-attachments/assets/1790c217-5b39-441b-878c-58c1b952ec35" />
<img width="1470" height="956" alt="Screenshot 2026-06-30 at 7 34 23 PM" src="https://github.com/user-attachments/assets/2d287fe5-fadd-462f-9a53-caec3c04e796" />




---

## Reports

![Reports]<img width="1470" height="956" alt="Screenshot 2026-06-30 at 7 28 13 PM" src="https://github.com/user-attachments/assets/f0f9f9e3-adac-4824-b779-82382ccd20de" />


---

## Audit Logs

![Audit]<img width="1470" height="956" alt="Screenshot 2026-06-30 at 7 28 18 PM" src="https://github.com/user-attachments/assets/a1801af6-6544-42c7-9791-15b61704cc01" />


---

## Settings

![Settings]<img width="1470" height="956" alt="Screenshot 2026-06-30 at 7 28 23 PM" src="https://github.com/user-attachments/assets/b056f174-7c68-4671-ad8d-88ac10faf485" />


---

Demo Link: https://employee-task-management-system-36y8.onrender.com/

# 🎥 Demo Video

Watch the complete project demonstration:




https://github.com/user-attachments/assets/13d87b1c-b0f1-40c3-abd0-1f5b73bc12aa


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



GitHub:
https://github.com/OmRaj6666

LinkedIn:
https://www.linkedin.com/in/om-raj-vit/


---

# ⭐ Support

If you found this project useful,

please ⭐ Star this repository on GitHub.
