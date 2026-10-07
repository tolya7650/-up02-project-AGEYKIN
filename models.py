"""Модели данных для проекта УП.02."""
from datetime import datetime
from discount import calculate_price_with_discount


class Product:
    """Класс Товар (Фильм) адаптированный под структуру Варианта 3."""

    def __init__(self, product_id: int, genre: str, name: str, duration: int, price: float, quantity: int, poster: str):
        """Инициализация полей на основе реальной таблицы 'Товар' из БД."""
        self.id = product_id
        self.жанр = genre
        self.название = name
        self.длительность = duration
        self.цена = price
        self.количество = quantity
        self.постер = poster

    def is_available(self):
        """Товар доступен для заказа?"""
        return self.количество > 0

    def total(self) -> float:
        """Общая стоимость всех доступных билетов данного фильма."""
        return self.цена * self.количество

    def discounted_price(self):
        """Цена со скидкой 25% (упрощённо для Пары 7)."""
        return self.цена * 0.90

    def price_with_discount_auto(self, date=None) -> float:
        """Цена со скидкой 25% по алгоритму ДЭ на основе заказов прошлого месяца."""
        if date is None:
            date = datetime.now()
        return calculate_price_with_discount(self.название, self.цена, date)

    def indicator(self) -> str:
        """Порог остатка билетов «много» или «мало» (порог 5)."""
        return "много" if self.количество > 5 else "мало"

    def info(self) -> str:
        """Строка с подробной информацией о фильме/товаре."""
        return (
            f"Билет на фильм '{self.название}' ({self.жанр}, {self.длительность} мин.): "
            f"{self.цена} руб. × {self.количество} мест = {self.total()} руб. "
            f"({self.indicator()})"
        )


class Order:
    """Класс Заказ (Покупка билетов)."""

    def __init__(self, order_id: int, date: str, client: str, product: Product, quantity: int):
        """Инициализация заказа."""
        self.id = order_id
        self.date = date
        self.client = client
        self.product = product      
        self.quantity = quantity    

    def total(self) -> float:
        """Стоимость конкретного заказа."""
        return self.product.цена * self.quantity

    def info(self) -> str:
        """Возвращает развернутую информацию о заказе."""
        return (f"Заказ №{self.id} от {self.date}: {self.client} — "
                f"Фильм '{self.product.название}' × {self.quantity} шт. на сумму {self.total()} руб.")

    # --- ЗДЕСЬ НАЧИНАЕТСЯ ГОТОВЫЙ КОД ИЗ ЗАДАНИЯ 1 ДОМАШНЕЙ РАБОТЫ ---
    def order_info(self):
        """Вспомогательный метод вывода краткой информации о заказе по заданию ДЗ."""
        return f"Заказ №{self.id} от {self.date}: {self.client}"
