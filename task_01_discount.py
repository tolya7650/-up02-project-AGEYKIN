# Запрос данных у пользователя
price = float(input("Введите цену: "))
discount_percent = float(input("Введите скидку (%): "))

# Расчет цены со скидкой
final_price = price * (1 - discount_percent / 100)

# Вывод результата с округлением до двух знаков после запятой
print(f"Цена со скидкой: {final_price:.2f} руб.")


