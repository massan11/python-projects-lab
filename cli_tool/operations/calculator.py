import sys 

def calculate(operation: str, num1: float, num2: float) -> float:
    '''Perform basic arithmetic operations on two numbers.'''
    try:
        if operation == "add":
            return num1 + num2
        elif operation == "subtract":
            return num1 - num2
        elif operation == "multiply":
            return num1 * num2
        elif operation == "divide":
            if num2 == 0:
                print("Error: Division by zero.")
                sys.exit(1)
            return num1 / num2
        else:
            print(f"Error: unknown operation {operation}")
            sys.exit(1)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)
        