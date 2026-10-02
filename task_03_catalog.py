# Список словарей с товарами
catalog = [
    {"name": "Кроссовки", "price": 8500, "qty": 3},
    {"name": "Ботинки", "price": 15000, "qty": 1},
    {"name": "Туфли", "price": 12000, "qty": 5},
    {"name": "Сандалии", "price": 4500, "qty": 8},
    {"name": "Кеды", "price": 6000, "qty": 2}
]

print("Каталог товаров:")
total_sum = 0

# Цикл по списку с получением индекса (начиная с 1)
for i, item in enumerate(catalog, start=1):
    name = item["name"]
    price = item["price"]
    qty = item["qty"]
    
    # Расчет стоимости для текущей позиции
    cost = price * qty
    total_sum += cost
    
    # Вывод строки товара (с выравниванием названия под ширину до 10 символов)
    print(f"{i}. {name:<10} — {price} × {qty} = {cost} руб.")

# Вывод разделителя и общего итога
print("-" * 30)
print(f"Итого: {total_sum} руб.")
