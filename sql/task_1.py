# pip install psycopg2

import psycopg2

# Для подключения к серверу PostgreSQL применяется функция connect(). 
# Она принимает настройки подключения:
conn = psycopg2.connect(dbname="market", 
                        user="alex", 
                        password="xoyrzk12345",
                        host="127.0.0.1", 
                        port="5432")
print(conn.status)
print("Подключение установлено")

cursor = conn.cursor()

# создаем таблицу people
# cursor.execute("CREATE TABLE people (id SERIAL PRIMARY KEY, name VARCHAR(50),  age INTEGER)")
# # поддверждаем транзакцию
# conn.commit()
# print("Таблица people успешно создана")

# # добавляем строку в таблицу people
# cursor.execute("INSERT INTO people (name, age) VALUES ('Tom', 38)")
# # выполняем транзакцию
# conn.commit()
# print("Данные добавлены")

# данные для добавления
# bob = ("Bob", 42)
# cursor.execute("INSERT INTO people (name, age) VALUES (%s, %s)", bob)
# conn.commit()

# данные для добавления
# people = [("Sam", 28), ("Alice", 33), ("Kate", 25)]
# cursor.executemany("INSERT INTO people (name, age) VALUES (%s, %s)", people)
# conn.commit()

# получаем все данные из таблицы people
# cursor.execute("SELECT * FROM people")
# print(cursor.fetchall())
# print(type(cursor.fetchall()))

cursor.execute("SELECT * FROM people")
# извлекаем первые 3 строки в полученном наборе
for i in cursor:
    print(i)
print(cursor.fetchmany(3))

cursor.close()  # закрываем курсор
conn.close()