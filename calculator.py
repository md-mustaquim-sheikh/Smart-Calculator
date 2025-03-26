print("""
      Enter '+' for addition
      Enter '-' for subtraction
      Enter '*' for multiplication
      Enter '/' for division
      Enter '%' for remainder
      Enter 'x' or 'X' to exit
     """)

while True:
    op = input("Enter Operator: ")

    if op in ('+', '-', '*', '/', '%'):  
        num1 = float(input("Enter first number: ")) 
        num2 = float(input("Enter second number: "))

        if op == "+":
            print("Result:", num1 + num2)
        elif op == "-":
            print("Result:", num1 - num2)
        elif op == "*":
            print("Result:", num1 * num2)
        elif op == "/":
            if num2 != 0:
                print("Result:", num1 / num2)
            else:
                print("Error: Cannot divide by zero")
        elif op == "%":
            if num2 != 0:
                print("Result:", num1 % num2)
            else:
                print("Error: Cannot find remainder with zero")

    elif op in ('x', 'X'):
        print("Exiting the calculator. Goodbye!")
        break
    else:
        print("Invalid operator. Please enter a valid operator.")
