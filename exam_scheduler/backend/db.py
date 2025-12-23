import pymysql

def get_conn():
    return pymysql.connect(
        host="localhost",
        user="root",
        password="",      # WAMP default
        database="exam_scheduler",
        port=3306,
        charset='utf8mb4'
    )

conn = get_conn()
print("Connected successfully!")  # Should print
conn.close()
