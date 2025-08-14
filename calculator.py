# PLP-python-week-1-assignment-
This is my solution for the week 1 assignment 
#Basic Calculator Program
#Get user inputs
num1 = float(input("Enter the first number"))
num2 = float(input("Enter the second number"))
operation = input("Enter operation (+,-,*,/)

# Perform the calculation
if operation == "+":
    result = num1 +num2 
elif operaton == "-":
    result = num1 - num2 
elif operation =="*"
    result = num1 * num2 
elif operation == "/":
if num2 != 0:
    result = num1 / num2 
else:
    result = "Error! Division by zero."
else:
    result = "Invalid operation."

 # Display the result
 if instance(result, (int, float)):
    print(f"{num1}{operation{num2}={result}")
else:
    print(result)


    
