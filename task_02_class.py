class Product:
    # Инициализатор (конструктор) класса с полями
    def __init__(self, name: str, price: int, qty: int):
        self.name = name
        self.price = price
        self.qty = qty

    # Метод для расчета общей стоимости
    def total(self):
        return self.price * self.qty

    # Метод для вывода информации в нужном формате
    def info(self):
        return f"{self.name}: {self.price} × {self.qty} = {self.total()} руб."

# Создание 3 объектов товаров
product1 = Product("Кроссовки", 8500, 3)
product2 = Product("Ботинки", 15000, 1)
product3 = Product("Туфли", 12000, 5)

# Вывод информации о каждом товаре
print(product1.info())
print(product2.info())
print(product3.info())
