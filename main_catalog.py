"""Главное окно приложения со всеми функциями ДЗ и Продвинутого блока."""
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import os
from config import APP_TITLE, FONT_FAMILY
import db_products as db
from catalog import create_product_card

class CatalogWindow:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title(APP_TITLE)
        self.root.geometry("950://750")
        self.root.minsize(800, 600)

        # Переменные для фильтрации и сортировки (Задания А1 - А5)
        self.search_var = tk.StringVar()
        self.category_var = tk.StringVar(value="Все категории")
        self.sort_var = tk.StringVar(value="Без сортировки")

        self.build_ui()
        
        # Привязка обработчиков событий к переменным для автоматического обновления списка
        self.search_var.trace_add("write", lambda *a: self.refresh_catalog())
        self.category_var.trace_add("write", lambda *a: self.refresh_catalog())
        self.sort_var.trace_add("write", lambda *a: self.refresh_catalog())

        self.refresh_catalog()

    def build_ui(self):
        # Шапка приложения
        header = tk.Frame(self.root, bg="#D2F6E7")
        header.pack(fill="x")

        # 📌 Задание 2 ДЗ: Добавление логотипа в шапку слева
        logo_path = "resources/logo.png"
        if os.path.exists(logo_path):
            try:
                logo_img = Image.open(logo_path).resize((50, 50))
                self.logo_photo = ImageTk.PhotoImage(logo_img)
                tk.Label(header, image=self.logo_photo, bg="#D2F6E7").pack(side="left", padx=10, pady=10)
            except Exception:
                pass

        tk.Label(header, text="КАТАЛОГ ФИЛЬМОВ", font=(FONT_FAMILY, 16, "bold"), bg="#D2F6E7").pack(side="left", pady=15, padx=10)

        # --- Элементы Управления (Продвинутый блок А1 - А3) ---
        # Панель инструментов справа в шапке
        controls_frame = tk.Frame(header, bg="#D2F6E7")
        controls_frame.pack(side="right", padx=10, pady=15)

        # Выпадающий список сортировки (Задание А3)
        tk.Label(controls_frame, text="Сортировка:", font=(FONT_FAMILY, 10), bg="#D2F6E7").pack(side="left", padx=2)
        sort_combo = ttk.Combobox(controls_frame, textvariable=self.sort_var, values=["Без сортировки", "Цена ↑", "Цена ↓"], state="readonly", width=14)
        sort_combo.pack(side="left", padx=5)

        # Выпадающий список категорий/жанров (Задание А2)
        tk.Label(controls_frame, text="Жанр:", font=(FONT_FAMILY, 10), bg="#D2F6E7").pack(side="left", padx=2)
        try:
            raw_products = db.get_all_products()
            genres = sorted(list(set([p[1] for p in raw_products])))
            categories = ["Все категории"] + genres
        except Exception:
            categories = ["Все категории"]
        
        category_combo = ttk.Combobox(controls_frame, textvariable=self.category_var, values=categories, state="readonly", width=14)
        category_combo.pack(side="left", padx=5)

        # Поле интерактивного поиска по названию (Задание А1)
        tk.Label(controls_frame, text="Поиск:", font=(FONT_FAMILY, 10), bg="#D2F6E7").pack(side="left", padx=2)
        search_entry = tk.Entry(controls_frame, textvariable=self.search_var, width=15)
        search_entry.pack(side="left", padx=5)

        # --- Область вывода списка с прокруткой ---
        self.canvas = tk.Canvas(self.root, bg="white", highlightthickness=0)
        scrollbar = ttk.Scrollbar(self.root, orient="vertical", command=self.canvas.yview)
        self.catalog_frame = tk.Frame(self.canvas, bg="white")
        
        self.catalog_frame.bind("<Configure>", lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))
        self.canvas.create_window((0, 0), window=self.catalog_frame, anchor="nw")
        
        # Интеграция прокрутки колесиком мыши
        self.canvas.bind_all("<MouseWheel>", lambda e: self.canvas.yview_scroll(int(-1*(e.delta/120)), "units"))
        
        self.canvas.configure(yscrollcommand=scrollbar.set)
        self.canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

    def refresh_catalog(self):
        """📌 Задания А4 и А5: Совместная обработка поиска, фильтра и сортировки."""
        # Очищаем текущие отображаемые карточки
        for widget in self.catalog_frame.winfo_children():
            widget.destroy()

        try:
            products = db.get_all_products()
            query = self.search_var.get().lower()
            selected_genre = self.category_var.get()
            selected_sort = self.sort_var.get()

            filtered_products = []
            for p in products:
                # Фильтрация по названию фильма (p[2])
                match_search = query in p[2].lower()
                # Фильтрация по жанру фильма (p[1])
                match_genre = selected_genre == "Все категории" or p[1] == selected_genre

                if match_search and match_genre:
                    filtered_products.append(p)

            # Сортировка данных по цене билета (p[4])
            if selected_sort == "Цена ↑":
                filtered_products.sort(key=lambda p: p[4])
            elif selected_sort == "Цена ↓":
                filtered_products.sort(key=lambda p: p[4], reverse=True)

            # Отрисовка итогового отфильтрованного списка
            if not filtered_products:
                tk.Label(self.catalog_frame, text="Совпадающих фильмов не найдено.", font=(FONT_FAMILY, 12), bg="white").pack(pady=30)
            else:
                for p in filtered_products:
                    create_product_card(self.catalog_frame, p)

        except Exception as e:
            tk.Label(self.catalog_frame, text=f"Критическая ошибка работы каталога: {e}", fg="red", bg="white").pack(pady=20)

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    CatalogWindow().run()
