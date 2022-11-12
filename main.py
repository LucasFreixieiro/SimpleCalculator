import numpy as np
import numexpr as ne
QUIT = "x"
HELP = "help"
expression = ""

def help():
    print("Supported Operations:")
    print("Sum: +")
    print("Subtration: -")
    print("Multiplication: *")
    print("Division: /")
    print("Percentage: %")
    print("Exponent: ** or ^")
    print("Square root: sqrt(number)")
    print("Letters are not supported")

print("Help command>", HELP)
help()
while(expression != QUIT):
    expression = input("Calculator>")
    if(expression != QUIT):
        try:
            exp = expression.replace("^", "**")
            print(expression, "=", ne.evaluate(exp))
        except:
            print("Invalid Expression. Try again!")

    if(expression == HELP):
        help()

print("Closing...")