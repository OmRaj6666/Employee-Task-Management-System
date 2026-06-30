from models import db

class Report(db.Model):

    __tablename__ = "report"

    report_id = db.Column(db.Integer, primary_key=True)

    report_name = db.Column(db.String(100))

    created_at = db.Column(db.DateTime)

    created_by = db.Column(db.Integer)

    file_name = db.Column(db.String(200))