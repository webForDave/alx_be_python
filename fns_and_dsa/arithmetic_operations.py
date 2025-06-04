def perform_operation(num1, num2, operation):
    if num2 == 0:
        return "Cannot divide by zero"
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == '/':
        return num1 / num2

