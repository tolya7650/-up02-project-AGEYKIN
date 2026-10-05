"""Тестирование алгоритма скидки."""
from datetime import datetime
from discount import calculate_price_with_discount


def run_tests():
    # Все строки внутри функции run_tests() должны быть сдвинуты на 4 пробела!
    test_cases = [
        # (product_id, price, date, expected, comment)
        ("1", 8500.0, datetime(2026, 10, 15), 8500.0, "Заказы есть в сентябре"),
        ("2", 15000.0, datetime(2026, 10, 15), 15000.0, "Заказов нет → скидка"),
        ("3", 12000.0, datetime(2026, 10, 15), 12000.0, "Заказы есть"),
        ("4", 4500.0, datetime(2026, 10, 15), 3375.0, "Заказов нет → скидка"),
        ("5", 6000.0, datetime(2026, 10, 15), 4500.0, "Заказов нет → скидка"),
        
        # Скорректированные тесты на ноябрь
        ("2", 15000.0, datetime(2026, 11, 15), 11250.0, "В октябре заказы были?"),
        ("1", 8500.0, datetime(2026, 11, 15), 6375.0, "В октябре заказы были?"),
        ("4", 4500.0, datetime(2026, 9, 1), 3375.0, "Август — заказов нет"),
        
        # Ваши собственные тесты
        ("3", 600.0, datetime(2026, 10, 1), 600.0, "Граничный тест: 1-е число месяца"),
        ("7", 850.0, datetime(2026, 10, 15), 637.5, "Фильм 'Хоббит' — нет заказов в сентябре"),
        ("6", 0.0, datetime(2026, 10, 15), 0.0, "Тест на бесплатный билет (цена 0)"),
    ]

    print("=" * 75)
    print("РАСШИРЕННОЕ ТЕСТИРОВАНИЕ АЛГОРИТМА СКИДКИ")
    print("=" * 75)

    passed = 0
    for product_id, price, date, expected, comment in test_cases:
        result = calculate_price_with_discount(product_id, price, date)
        
        is_ok = abs(result - expected) < 0.01
        status = "✅" if is_ok else "❌"
        
        if is_ok:
            passed += 1
            
        print(f"{status} Товар {product_id} на {date.date()}: "
              f"{price} → {result} (ожидалось {expected}) — {comment}")

    print("=" * 75)
    print(f"Пройдено: {passed} / {len(test_cases)}")


# Точка входа в программу пишется без отступов, с самого начала строки
if __name__ == "__main__":
    run_tests()
