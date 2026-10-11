class Calculator:
    """Класс, реализующий основные арифметические операции."""

    @staticmethod
    def add(a: float, b: float) -> float:
        """Сложение."""
        return a + b

    @staticmethod
    def subtract(a: float, b: float) -> float:
        """Вычитание."""
        return a - b

    @staticmethod
    def multiply(a: float, b: float) -> float:
        """Умножение."""
        return a * b

    @staticmethod
    def divide(a: float, b: float) -> float:
        """Деление с проверкой на ноль."""
        if b == 0:
            raise ValueError("Деление на ноль невозможно")
        return a / b

    @staticmethod
    def power(a: float, b: float) -> float:
        """Возведение в степень."""
        return a ** b

    @staticmethod
    def sqrt(a: float) -> float:
        """Квадратный корень."""
        if a < 0:
            raise ValueError("Нельзя извлечь корень из отрицательного числа")
        return a ** 0.5


def main() -> None:
    """Простой CLI-интерфейс калькулятора."""
    calc = Calculator()

    print("=== Калькулятор ===")
    print("Операции: +, -, *, /, **, sqrt")
    print("Для выхода введите 'q'\n")

    while True:
        op = input("Введите операцию: ").strip()

        if op.lower() == "q":
            print("Выход.")
            break

        try:
            if op == "sqrt":
                a = float(input("Число: "))
                print(f"Результат: {calc.sqrt(a)}")
            elif op in ("+", "-", "*", "/", "**"):
                a = float(input("Первое число: "))
                b = float(input("Второе число: "))
                operations = {
                    "+": calc.add,
                    "-": calc.subtract,
                    "*": calc.multiply,
                    "/": calc.divide,
                    "**": calc.power,
                }
                print(f"Результат: {operations[op](a, b)}")
            else:
                print("Неизвестная операция")
        except ValueError as e:
            print(f"Ошибка: {e}")


if __name__ == "__main__":
    main()
