import mysql.connector

conn = mysql.connector.connect(host='localhost', database='clg_students', user='root', password='0210')
cursor = conn.cursor()
print(conn.is_connected())

sql = "select * from clg_stu"
cursor.execute(sql)
result = cursor.fetchall()
print(result)