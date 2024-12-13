import sqlite3
    
# Создаем подключение к базе данных
connection = sqlite3.connect('movie.db')
# Создание курсора для выполнения SQL-запросов
cursor = connection.cursor()

# Символ * обозначает все
cursor.execute(''' 
SELECT title, name AS director_name
FROM movies
INNER JOIN directors ON movies.director_id = directors.id
''')

# Использование метода fetchall() для получения результатов
result = cursor.fetchall()

# Вывод результатов
for row in result:
    print(row)

# Закрываем соединение с базой данных после использования
connection.close()