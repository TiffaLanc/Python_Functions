#Objective: The aim of this assignment is to build a basic calculator that can perform addition, subtraction, multiplication and division.

#Task 1 Create functions for each arithmetic operation

def add(num1, num2):
    return num1 + num2 

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    if num2 == 0:
        return "Error, division by zero not allowed"
    return num1 / num2

print("Please select an operation \n"\
            "1. Add\n"\
            "2. Subtrct\n"\
            "3. Multiply\n"\
            "4. Divide\n")


#Task 2 Use inputs to ask the user what operation they want to perform and what numbers they want to use. 


operation = int(input("Please select an operation (1, 2, 3 or 4): "))

number_1 = int(input("Please select the first number you would like to use: "))
number_2 = int(input("Please select the second number you would like to use: "))




#Task 3 Ensure your code can handle division by zero and other potential erros. So if you divide by zero, there is error handling set up to prevent an error
#  from showoing in the console.



if operation == 1:
        print(number_1, "+", number_2, "=", 
            add(number_1, number_2))

elif operation == 2:
        print(number_1, "-", number_2, "=",
            subtract(number_1, number_2))  

elif operation == 3:
        print(number_1, "*", number_2, "=",
            multiply(number_1, number_2)) 
    
elif operation == 4:
        print(number_1, "/", number_2, "=",
            divide(number_1, number_2)) 
    
else:
        print("Error: Invalid input.")
