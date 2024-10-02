import sqlite3

# Veritabanı bağlantısını oluştur
conn = sqlite3.connect('jobs.db')
cursor = conn.cursor()

# Tabloyu olusturma

cursor.execute('''
    CREATE TABLE IF NOT EXISTS job_listings (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        description TEXT,
        skills_required TEXT
        )
               ''')

# İş ilanlarını ekleme

jobs = [
    ("Data Scientist", "Looking for a data scientist with expertise in machine learning and Python.", "machine learning, python, data analysis"),
    
]

cursor.executemany('''
    INSERT INTO job_listings (title, description, skills_required)
    VALUES (?, ?, ?)
    ''', jobs)

# Değişiklikleri Kaydetme

conn.commit()
conn.close()