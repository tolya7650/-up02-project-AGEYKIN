from datetime import datetime
from models import Product

# Создаем тестовый объект фильма (id, жанр, название, длительность, цена, количество, постер)
p = Product(2, "Драма", "Ботинки Timberland", 120, 15000, 3, "poster.png")

date = datetime(2026, 10, 15)

# p.цена используется вместо p.price, так как поля в вашей БД на русском языке
print(f"Базовая цена: {p.цена}")
print(f"Со скидкой: {p.price_with_discount_auto(date)}")
