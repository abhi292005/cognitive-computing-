def divide_numbers():
    try:
        numerator = float(input("Enter the numerator: "))
        denominator = float(input("Enter the denominator: "))
        result = numerator / denominator
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
    else:
        print(f"The result of {numerator} divided by {denominator} is {result}.")

divide_numbers()
#8.2
def get_number():
    while True:
        try:
            number = float(input("Enter a number: "))
            print(f"You entered: {number}")
            break  
        except ValueError:
            print("Invalid input. Please enter a valid number.")

get_number()
#8.3
def file_operations():
    try:
        file = open("example.txt", "r")
        content = file.read()
        print(content)
    except FileNotFoundError:
        print("Error: The file does not exist.")
    finally:
        
        print("Execution of file operations is complete.")
        try:
            file.close()
        except NameError:
            print("File was never opened, so no need to close it.")

file_operations()