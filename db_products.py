"""Загрузка товаров из БД в объекты класса Product с фильтрацией."""
import sqlite3
from config import DB_PATH
from models import Product


def get_all_products():
    """Возвращает список всех объектов Product из БД."""
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("SELECT * FROM Товар ORDER BY id")
    rows = cur.fetchall()
    conn.close()

    products = []
    for row in rows:
        product = Product(
            product_id=row[0],
            genre=row[1],
            name=row[2],
            duration=row[3],
            price=row[4],
            quantity=row[5],
            poster=row[6]
        )
        products.append(product)
    return products


def get_products_by_category(category):
    """Возвращает список объектов Product по жанру (категории)."""
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    # В вашей БД колонка называется 'жанр', а не 'категория'
    cur.execute("SELECT * FROM Товар WHERE жанр = ?", (category,))
    rows = cur.fetchall()
    conn.close()

    products = []
    for row in rows:
        product = Product(
            product_id=row[0],
            genre=row[1],
            name=row[2],
            duration=row[3],
            price=row[4],
            quantity=row[5],
            poster=row[6]
        )
        products.append(product)
    return products


def get_products_low_stock():
    """Возвращает товары с количеством ≤ 3."""
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("SELECT * FROM Товар WHERE количество <= 3")
    rows = cur.fetchall()
    conn.close()

    products = []
    for row in rows:
        product = Product(
            product_id=row[0],
            genre=row[1],
            name=row[2],
            duration=row[3],
            price=row[4],
            quantity=row[5],
            poster=row[6]
        )
        products.append(product)
    return products


def print_catalog_with_highlight(products):
    """Выводит каталог с подсветкой ⚠️ для фильмов, где количество билетов ≤ 3."""
    print(f"\n{'=' * 70}")
    print(f"КАТАЛОГ ({len(products)} фильмов)")
    print("=" * 70)

    for p in products:
        # p.количество используется вместо p.quantity, так как имя поля на русском языке
        highlight = "⚠️" if p.количество <= 3 else "  "
        print(f"{highlight} {p.info()}")

    print("=" * 70)


if __name__ == "__main__":
    print("1. Все товары:")
    print_catalog_with_highlight(get_all_products())

    # Вместо абстрактных «Кроссовок» передаем ваш реальный жанр из БД
    print("\n2. Товары категории «Фантастика»:")
    print_catalog_with_highlight(get_products_by_category("Фантастика"))

    print("\n3. Товары с низким остатком (≤3):")
    print_catalog_with_highlight(get_products_low_stock())

