import time
import pymysql

# Підключення до MySQL
mysql_connection = pymysql.connect(
    host='localhost',
    user='kseniya_gladkih',
    password='passexams',
    database='online_store'
)
mysql_cursor = mysql_connection.cursor()

# Тестування часу вибору всіх користувачів
start_time = time.time()
mysql_cursor.execute("SELECT * FROM Users")
result = mysql_cursor.fetchall()
end_time = time.time()
mysql_execution_time = end_time - start_time
print(f"Час вибору всіх користувачів з MySQL: {mysql_execution_time} мс")

# Тестування часу вставки нового користувача
start_time = time.time()
mysql_cursor.execute("INSERT INTO Users (first_name, last_name, email, password, registration_date, address) VALUES ('John', 'Doe', 'john.doe@example.com', 'hashed_password', '2023-01-01 12:00:00', '123 Main St')")
mysql_connection.commit()
end_time = time.time()
mysql_execution_time = end_time - start_time
print(f"Час вставки нового користувача в MySQL: {mysql_execution_time} мс")

# Закриття підключення
mysql_cursor.close()
mysql_connection.close()