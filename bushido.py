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
cursor.execute('CREATE INDEX idx_email ON Users(email)')

# Сохраняем изменения и закрываем соединение
connection.commit()
connection.close()

