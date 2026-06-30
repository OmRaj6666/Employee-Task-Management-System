import oracledb

try:
    connection = oracledb.connect(
        user="taskmanager",
        password="TaskManager123",
        host="localhost",
        port=1521,
        service_name="FREEPDB1"
    )

    print("✅ Connected Successfully to Oracle Database!")

except Exception as e:
    print("❌ Connection Failed")
    print(e)

finally:
    try:
        connection.close()
    except:
        pass