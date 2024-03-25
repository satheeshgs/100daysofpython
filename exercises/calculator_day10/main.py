#calculator
from clear import clearscreen
from art import logo
#add
def add(n1, n2):
    return n1 + n2

#subtract
def subtract(n1, n2):
    return n1 - n2

#multiply
def multiply(n1, n2):
    return n1 * n2

#divide
def divide(n1, n2):
    if n2 == 0:
        return "Can't divide by zero"
    else:
        return n1 / n2
    
operations = {
    "+" : add, 
    "-" : subtract, 
    "*" : multiply, 
    "/" : divide
}

def calculator():
    """This is a calculator function which takes two numbers and an operation as input 
    output is the mathematical operation on the two numbers"""
    print(logo)
    num1 = float(input("What is your first number?: "))
    num2 = float(input("what is your second number?: "))
    #for symbol in operations:
    #    print(symbol)

    operation_reqd = input("Pick an operation from the calculator: ")

    to_continue = 'y'
    while to_continue == 'y':
        function = operations[operation_reqd]
        answer = function(num1, num2)
        print(f"{num1} {operation_reqd} {num2} = {answer}")

        to_continue = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to exit, or 'r' to start a new calculation.: ")
        if to_continue == 'y':
            operation_reqd = input("Pick an operation from the line above: ")
            num1 = answer
            num2 = float(input("What's the next number?: "))
        elif to_continue == 'r':
            clearscreen()
            calculator()
        else: 
            clearscreen()


calculator()