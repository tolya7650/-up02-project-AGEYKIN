"""Каталог товаров (Фильмов) для Варианта 3 с ДЗ."""
import tkinter as tk
import os
from PIL import Image, ImageTk
from config import COLOR_HIGHLIGHT, FONT_FAMILY

def create_product_card(parent, product):
    """Создаёт карточку фильма по макету ДЭ с разделителем."""
    genre = product[1]
    name = product[2]
    duration = product[3]
    price = product[4]
    qty = product[5]
    poster = product[6]

    # Задание 1 ДЗ: Подсветка светло-красным (#ff8080), если количество мест <= 3
    bg_color = COLOR_HIGHLIGHT if qty <= 3 else "white"

    card = tk.Frame(parent, bg=bg_color, bd=1, relief="solid")
    card.pack(fill="x", padx=10, pady=5)

    # === Изображение (слева) ===
    img_frame = tk.Frame(card, bg=bg_color)
    img_frame.pack(side="left", padx=10, pady=10)

    image_path = poster if poster else "resources/picture.png"
    if not os.path.exists(image_path):
        image_path = "resources/picture.png"

    try:
        img = Image.open(image_path).resize((100, 100))
        photo = ImageTk.PhotoImage(img)
        img_label = tk.Label(img_frame, image=photo, bg=bg_color)
        img_label.image = photo  # type: ignore
        img_label.pack()
    except Exception:
        tk.Label(img_frame, text="[ПОСТЕР]", bg=bg_color, width=10, height=5, font=(FONT_FAMILY, 10)).pack()

    # === Текстовый блок ===
    text_frame = tk.Frame(card, bg=bg_color)
    text_frame.pack(side="left", fill="both", expand=True, padx=10, pady=10)

    tk.Label(text_frame, text=f"{genre} | {name}", font=(FONT_FAMILY, 14, "bold"), bg=bg_color, anchor="w").pack(fill="x")
    tk.Label(text_frame, text=f"Категория: {genre}", font=(FONT_FAMILY, 11), bg=bg_color, anchor="w").pack(fill="x")
    tk.Label(text_frame, text=f"Длительность: {duration} мин.", font=(FONT_FAMILY, 11), bg=bg_color, anchor="w").pack(fill="x")
    
    indicator = "много" if qty > 5 else "мало"
    tk.Label(text_frame, text=f"Места: {indicator} ({qty})", font=(FONT_FAMILY, 11), bg=bg_color, anchor="w").pack(fill="x")
    tk.Label(text_frame, text=f"{price} руб.", font=(FONT_FAMILY, 14, "bold"), bg=bg_color, anchor="e").pack(fill="x")

    # 📌 Задание 1 ДЗ: Линия-разделитель внизу карточки товара (Акцентный цвет #70B2AF)
    separator = tk.Frame(parent, height=2, bg="#70B2AF")
    separator.pack(fill="x", padx=10, pady=2)

    return card
