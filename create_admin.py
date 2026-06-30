from app import app
from models import db, bcrypt
from models.employee import Employee

with app.app_context():

    username = "admin"

    existing = Employee.query.filter_by(username=username).first()

    if existing:
        print("Admin already exists.")

    else:
        password = bcrypt.generate_password_hash("Admin@123").decode("utf-8")

        admin = Employee(
            company_id=1,
            full_name="System Administrator",
            email="admin@mponline.com",
            phone="9876543210",
            username="admin",
            password=password,
            role="Manager"
        )

        db.session.add(admin)
        db.session.commit()

        print("Admin created successfully.")