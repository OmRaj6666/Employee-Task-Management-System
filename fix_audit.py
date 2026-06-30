# fix_tables.py
from app import app
from models import db
from models.audit import AuditLog
from sqlalchemy import inspect, text

def create_tables_properly():
    with app.app_context():
        print("🔍 Checking existing tables...")
        
        # Get current tables
        inspector = inspect(db.engine)
        existing_tables = inspector.get_table_names()
        print(f"📋 Existing tables: {existing_tables}")
        
        # Check if audit_logs table exists
        if "audit_logs" in existing_tables:
            print("⚠️ audit_logs table already exists. Dropping it first...")
            
            # Drop the audit_logs table first (this will remove the foreign key constraint)
            db.session.execute(text("DROP TABLE audit_logs CASCADE CONSTRAINTS"))
            db.session.commit()
            print("✅ audit_logs table dropped successfully!")
        
        # Now create all tables
        print("🔄 Creating all tables...")
        db.create_all()
        print("✅ Tables created successfully!")
        
        # Verify the tables
        inspector = inspect(db.engine)
        tables = inspector.get_table_names()
        print(f"\n📋 Tables in database after creation: {tables}")
        
        # Check if audit_logs was created
        if "audit_logs" in tables:
            print("✅ audit_logs table created successfully!")
            # Show columns
            cols = inspector.get_columns("audit_logs")
            print("📝 Columns in audit_logs:")
            for col in cols:
                print(f"  - {col['name']} ({col['type']})")
        else:
            print("❌ audit_logs table was NOT created!")

def test_audit_log():
    with app.app_context():
        try:
            # Create a test log
            test_log = AuditLog(
                employee_id=1,
                action="Test",
                description="Test audit log entry"
            )
            db.session.add(test_log)
            db.session.commit()
            print("✅ Test log created successfully!")
            
            # View all logs
            logs = AuditLog.query.all()
            print(f"📊 Total logs: {len(logs)}")
            for log in logs:
                print(f"  {log.audit_id}: {log.action} - {log.description}")
        except Exception as e:
            print(f"❌ Error creating test log: {e}")

if __name__ == "__main__":
    print("🚀 Starting database fix...\n")
    create_tables_properly()
    print("\n🧪 Testing audit log...")
    test_audit_log()
    print("\n✅ Done!")