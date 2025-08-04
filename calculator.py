# My Python Calculator Practice
# Trying out variables and user input

def simple_calc():
    print("Let's do some math!")
    print("Choose two numbers and an operation (+, -, *, /)")
    
    # Get numbers from user
    num1 = input("First number: ")
    num2 = input("Second number: ")
    
    # Check if inputs are numbers
    try:
        num1 = float(num1)
        num2 = float(num2)
    except:
        print("Please enter numbers only!")
        return
    
    # Get operation
    op = input("Operation (+, -, *, /): ")
    
    # Calculate based on operation
    if op == '+':
        result = num1 + num2
    elif op == '-':
        result = num1 - num2
    elif op == '*':
        result = num1 * num2
    elif op == '/':
        if num2 == 0:
            print("Can't divide by zero!")
            return
        result = num1 / num2
    else:
        print("Invalid operation")
        return
    
    # Show the calculation
    print(f"{num1} {op} {num2} = {result}")

# Run the calculator
while True:
    simple_calc()
    
    # Ask to continue
    again = input("Another calculation? (y/n): ")
    if again.lower() != 'y':
        print("Goodbye!")
        break