from models import Product

# Создание тестового объекта вручную должно выглядеть так:
p = Product(
    product_id=1,
    genre="Фантастика",
    name="Дюна 2",
    duration=166,
    price=800.0,
    quantity=50,
    poster="dune.png"
)

# Проверяем работу методов
print(p.info())
