import time
from pymongo import MongoClient

# Підключення до MongoDB
mongo_client = MongoClient('mongodb://localhost:27017/')
mongo_db = mongo_client['online_store']
mongo_users_collection = mongo_db['users']

# Тестування часу вибору всіх користувачів
start_time = time.time()
mongo_users_data = list(mongo_users_collection.find())
end_time = time.time()
mongo_execution_time = end_time - start_time
print(f"Час вибору всіх користувачів з MongoDB {mongo_execution_time} мс")

# Тестування часу вставки нового користувача
start_time = time.time()
new_user_data = {
    'first_name': 'John',
    'last_name': 'Doe',
    'email': 'john.doe@example.com',
    'password': 'hashed_password',
    'registration_date': '2023-01-01 12:00:00',
    'address': '123 Main St'
}
mongo_users_collection.insert_one(new_user_data)
end_time = time.time()
mongo_execution_time = end_time - start_time
print(f"Час вставки нового користувача в MongoDB {mongo_execution_time} мс")

# Закриття підключення
mongo_client.close()