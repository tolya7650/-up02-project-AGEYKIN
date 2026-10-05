"""Модели данных для проекта УП.02."""

class Product:
    """Класс Товар (Фильм)."""

    def __init__(self, product_id: int, genre: str, name: str, duration: int, price: float, quantity: int, poster: str):
        """Инициализация товара на основе структуры БД."""
        self.id = product_id
        self.жанр = genre
        self.название = name
        self.длительность = duration
        self.цена = price
        self.количество = quantity
        self.постер = poster

    def total(self) -> float:
        """Общая стоимость всех доступных билетов данного фильма."""
        return self.цена * self.количество

    def price_with_discount(self, discount_percent: float) -> float:
        """Вычисляет цену билета со скидкой в процентах."""
        return self.цена * (1 - discount_percent / 100)

    def indicator(self) -> str:
        """Индикатор остатка билетов «много» или «мало» (порог 5)."""
        return "много" if self.количество > 5 else "мало"

    def info(self) -> str:
        """Возвращает строку с подробной информацией о фильме/товаре."""
        return (f"Билет на фильм '{self.название}' ({self.жанр}, {self.длительность} мин.). "
                f"Цена: {self.цена} руб. Осталось мест: {self.количество} шт. ({self.indicator()})")

    # --- ЗАДАНИЕ 1: Новый метод ---
    def is_available(self) -> bool:
        """Возвращает True, если билеты есть в наличии (> 0)."""
        return self.количество > 0


class Order:
    """Класс Заказ (Покупка билетов)."""

    def __init__(self, order_id: int, date: str, client: str, product: Product, quantity: int):
        """
        Инициализация заказа.
        
        :param order_id: Идентификатор заказа (id)
        :param date: Дата и время сеанса/покупки (дата)
        :param client: ФИО зрителя (клиент)
        :param product: Объект класса Product (связанный фильм)
        :param quantity: Сколько билетов куплено (количество)
        """
        self.id = order_id
        self.date = date
        self.client = client
        self.product = product      # Передаем сюда готовый объект Product
        self.quantity = quantity    # Количество купленных билетов в данном заказе

    # --- ЗАДАНИЕ 2: Методы класса Order ---
    def total(self) -> float:
        """Стоимость конкретного заказа (цена билета × количество купленных)."""
        return self.product.цена * self.quantity

    def info(self) -> str:
        """Возвращает информацию о заказе."""
        return (f"Заказ №{self.id} от {self.date}: {self.client} — "
                f"Фильм '{self.product.название}' × {self.quantity} шт. на сумму {self.total()} руб.")
