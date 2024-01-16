import art

print(art.logo)
f_input = input("What's the first number?: ")

def switch(f_input, s_input, operator):
    if operator == "+":
        result = f_input + s_input
    elif operator == "-":
        result = f_input - s_input
    elif operator == "*":
        result = f_input * s_input
    elif operator == "/":
        result = f_input / s_input
    return result

def calculator(f_input):
    print("+\n-\n*\n/\n")
    operator = input("Pick an operation: ")
    s_input = input("What's the next number?: ")

    f_num = float(f_input)
    s_num = float(s_input)
    result = switch(f_num, s_num, operator)

    print(f"{f_num} {operator} {s_num} = {result}")
    toContinue = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ").lower()

    if toContinue == "y":
        calculator(result)

calculator(f_input)