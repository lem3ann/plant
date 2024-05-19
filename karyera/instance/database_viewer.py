import sqlite3

# SQLite faylını aç
conn = sqlite3.connect('applications.db')
cursor = conn.cursor()

# cedvelleri görüntüle
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()
for table in tables:
    print(table)

# Bir SQL sorgusu çalışdıraraq db melumatlarina baxmaq
cursor.execute("SELECT * FROM Application;")
rows = cursor.fetchall()
for row in rows:
    print(row)


conn.close()
