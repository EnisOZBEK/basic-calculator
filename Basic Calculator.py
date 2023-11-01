def addition(a, b):
    result = a + b
    print(result)

def subtraction(a, b):
    result = a - b
    print(result)

def multiplication(a, b):
    result = a * b
    print(result)

def divison(a, b):
    result = a / b
    print(result)

def fulldivision(a, b):
    result = a // b
    print(result)

def exponentiate(a, b):
    result = a ** b
    print(result)

def mod(a, b):
    result = a % b
    print(result)

again = "y"

while again == "y":
    a=float(input("Enter the first number: "))
    b=float(input("Enter the second number: "))
    operator=input("Enter the operator(+,-,*,/,//,**): ")

    if operator == "+":
        addition(a, b)
        again = input("Do you want to calculate again ? (y, n): ")

        if again == "n":
            print("Thanks for using our service!")
        
    elif operator == "-":
        subtraction(a, b)
        again = input("Do you want to calculate again ? (y, n): ")

        if again == "n":
            print("Thanks for using our service!")        

    elif operator == "*":
        multiplication(a, b)
        again = input("Do you want to calculate again ? (y, n): ")

        if again == "n":
            print("Thanks for using our service!")    

    elif operator == "/":
        divison(a, b)
        again = input("Do you want to calculate again ? (y, n): ")

        if again == "n":
            print("Thanks for using our service!")       

    elif operator == "//":
        fulldivision(a, b)
        again = input("Do you want to calculate again ? (y, n): ")

        if again == "n":
            print("Thanks for using our service!")        

    elif operator == "**":
        exponentiate(a, b)
        again = input("Do you want to calculate again ? (y, n): ")

        if again == "n":
            print("Thanks for using our service!")

    elif operator == "%":
        mod(a ,b)
        again = input("Do you want to calculate again ? (y, n): ")

        if again == "n":
            print("Thanks for using our service!")

    else:
        print("İnvalid Operator")
        again = input("Do you want to calculate again ? (y, n): ")

        if again == "n":
            print("Thanks for using our service!")        