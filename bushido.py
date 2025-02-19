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

# Сохраняем изменения и закрываем соединение
connection.commit()
connection.close()

