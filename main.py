import sympy as sp

class DerivativeCalculator:
    """
    Калькулятор для вычисления обычных и смешанных производных
    """
    
    def __init__(self):
        # Создаем символы для переменных x, y, z
        # Символы - это как переменные в математике, с которыми можно работать
        self.x = sp.Symbol('x')
        self.y = sp.Symbol('y')
        self.z = sp.Symbol('z')
    
    def calculate_simple_derivative(self, expression, variable='x', order=1):
        """
        Вычисляет обычную производную функции одной переменной
        
        Аргументы:
            expression - математическое выражение в виде строки (например, "x**2 + 3*x")
            variable - переменная, по которой берем производную ('x', 'y' или 'z')
            order - порядок производной (1 - первая, 2 - вторая и т.д.)
        """
        print(f"\n=== Вычисление {order}-й производной по {variable} ===")
        print(f"Функция: f({variable}) = {expression}")
        
        try:
            # Шаг 1: Преобразуем строку в математическое выражение
            # sympify понимает математические выражения из строк
            math_expr = sp.sympify(expression)
            print(f"✓ Преобразовано в математическое выражение: {math_expr}")
            
            # Шаг 2: Выбираем переменную для дифференцирования
            if variable == 'x':
                var = self.x
            elif variable == 'y':
                var = self.y
            else:
                var = self.z
            
            # Шаг 3: Вычисляем производную
            # diff вычисляет производную: первый аргумент - выражение, 
            # второй - переменная, третий - порядок
            derivative = sp.diff(math_expr, var, order)
            print(f"✓ Вычислена производная: {derivative}")
            
            # Шаг 4: Упрощаем результат (если возможно)
            simplified = sp.simplify(derivative)
            print(f"✓ Упрощенная форма: {simplified}")
            
            return math_expr, derivative, simplified
            
        except Exception as error:
            print(f"✗ Ошибка: {error}")
            return None, None, None
    
    def calculate_mixed_derivative(self, expression, variables, orders):
        """
        Вычисляет смешанную производную функции нескольких переменных
        
        Аргументы:
            expression - математическое выражение (например, "x**2 * y**3")
            variables - список переменных ['x', 'y'] 
            orders - список порядков [1, 2] (производная по x 1-го порядка, по y 2-го порядка)
        """
        print(f"\n=== Вычисление смешанной производной ===")
        print(f"Функция: f({', '.join(variables)}) = {expression}")
        print(f"Порядки производных: {list(zip(variables, orders))}")
        
        try:
            # Шаг 1: Преобразуем строку в математическое выражение
            math_expr = sp.sympify(expression)
            print(f"✓ Преобразовано в математическое выражение: {math_expr}")
            
            # Шаг 2: Начинаем с исходного выражения
            current_expr = math_expr
            steps = []  # Будем хранить шаги вычислений
            
            # Шаг 3: Последовательно вычисляем производные по каждой переменной
            for i, (var_name, order) in enumerate(zip(variables, orders)):
                # Выбираем символ переменной
                if var_name == 'x':
                    var = self.x
                elif var_name == 'y':
                    var = self.y
                else:
                    var = self.z
                
                # Вычисляем производную нужного порядка
                current_expr = sp.diff(current_expr, var, order)
                
                # Запоминаем шаг
                step_desc = f"∂^{order}f/∂{var_name}^{order}"
                steps.append((step_desc, current_expr))
                print(f"✓ Шаг {i+1}: {step_desc} = {current_expr}")
            
            # Шаг 4: Упрощаем финальный результат
            final_result = sp.simplify(current_expr)
            print(f"✓ Финальный упрощенный результат: {final_result}")
            
            return math_expr, steps, final_result
            
        except Exception as error:
            print(f"✗ Ошибка: {error}")
            return None, [], None
    
    def evaluate_at_point(self, expression, point_values):
        """
        Вычисляет значение выражения в заданной точке
        
        Аргументы:
            expression - математическое выражение
            point_values - словарь с значениями переменных {'x': 2, 'y': 3}
        """
        print(f"\n--- Вычисление значения в точке {point_values} ---")
        
        try:
            # Создаем словарь для подстановки: {символ: значение}
            substitutions = {}
            if 'x' in point_values:
                substitutions[self.x] = point_values['x']
            if 'y' in point_values:
                substitutions[self.y] = point_values['y']
            if 'z' in point_values:
                substitutions[self.z] = point_values['z']
            
            # Подставляем значения и вычисляем
            value = expression.subs(substitutions)
            print(f"✓ Выражение: {expression}")
            print(f"✓ После подстановки {point_values}: {value}")
            
            # Если результат - число, показываем его численное значение
            if value.is_number:
                print(f"✓ Численное значение: {float(value):.4f}")
            
            return value
            
        except Exception as error:
            print(f"✗ Ошибка вычисления: {error}")
            return None

def main():
    """
    Главная функция программы - взаимодействие с пользователем
    """
    # Создаем экземпляр калькулятора
    calculator = DerivativeCalculator()
    
    print("🎯 КАЛЬКУЛЯТОР ПРОИЗВОДНЫХ")
    print("=" * 50)
    
    # Примеры для демонстрации
    examples = [
        {"type": "simple", "func": "x**2 + 3*x + 5", "var": "x", "order": 1, "desc": "Квадратичная функция"},
        {"type": "simple", "func": "sin(x)", "var": "x", "order": 1, "desc": "Синус"},
        {"type": "mixed", "func": "x**2 * y**3", "vars": ["x", "y"], "orders": [1, 1], "desc": "Смешанная производная x²y³"},
        {"type": "mixed", "func": "sin(x)*cos(y)", "vars": ["x", "y"], "orders": [1, 1], "desc": "Смешанная производная sin(x)cos(y)"},
    ]
    
    while True:
        print("\n" + "="*50)
        print("ВЫБЕРИТЕ ДЕЙСТВИЕ:")
        print("1 - Вычислить обычную производную")
        print("2 - Вычислить смешанную производную")
        print("3 - Показать примеры")
        print("4 - Выйти из программы")
        
        choice = input("Ваш выбор (1-4): ").strip()
        
        if choice == '1':
            # Режим обычной производной
            print("\n--- ОБЫЧНАЯ ПРОИЗВОДНАЯ ---")
            expression = input("Введите функцию (например, x**2 + sin(x)): ").strip()
            variable = input("По какой переменной дифференцируем? (x/y/z, по умолчанию x): ").strip()
            if not variable:
                variable = 'x'
            
            try:
                order = int(input("Порядок производной (1, 2, 3...): ").strip() or "1")
            except:
                order = 1
                print("Используем порядок 1 по умолчанию")
            
            # Вычисляем производную
            original, derivative, simplified = calculator.calculate_simple_derivative(
                expression, variable, order
            )
            
            # Если вычисление успешно, предлагаем вычислить значение в точке
            if original is not None:
                calc_point = input("Вычислить значение в точке? (y/n): ").strip().lower()
                if calc_point == 'y':
                    try:
                        point_val = float(input(f"Введите значение {variable} = ").strip())
                        calculator.evaluate_at_point(simplified, {variable: point_val})
                    except:
                        print("Некорректное значение точки")
        
        elif choice == '2':
            # Режим смешанной производной
            print("\n--- СМЕШАННАЯ ПРОИЗВОДНАЯ ---")
            expression = input("Введите функцию нескольких переменных (например, x**2 * y**3): ").strip()
            
            # Получаем переменные
            vars_input = input("Введите переменные через запятую (например, x,y): ").strip()
            variables = [v.strip() for v in vars_input.split(',') if v.strip()]
            
            # Получаем порядки производных
            orders = []
            print("Введите порядки производных для каждой переменной:")
            for var in variables:
                try:
                    order = int(input(f"Порядок для {var}: ").strip() or "1")
                    orders.append(order)
                except:
                    orders.append(1)
                    print(f"Используем порядок 1 для {var}")
            
            # Вычисляем смешанную производную
            original, steps, result = calculator.calculate_mixed_derivative(
                expression, variables, orders
            )
            
            # Предлагаем вычислить значение в точке
            if original is not None:
                calc_point = input("Вычислить значение в точке? (y/n): ").strip().lower()
                if calc_point == 'y':
                    point_vals = {}
                    for var in variables:
                        try:
                            val = float(input(f"Введите значение {var} = ").strip())
                            point_vals[var] = val
                        except:
                            print(f"Некорректное значение для {var}, пропускаем")
                    if point_vals:
                        calculator.evaluate_at_point(result, point_vals)
        
        elif choice == '3':
            # Показываем примеры
            print("\n--- ПРИМЕРЫ ---")
            for i, example in enumerate(examples, 1):
                print(f"\n{i}. {example['desc']}")
                if example['type'] == 'simple':
                    original, derivative, simplified = calculator.calculate_simple_derivative(
                        example['func'], example['var'], example['order']
                    )
                else:
                    original, steps, result = calculator.calculate_mixed_derivative(
                        example['func'], example['vars'], example['orders']
                    )
        
        elif choice == '4':
            print("До свидания! 👋")
            break
        
        else:
            print("❌ Неверный выбор! Попробуйте снова.")

# Точка входа в программу
if __name__ == "__main__":
    main()