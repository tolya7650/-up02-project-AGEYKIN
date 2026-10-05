"""Загрузка заказов из БД и связывание их с объектами Product."""
import sqlite3
from config import DB_PATH
from models import Product, Order


def get_all_orders():
    """Загружает заказы из БД, связывает их с товарами и возвращает список объектов Order."""
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    
    # 1. Сначала загружаем все фильмы (товары) в словарь, где ключ — НАЗВАНИЕ фильма
    # (так как в вашей таблице Заказ в поле 'товар' хранится текстовое название, а не id)
    cur.execute("SELECT * FROM Товар")
    product_rows = cur.fetchall()
    
    products_dict = {}
    for p_row in product_rows:
        prod = Product(
            product_id=p_row[0],
            genre=p_row[1],
            name=p_row[2],
            duration=p_row[3],
            price=p_row[4],
            quantity=p_row[5],
            poster=p_row[6]
        )
        products_dict[prod.название] = prod

    # 2. Загружаем все записи из таблицы Заказ
    cur.execute("SELECT id, дата, клиент, товар, количество FROM Заказ ORDER BY id")
    order_rows = cur.fetchall()
    conn.close()

    orders = []
    for o_row in order_rows:
        order_id = o_row[0]
        date = o_row[1]
        client = o_row[2]
        product_name = o_row[3]
        quantity = o_row[4]

        # Ищем объект фильма по его названию в нашем словаре
        # Если фильм не найден, создаем временный пустой объект, чтобы программа не падала
        product_obj = products_dict.get(
            product_name, 
            Product(0, "Неизвестно", product_name, 0, 0.0, 0, "")
        )

        # Создаем объект Заказа и передаем туда объект Товара
        order_obj = Order(
            order_id=order_id,
            date=date,
            client=client,
            product=product_obj,
            quantity=quantity
        )
        orders.append(order_obj)
        
    return orders


def print_orders_report(orders_list):
    """Выводит отчет по заказам и считает итоговую выручку."""
    print(f"\n{'=' * 75}")
    print(f"ОТЧЕТ ПО ЗАКАЗАМ КИНОТЕАТРА (Всего покупок: {len(orders_list)})")
    print("=" * 75)
    
    grand_total = 0.0
    for o in orders_list:
        print(o.info())
        grand_total += o.total()
        
    print("=" * 75)
    print(f"ОБЩАЯ ВЫРУЧКА КИНОТЕАТРА: {grand_total} руб.")
    print(f"{'=' * 75}\n")


if __name__ == "__main__":
    try:
        all_orders = get_all_orders()
        print_orders_report(all_orders)
    except sqlite3.OperationalError as e:
        print(f"Ошибка базы данных. Проверьте правильность пути в config.py. Подробнее: {e}")
