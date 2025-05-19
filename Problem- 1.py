class Calculator:
    def __init__(self, a, b):
        self.a = float(a)
        self.b = float(b)

    def calculate(self, operation):
        if operation == 'add':
            return self.a + self.b
        elif operation == 'subtract':
            return self.a - self.b
        elif operation == 'multiply':
            return self.a * self.b
        elif operation == 'divide':
            if self.b != 0:
                return self.a / self.b
            else:
                return "Division by zero error"
        else:
            return "Invalid operation"

# Example usage
calc = Calculator(20, 4)
print("Addition:", calc.calculate('add'))
print("Subtraction:", calc.calculate('subtract'))
print("Multiplication:", calc.calculate('multiply'))
print("Division:", calc.calculate('divide'))
