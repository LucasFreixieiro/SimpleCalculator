import numpy as np
import numexpr as ne
import warnings
warnings.filterwarnings("error")

QUIT = "exit" # Command to close programme
HELP = "help" # Command to open help information
expression = "" # User expression

def help():
    """
    Basic usage information about the software
    """
    print("Supported Operations:")
    print("Sum: +")
    print("Subtration: -")
    print("Multiplication: *")
    print("Division: /")
    print("Modulus: %")
    print("Exponent: ** or ^")
    print("Square root: sqrt(number)")
    print("Letters are not supported")
    print(QUIT, "to exit")

print("Help command>", HELP) 
help()
while(expression != QUIT):
    expression = input("Calculator>")
    if(expression != QUIT):
        try:
            exp = expression.replace("^", "**") # replace ^ to ** so numexpr library can evaluate expression
            print(expression, "=", ne.evaluate(exp)) # numexpr library will evaluate the user expression and return the operation result
        except ZeroDivisionError: # if the expression contains invalid operators or is a invalid expression it'll be shown a error message to the user
            print("Can't divide a value by 0. Try again!")
        except RuntimeWarning:
            print("Invalid Expression. Try again!")
        except:
            print("Invalid Expression. Try again!")

    if(expression == HELP):
        help()

print("Closing...")