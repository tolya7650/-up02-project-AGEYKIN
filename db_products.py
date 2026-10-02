"""Загрузка товаров из БД с расширенным выводом."""
import sqlite3
from config import DB_PATH


def get_all_products():
    """Возвращает список всех товаров."""
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("SELECT * FROM Товар ORDER BY id")
    products = cur.fetchall()
    conn.close()
    return products


def get_products_by_category(genre):
    """Товары по жанру."""
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("SELECT * FROM Товар WHERE жанр = ?", (genre,))
    products = cur.fetchall()
    conn.close()
    return products


def get_products_low_stock():
    """Товары с количеством <= 3."""
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("SELECT * FROM Товар")
    all_products = cur.fetchall()
    conn.close()
    # Фильтрация по предпоследнему полю (количество)
    return [p for p in all_products if int(p[-2]) <= 3]


def get_categories():
    """Список всех жанров."""
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("SELECT DISTINCT жанр FROM Товар ORDER BY жанр")
    categories = [row[0] for row in cur.fetchall()]
    conn.close()
    return categories


def print_catalog(products):
    """Каталог с индикатором."""
    print(f"\n{'=' * 60}")
    print(f"КАТАЛОГ ({len(products)} товаров)")
    print("=" * 60)

    for p in products:
        name = p[1]       # Название
        genre = p[2]      # Жанр
        price = p[4]      # Цена
        qty = int(p[-2])  # Количество (предпоследнее поле)

        indicator = "много" if qty > 5 else "мало"
        highlight = "⚠️" if qty <= 3 else "  "

        print(f"{highlight} {name} ({genre})")
        print(f"   Цена: {price} руб. | Кол-во: {qty} ({indicator})")

    print("=" * 60)


if __name__ == "__main__":
    print("1. Все товары")
    print_catalog(get_all_products())

    print("\n2. Категории:")
    for cat in get_categories():
        print(f"   - {cat}")

    print("\n3. Товары с низким остатком (≤3):")
    print_catalog(get_products_low_stock())
