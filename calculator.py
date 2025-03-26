print("""
      Enter '+' for add
      Enter '-' for substract
      Enter '*' for multiply
      Enter '/' for division
      Enter '%' for remainder
      Enter 'x' or 'X' to exit
     """)
while(True):
    op = input("Enter Operator :")
    if (op=='+'or op=='-' or op=='*' or op=='/'):
        num1 = int(input("Enter first number :"))
        num2 = int(input("Enter second number :"))
        if (op=="+"):
            print(num1+num2)
        elif (op=="-"):
            print(num1-num2)
        elif (op=="*"):
            print(num1*num2)
        elif (op=="/"):
            if(num2!=0):
                print(num1/num2)
            else:
                print("Number cannot divided by zero")
        elif (op=="%"):
            print(num1%num2)
        
    else:
        print("Invalid operator")
    if(op=='x'or op=='X'):
        break