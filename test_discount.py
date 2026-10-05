"""Расширенное тестирование алгоритма скидки с генерацией отчета."""
from datetime import datetime
from discount import calculate_price_with_discount


def print_test_report(passed: int, total: int):
    """Выводит графический отчёт о результатах тестирования."""
    print("========================================")
    print("ОТЧЁТ О ТЕСТИРОВАНИИ")
    print(f"Пройдено: {passed} / {total}")
    if passed == total:
        print("Результат: ✅ УСПЕХ")
    else:
        print("Результат: ❌ ЕСТЬ ОШИБКИ")
    print("========================================")


def run_homework_tests():
    # Отступ здесь равен ровно 4 пробелам (переменная находится внутри функции)
    test_cases = [
        # --- ЗАДАНИЕ 1: 5 ГРАНИЧНЫХ ТЕСТОВ ДЛЯ ДЗ ---
        
        # 1. Дата расчёта — 1-е число месяца
        ("Дюна 2", 800.0, datetime(2026, 10, 1), 600.0, 
         "Граничный случай: 1-е число месяца"),
         
        # 2. Дата расчёта — последний день месяца
        ("Форсаж 10", 700.0, datetime(2026, 10, 31), 525.0, 
         "Граничный случай: Последний день месяца"),
         
        # 3. Товар с нулевой ценой
        ("Барби", 0.0, datetime(2026, 10, 15), 0.0, 
         "Граничный случай: Нулевая цена билета"),
         
        # 4. Товар с отрицательными данными
        ("Дюна 2", -100.0, datetime(2026, 10, 15), -75.0, 
         "Граничный случай: Отрицательная стоимость"),
         
        # 5. Заказы только в позапрошлом месяце
        ("Барби", 600.0, datetime(2026, 10, 15), 450.0, 
         "Граничный случай: Заказы только в позапрошлом месяце")
    ]

    print("\nЗапуск домашних граничных тестов...")
    print("-" * 80)
    
    passed_count = 0
    for name, price, date, expected, comment in test_cases:
        result = calculate_price_with_discount(name, price, date)
        
        is_ok = abs(result - expected) < 0.01
        status = "✅" if is_ok else "❌"
        
        if is_ok:
            passed_count += 1
            
        print(f"{status} Фильм '{name}' на {date.date()}: {price} руб. -> "
              f"Получено: {result} руб. (Ожидалось: {expected}) — {comment}")
    
    print("-" * 80)
    print_test_report(passed_count, len(test_cases))


# Вызов функции пишется без отступов с самого начала строки
if __name__ == "__main__":
    run_homework_tests()
