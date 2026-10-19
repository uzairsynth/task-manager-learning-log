import sqlite3
from datetime import date


connection = sqlite3.connect("tasks.db")
cursor = connection.cursor()


today = date.today().isoformat()

print("Today is:", today)


cursor.execute("""
SELECT * FROM tasks
WHERE deadline = ?
""", (today,))


tasks = cursor.fetchall()

print("Today's tasks:")
print(tasks)


connection.close()