def calculator():
    print("=== Basic Calculator ===")
    try:
        num1 = float(input("Enter first number: "))
        op = input("Choose operation (+, -, *, /): ")
        num2 = float(input("Enter second number: "))

        match op:
            case '+':
                result = num1 + num2
            case '-':
                result = num1 - num2
            case '*':
                result = num1 * num2
            case '/':
                result = num1 / num2 if num2 != 0 else "Cannot divide by zero"
            case _:
                result = "Invalid operator"
        print(f"Result: {result}")
    except ValueError:
        print("Invalid input! Use numeric values.")

calculator()
