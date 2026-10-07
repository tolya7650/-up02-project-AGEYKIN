import sqlite3
import os


import sqlite3
import os

def get_all_products():
    """Загружает все фильмы из реальной базы данных SQLite, лежащей в папке databases."""
    
    # Получаем путь к текущей папке, где лежит этот скрипт (up02_project)
    current_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Прописываем точный путь к базе внутри папки databases
    path_to_db = os.path.join(current_dir, "databases", "db_variant_3.db")

    # Подключаемся строго по этому пути
    conn = sqlite3.connect(path_to_db)
    cur = conn.cursor()
    
    # Делаем запрос к заполненной таблице
    cur.execute("SELECT * FROM Товар ORDER BY id")
    products = cur.fetchall()
    
    conn.close()
    return products
