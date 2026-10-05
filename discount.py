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
    """Проверяет наличие заказов фильма в предыдущем месяце."""
    start, end = get_previous_month_range(date)

    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    
    cur.execute("PRAGMA table_info(Заказ)")
    columns = [col[1] for col in cur.fetchall()]
    column_name = "товар" if "товар" in columns else ("товар_id" if "товар_id" in columns else columns[3])

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
    """Рассчитывает цену билета со скидкой 25% (если не было заказов)."""
    if has_orders_in_previous_month(product_name, date):
        return round(float(price), 2)
    return round(float(price) * 0.75, 2)
