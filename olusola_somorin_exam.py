# Question 1
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
        return a / b
    
while True:

    try:
        print()
        print("Calculator".center(20, "="))
        number1 = int(input("Enter first number: "))
        number2 = int(input("Enter second number: "))
        operation = input("Choose operation (+, -, *, /) or 'exit' to quit: ")

        if operation == "+":
            print(f"Result for {number1} + {number2}: {add(number1, number2)}")

        elif operation == "-":
            print(f"Result for {number1} - {number2}: {subtract(number1, number2)}")

        elif operation == "*":
            print(f"Result for {number1} * {number2}: {multiply(number1, number2)}")

        elif operation == "/":
            print(f"Result for {number1}/{number2}: {divide(number1, number2)}")

        elif operation == "exit":
            print("Exiting calculator... Goodbye!")
            break
        
        else:
            print("Invalid input!")

    except Exception as e:
        print("Error as", e)




# Question 2
while True:
    user_input = input("Enter a number (or type 'exit' to quit): ")
    if user_input == "exit":
        print("Goodbye!")
        break        # break out of loop
    
    num = int(user_input)   # convert to integer
    
    if num % 2 == 0:
        print("The number is even")
    else:
        print("The number is odd")




# Question 3
while True:
    age = input("Enter your age (or type exit to quit): ")
    if age == "exit":
        print("Goodbye!")
        break
    
    try:
        if int(age) >= 18:
            print("You can vote")
        else:
            print("You cannot vote")
    except:
        print("Invalid input")