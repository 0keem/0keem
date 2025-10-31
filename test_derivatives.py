"""
ТЕСТОВЫЙ ФАЙЛ для калькулятора производных
Этот файл проверяет, что программа работает правильно
"""

import sympy as sp
from main import DerivativeCalculator  # Импортируем наш калькулятор из main.py

def run_all_tests():
    """
    Запускает все тесты для калькулятора производных
    """
    print("🧪 ЗАПУСК ТЕСТОВ КАЛЬКУЛЯТОРА ПРОИЗВОДНЫХ")
    print("=" * 60)
    
    # Создаем калькулятор для тестирования
    calc = DerivativeCalculator()
    
    # Тест 1: Простые производные
    print("\n1. ТЕСТИРУЕМ ПРОСТЫЕ ПРОИЗВОДНЫЕ:")
    print("-" * 40)
    
    # Список тестов: (функция, переменная, порядок, ожидаемый результат)
    test_cases = [
        # (функция, переменная, порядок, что должно получиться)
        ("x**2", "x", 1, "2*x"),           # Производная x² = 2x
        ("x**3", "x", 2, "6*x"),           # Вторая производная x³ = 6x
        ("sin(x)", "x", 1, "cos(x)"),      # Производная sin(x) = cos(x)
        ("cos(x)", "x", 1, "-sin(x)"),     # Производная cos(x) = -sin(x)
        ("exp(x)", "x", 1, "exp(x)"),      # Производная e^x = e^x
        ("log(x)", "x", 1, "1/x"),         # Производная ln(x) = 1/x
    ]
    
    passed_tests = 0  # Счетчик пройденных тестов
    
    for i, (func, var, order, expected) in enumerate(test_cases, 1):
        print(f"\nТест {i}: d({func})/d{var}^{order}")
        print(f"Ожидаем: {expected}")
        
        # Вызываем наш калькулятор
        original, derivative, simplified = calc.calculate_simple_derivative(func, var, order)
        
        # Преобразуем ожидаемый результат в символьное выражение
        expected_expr = sp.sympify(expected)
        
        # Проверяем, совпадает ли результат с ожидаемым
        if simplified == expected_expr:
            print("✅ ТЕСТ ПРОЙДЕН")
            passed_tests += 1
        else:
            print(f"❌ ТЕСТ НЕ ПРОЙДЕН")
            print(f"   Получили: {simplified}")
    
    # Тест 2: Смешанные производные
    print("\n\n2. ТЕСТИРУЕМ СМЕШАННЫЕ ПРОИЗВОДНЫЕ:")
    print("-" * 40)
    
    mixed_test_cases = [
        # (функция, переменные, порядки, ожидаемый результат)
        ("x**2 * y**3", ["x", "y"], [1, 1], "6*x*y**2"),  # ∂²/∂x∂y (x²y³) = 6xy²
        ("x*y + y**2", ["x", "y"], [1, 1], "1"),          # ∂²/∂x∂y (xy + y²) = 1
        ("sin(x)*cos(y)", ["x", "y"], [1, 1], "-sin(x)*sin(y)"),  # ∂²/∂x∂y (sin(x)cos(y))
    ]
    
    for i, (func, vars, orders, expected) in enumerate(mixed_test_cases, 1):
        print(f"\nТест {i}: смешанная производная {func}")
        print(f"По переменным: {vars} с порядками: {orders}")
        print(f"Ожидаем: {expected}")
        
        # Вызываем калькулятор для смешанных производных
        original, steps, result = calc.calculate_mixed_derivative(func, vars, orders)
        
        # Преобразуем ожидаемый результат
        expected_expr = sp.sympify(expected)
        
        # Проверяем результат
        if result == expected_expr:
            print("✅ ТЕСТ ПРОЙДЕН")
            passed_tests += 1
        else:
            print(f"❌ ТЕСТ НЕ ПРОЙДЕН")
            print(f"   Получили: {result}")
    
    # Тест 3: Вычисление в точках
    print("\n\n3. ТЕСТИРУЕМ ВЫЧИСЛЕНИЕ В ТОЧКАХ:")
    print("-" * 40)
    
    # Берем производную x² (должна быть 2x)
    original, derivative, simplified = calc.calculate_simple_derivative("x**2", "x", 1)
    
    # Вычисляем в точке x=3 (должно быть 2*3 = 6)
    print("Тест: вычисление производной x² в точке x=3")
    value = calc.evaluate_at_point(simplified, {'x': 3})
    
    if value == 6:
        print("✅ ТЕСТ ПРОЙДЕН: 2*3 = 6")
        passed_tests += 1
    else:
        print(f"❌ ТЕСТ НЕ ПРОЙДЕН: получили {value}, ожидали 6")
    
    # Итоги тестирования
    total_tests = len(test_cases) + len(mixed_test_cases) + 1
    print("\n" + "=" * 60)
    print(f"ИТОГИ ТЕСТИРОВАНИЯ:")
    print(f"Пройдено тестов: {passed_tests} из {total_tests}")
    
    if passed_tests == total_tests:
        print("🎉 ВСЕ ТЕСТЫ ПРОЙДЕНЫ УСПЕШНО!")
    else:
        print("⚠️  НЕКОТОРЫЕ ТЕСТЫ НЕ ПРОЙДЕНЫ")
    
    print("=" * 60)

# Этот код выполнится только если файл запущен напрямую
if __name__ == "__main__":
    run_all_tests()