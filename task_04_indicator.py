# Исходный список словарей из программы 3
catalog = [
    {"name": "Кроссовки", "price": 8500, "qty": 3},
    {"name": "Ботинки", "price": 15000, "qty": 1},
    {"name": "Туфли", "price": 12000, "qty": 5},
    {"name": "Сандалии", "price": 4500, "qty": 8},
    {"name": "Кеды", "price": 6000, "qty": 2}
]

# Сортировка списка по убыванию количества (qty), чтобы "много" оказалось сверху
catalog.sort(key=lambda item: item["qty"], reverse=True)

print("Каталог с индикатором:")

# Вывод элементов с расчетом индикатора
for i, item in enumerate(catalog, start=1):
    name = item["name"]
    qty = item["qty"]
    
    # Определение статуса (много/мало) по условию задачи
    indicator = "много" if qty > 5 else "мало"
    
    # Вывод строки с форматированием названия
    print(f"{i}. {name:<10} — {qty} шт. → {indicator}")
