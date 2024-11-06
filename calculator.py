# def add(x, y):
#     return x + y

# def subtract(x, y):
#     return x - y

# def multiply(x, y):
#     return x * y

# def divide(x, y):
#     if y == 0:
#         raise ValueError("Cannot divide by zero")
#     return x / y

# def calculator():
#     print("Select operation:")
#     print("1. Add")
#     print("2. Subtract")
#     print("3. Multiply")
#     print("4. Divide")
    
#     while True:
#         choice = input("Enter choice (1/2/3/4): ")
        
#         if choice in ['1', '2', '3', '4']:
#             try:
#                 num1 = float(input("Enter first number: "))
#                 num2 = float(input("Enter second number: "))
#             except ValueError:
#                 print("Invalid input! Please enter numeric values.")
#                 continue
            
#             if choice == '1':
#                 print(f"{num1} + {num2} = {add(num1, num2)}")
#             elif choice == '2':
#                 print(f"{num1} - {num2} = {subtract(num1, num2)}")
#             elif choice == '3':
#                 print(f"{num1} * {num2} = {multiply(num1, num2)}")
#             elif choice == '4':
#                 try:
#                     print(f"{num1} / {num2} = {divide(num1, num2)}")
#                 except ValueError as e:
#                     print(e)

#             # Ask if the user wants another calculation
#             next_calculation = input("Do you want to perform another calculation? (yes/no): ")
#             if next_calculation.lower() != 'yes':
#                 break
#         else:
#             print("Invalid Input")

# if __name__ == "__main__":
#     calculator()


import argparse

# Define the calculator functions
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        raise ValueError("Cannot divide by zero")
    return x / y

# Set up the argument parser
def parse_args():
    parser = argparse.ArgumentParser(description="Simple Calculator")
    parser.add_argument('operation', choices=['add', 'subtract', 'multiply', 'divide'], 
                        help="The operation to perform: add, subtract, multiply, or divide")
    parser.add_argument('num1', type=float, help="The first number")
    parser.add_argument('num2', type=float, help="The second number")
    
    return parser.parse_args()

def calculator():
    # Parse the command line arguments
    args = parse_args()

    # Perform the selected operation
    if args.operation == 'add':
        print(f"{args.num1} + {args.num2} = {add(args.num1, args.num2)}")
    elif args.operation == 'subtract':
        print(f"{args.num1} - {args.num2} = {subtract(args.num1, args.num2)}")
    elif args.operation == 'multiply':
        print(f"{args.num1} * {args.num2} = {multiply(args.num1, args.num2)}")
    elif args.operation == 'divide':
        try:
            print(f"{args.num1} / {args.num2} = {divide(args.num1, args.num2)}")
        except ValueError as e:
            print(e)

if __name__ == "__main__":
    calculator()
