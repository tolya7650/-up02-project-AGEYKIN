"""Модели данных для проекта УП.02."""

class Product:
    """Класс Товар (Фильм)."""

    def __init__(self, product_id: int, genre: str, name: str, duration: int, price: float, quantity: int, poster: str):
        """
        Инициализация товара на основе структуры БД.
        
        :param product_id: Идентификатор (id)
        :param genre: Жанр фильма (жанр)
        :param name: Название фильма (название)
        :param duration: Длительность в минутах (длительность)
        :param price: Цена билета (цена)
        :param quantity: Доступно билетов/остаток (количество)
        :param poster: Имя файла или ссылка на постер (постер)
        """
        self.id = product_id
        self.жанр = genre
        self.название = name
        self.длительность = duration
        self.цена = price
        self.количество = quantity
        self.постер = poster

    def total(self) -> float:
        """Общая стоимость всех доступных билетов данного фильма (цена × количество)."""
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
