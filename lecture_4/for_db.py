import sqlite3
conn = sqlite3.connect('school.db')
print("Database 'school.db' created successfully.")
cursor = conn.cursor()



cursor.execute('''
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    full_name TEXT NOT NULL,
    birth_year INTEGER NOT NULL
)
''')


conn.commit()
print("Table 'students' created successfully.")

cursor.execute('PRAGMA foreign_keys = ON;')

cursor.execute('''
CREATE TABLE IF NOT EXISTS grades (
    id INTEGER PRIMARY KEY AUTOINCREMENT, 
    student_id INTEGER NOT NULL,
    subject TEXT NOT NULL,
    grade INTEGER NOT NULL,
    FOREIGN KEY(student_id) REFERENCES students(id)ON DELETE RESTRICT ON UPDATE CASCADE) ''')


conn.commit()
print("Table 'grades' created successfully.")


new_students = [
        ('Alice Johnson', 2005),
        ('Brian Smith', 2004),
        ('Carla Reyes', 2006),
        ('Daniel Kim', 2005),
        ('Eva Thompson', 2003),
        ('Felix Nguyen', 2007),
        ('Grace Patel', 2005),
        ('Henry Lopez', 2004),
        ('Isabella Martinez', 2006)
    ]
cursor.executemany("INSERT INTO students (full_name, birth_year) VALUES (?, ?)", new_students)
conn.commit()
print("Students inserted successfully.")


new_grades = [
    (1, 'Math', 88), (1, 'English', 92), (1, 'Science', 85),
    (2, 'Math', 75), (2, 'History', 83), (2, 'English', 79),
    (3, 'Science', 95), (3, 'Math', 91), (3, 'Art', 89),
    (4, 'Math', 84), (4, 'Science', 88), (4, 'Physical Education', 93),
    (5, 'English', 90), (5, 'History', 85), (5, 'Math', 88),
    (6, 'Science', 72), (6, 'Math', 78), (6, 'English', 81),
    (7, 'Art', 94), (7, 'Science', 87), (7, 'Math', 90),
    (8, 'History', 77), (8, 'Math', 83), (8, 'Science', 80),
    (9, 'English', 96), (9, 'Math', 89), (9, 'Art', 92)
    ]
cursor.executemany("INSERT INTO grades (student_id, subject, grade) VALUES (?, ?, ?)", new_grades)
conn.commit()
print("Grades inserted successfully.")




























# import sqlite3
#
# conn = sqlite3.connect('school.db')
# cursor = conn.cursor()
#
# # Включаем внешние ключи
# cursor.execute("PRAGMA foreign_keys = ON")
#
# print("Очищаем базу данных...")
#
# # 1. УДАЛЯЕМ данные в правильном порядке
# cursor.execute("DELETE FROM grades")  # сначала оценки (зависимая таблица)
# cursor.execute("DELETE FROM students")  # потом студентов
#
# # 2. СБРАСЫВАЕМ автоинкремент (ЭТО ВАЖНО!)
# cursor.execute("DELETE FROM sqlite_sequence WHERE name='students'")
# cursor.execute("DELETE FROM sqlite_sequence WHERE name='grades'")
#
# conn.commit()
# print(" Старые данные удалены, автоинкремент сброшен")












# conn.close()


# conn = sqlite3.connect('school.db')
#
# # conn.execute("DROP TABLE students")
# conn.execute("DROP TABLE grades")
#
# print("data dropped successfully")
#
# # conn.close()




#     # 4. Создаем таблицу
#     cursor.execute('''
#     CREATE TABLE IF NOT EXISTS students (
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         full_name TEXT NOT NULL,
#         birth_year INTEGER NOT NULL
#     )
#     ''')
#
#     conn.commit()
#     print("База данных '{db_name}' успешно создана!")
#
#     # 5. Проверяем таблицы
#     cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
#     tables = cursor.fetchall()
#     print(f"Таблицы в базе: {tables}")
#
#     conn.close()
#
# except Exception as e:
#     print(f"Ошибка: {e}")