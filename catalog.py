"""Каталог товаров (Фильмов) для Варианта 3."""
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import os

from config import COLOR_HIGHLIGHT, FONT_FAMILY


def create_product_card(parent, product):
    """Создаёт карточку фильма по макету ДЭ.
    
    Структура кортежа product (Вариант 3):
    [0] - id, [1] - жанр, [2] - название, [3] - длительность, 
    [4] - цена, [5] - количество, [6] - постер
    """
    genre = product[1]
    name = product[2]
    duration = product[3]
    price = product[4]
    qty = product[5]
    poster = product[6]

    bg_color = COLOR_HIGHLIGHT if qty <= 3 else "white"

    card = tk.Frame(parent, bg=bg_color, bd=1, relief="solid")
    card.pack(fill="x", padx=10, pady=5)

    # === Изображение / Постер (слева) ===
    img_frame = tk.Frame(card, bg=bg_color)
    img_frame.pack(side="left", padx=10, pady=10)

    image_path = poster if poster else "resources/picture.png"
    if not os.path.exists(image_path):
        image_path = "resources/picture.png"

    try:
        img = Image.open(image_path).resize((100, 100))
        photo = ImageTk.PhotoImage(img)
        img_label = tk.Label(img_frame, image=photo, bg=bg_color)
        img_label.image = photo   # type: ignore
        img_label.pack()
    except Exception:
        tk.Label(img_frame, text="[ПОСТЕР]", bg=bg_color,
                 width=10, height=5, font=(FONT_FAMILY, 10)).pack()

    # === Текстовая часть (справа) ===
    text_frame = tk.Frame(card, bg=bg_color)
    text_frame.pack(side="left", fill="both", expand=True, padx=10, pady=10)

    # 1. Жанр | Наименование (Сверху)
    title = f"{genre} | {name}"
    tk.Label(text_frame, text=title, font=(FONT_FAMILY, 14, "bold"),
             bg=bg_color, anchor="w").pack(fill="x")

    # 2. Категория
    tk.Label(text_frame, text=f"Категория: {genre}",
             font=(FONT_FAMILY, 11), bg=bg_color, anchor="w").pack(fill="x")

    # 3. Длительность фильма
    tk.Label(text_frame, text=f"Длительность: {duration} мин.",
             font=(FONT_FAMILY, 11), bg=bg_color, anchor="w").pack(fill="x")

    # 4. Количество / Оставшиеся места
    indicator = "много" if qty > 5 else "мало"
    tk.Label(text_frame, text=f"Места: {indicator} ({qty})",
             font=(FONT_FAMILY, 11), bg=bg_color, anchor="w").pack(fill="x")

    # 5. Цена билета (Выравнивание по правому краю)
    tk.Label(text_frame, text=f"{price} руб.",
             font=(FONT_FAMILY, 14, "bold"),
             bg=bg_color, anchor="e").pack(fill="x")

    return card
