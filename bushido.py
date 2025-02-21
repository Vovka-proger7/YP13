import sqlite3

# Устанавливаем соединение с базой данных
connection = sqlite3.connect('my_database.db')
cursor = connection.cursor()

# Создаем таблицу Users
cursor.execute('''
CREATE TABLE IF NOT EXISTS Users (
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER
)
''')

# Создание индекса для столбца "email"
cursor.execute('CREATE INDEX IF NOT EXISTS idx_email ON Users(email)')

cursor.execute('''INSERT INTO Users (username, email,
age) VALUES ('newuser', 'newuser@example.com', 28)''')


# Обновляем возраст пользователя "newuser"
cursor.execute('''UPDATE Users SET age = 29 WHERE
username = 'newuser'
''')

# Удаляем пользователя "newuser"
cursor.execute('''DELETE FROM Users WHERE
username = 'newuser'
''')

# Выбираем всех пользователей
cursor.execute('SELECT * FROM Users')
users = cursor.fetchall()

# Выводим результаты
for user in users:
    print(user)


# Выбираем имена и возраст пользователей старше 25 лет
cursor.execute('SELECT username, age FROM Users WHERE age > ?', (25,))
results = cursor.fetchall()
for row in results:
    print(row)

# Получаем средний возраст пользователей для каждого возраста
cursor.execute('SELECT age, AVG(age) FROM Users GROUP BY age')
results = cursor.fetchall()
for row in results:
    print(row)


# Фильтруем группы по среднему возрасту больше 30
cursor.execute('SELECT age, AVG(age) FROM Users GROUP BY age HAVING AVG(age) > ?', (30,))
filtered_results = cursor.fetchall()
for row in filtered_results:
    print(row)



# Сохраняем изменения и закрываем соединение
connection.commit()
connection.close()

