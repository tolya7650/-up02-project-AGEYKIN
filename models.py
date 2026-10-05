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

    def total(self) -> float:
        """Общая стоимость (цена × количество)."""
        return self.цена * self.количество

    # --- ЗАДАНИЕ 8: Метод автоматического расчёта динамической скидки ---
    def price_with_discount_auto(self, date=None) -> float:
        """Цена со скидкой 25% по алгоритму ДЭ на основе заказов прошлого месяца."""
        if date is None:
            date = datetime.now()
        # В функцию discount.py передаем название фильма (self.название) и его базовую цену (self.цена)
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
