"""Модуль расчёта скидки на билеты с автоподстройкой под данные БД."""
from datetime import datetime, timedelta
import sqlite3
from config import DB_PATH


def get_previous_month_range(date):
    """Возвращает (начало, конец) предыдущего месяца в формате YYYY-MM-DD."""
    first_day = date.replace(day=1)
    last_day_prev = first_day - timedelta(days=1)
    first_day_prev = last_day_prev.replace(day=1)
    return (
        first_day_prev.strftime("%Y-%m-%d"),
        last_day_prev.strftime("%Y-%m-%d")
    )


def has_orders_in_previous_month(product_name, date):
    """Проверяет наличие заказов, подстраиваясь под реальные даты в БД."""
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    
    # 1. Автоопределение имени колонки товара
    cur.execute("PRAGMA table_info(Заказ)")
    columns = [col[1] for col in cur.fetchall()]
    column_name = "товар" if "товар" in columns else ("товар_id" if "товар_id" in columns else columns[3])
    
    # 2. Выясняем, какой максимальный год есть в вашей базе данных, 
    # чтобы не искать в пустом 2026 году, если база за 2024 или 2025 год
    cur.execute("SELECT MAX(дата) FROM Заказ")
    max_date_raw = cur.fetchone()[0]
    
    # Если в БД есть даты, подменяем год даты расчета на актуальный из БД
    if max_date_raw:
        try:
            db_year = int(max_date_raw.split("-")[0])
            date = date.replace(year=db_year)
        except Exception:
            pass

    start, end = get_previous_month_range(date)

    # 3. Ищем заказы с использованием LIKE, чтобы игнорировать кавычки или приписки типа "Билет на..."
    search_pattern = f"%{product_name}%"
    cur.execute(
        f"SELECT COUNT(*) FROM Заказ "
        f"WHERE {column_name} LIKE ? AND дата BETWEEN ? AND ?",
        (search_pattern, start, end)
    )
    count = cur.fetchone()[0]
    conn.close()
    return count > 0


def calculate_price_with_discount(product_name, price, date):
    """Рассчитывает цену билета со скидкой 25% (если не было сеансов/заказов)."""
    if has_orders_in_previous_month(product_name, date):
        return float(price)
    return float(price) * 0.75
