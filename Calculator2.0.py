# Create a new file called "calculator_2.0.py"
import math
# Create a class called "Calculator" that contains the following
class Calculator:

# Below is a method called "init" that initializes the dictionary with the basic mathematical operations 
# (+, -, *, /) and corresponding functions
    def __init__(self):
        self.operations = {
            "+" : self.add,
            "-" : self.subtract,
            "*" : self.multiply,
            "/" : self.divide
        }
# corresponding functions

    def add(self, a, b):
        return a + b
    def subtract(self, a, b):
        return a - b
    def multiply(self, a, b):
        return a * b
    def divide(self, a , b): 
        if b == 0:
            raise ValueError("Cannot divide by zero")
        else:
            return a / b
    

# A method called "add_operation" that takes in two arguments: 
# the operation symbol and the corresponding function. 
# This method should add the new operation and function to the dictionary.

    def add_operations(self, operational_symbol, function):
        self.operations[operational_symbol] = function

# A method called "calculate" that takes in three arguments: 
# the first number "a", the operation symbol, and the second number "b". 

    def calculate(self, a, operational_symbol, b=None):

# This method should use the dictionary to determine the appropriate function to perform the calculation. 
# It should also include error handling to check if the operation symbol is valid and if the input values are numbers. 
# If an error is encountered, the method should print an error message and raise an exception.
        if operational_symbol not in self.operations:
            raise ValueError (f" Invalid operational Symbol: {operational_symbol}")
        if not isinstance (a, (int, float)) or (b is not None and not isinstance(b, (int, float))) :
            raise ValueError ("Invalid input: You can only input numbers")
        if operational_symbol in ["sqrt", "log"]:
            return self.operations[operational_symbol](a)
        if not isinstance (b, (int, float)) and b is not None:
            raise ValueError("Invalid input: You can only input numbers")
        calculate_function = self.operations[operational_symbol]
        return calculate_function(a,b)
            
# Create separate functions for the advanced mathematical operations 
# (exponentiation, square root, logarithm) and use the 
# "add_operation" method to add them to the calculator's dictionary.

    def exponentiation (self, a, b): 
        return a ** b

    def square_root (self, a):
        if a >= 0:
            return math.sqrt (a)
        else: 
            raise ValueError ("Error: negative number not supported")
    def logarithm (self, a, base=10): 
        if a > 0:
            return math.log(a, base) 
        else: 
            raise ValueError("Error: Logarithm undefined for non-positive value")
    
# In the main program, create an instance of the Calculator class
if __name__ == "__main__":
    # Create a Calculator instance
    calc = Calculator()
     # Add advanced operations
    calc.add_operations("^", calc.exponentiation)
    calc.add_operations("sqrt", calc.square_root)
    calc.add_operations("log", calc.logarithm)

    print("Welcome to Calculator2.0 by Maki!")

# use a while loop that allows the user to continue performing calculations until they choose to exit.
# Use the input() function to get input from the user for the numbers and operation symbol.
# Use the math library for advanced mathematical operations
    while True:
        try:
            a = float(input("Enter the First Number: "))
            operational_symbol = input("Enter Operational Symbol (+, -, *, /, ^, sqrt, log): ")
            if operational_symbol in ("sqrt", "log"):
                result = calc.calculate(a, operational_symbol)
                print(f"The result is {round(result, 4)}")
            else:
                b = float(input("Enter the Second Number: "))
                result = calc.calculate(a, operational_symbol, b)
                print(f"the result is {round(result, 4)}")
        except:
            print("Invalid Operational Parameters entered")

        exit = input("Do you want to exit this calculator? (y/n): ").strip().lower()
        if exit == "y":
            print("Goodbye")
            break




                
            








    


    


        
   