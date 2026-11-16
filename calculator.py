def get_operands():
    a = validate_float(input("Please input a value for A: "))
    b = validate_float(input("Please input a value for B: "))
    return a, b

def validate_float(num):
    while True:
        try:
            return float(num)
        except ValueError:
            num = input("Please enter a valid number: ")

def perform_math(operations):
    expression = input("Expression: ")
    pieces = expression.split(" ")
    total = validate_float(pieces[0])
    for piece in pieces[1:]:
        if piece in operations:
            operation = piece
        elif piece not in operations:
            operand = validate_float(piece)
            total = operations[operation](total, operand)
    print(total)


def add(a, b):
    return a + b

def subtract(a, b):
    return a - b


def validate_divide_by_0(b):
    while True:
        if b == 0:
           print("Cannot divide by 0.")
           b = validate_float(input("Please enter a valid number: "))
        else:
            return b

def divide(a, b):
    return a / b

def multiply(a, b):
    return a * b


if __name__ == "__main__":
    running = True

    operations = {
        "+": add,
        "-": subtract,
        "/": divide,
        "*": multiply
    }
    choices = {
        1: "Math",
        2: exit
    }

    while running:
        choice = -1
        while choice not in choices:
            try:
                choice = int(input('\n'
                               '1. Perform math\n'
                               '2. Exit\n'))

            except ValueError:
                print("Please print a valid integer in range.\n")
                continue

        if choices[choice] == exit:
            running = False
            break

        elif choices[choice] == "Math":
            perform_math(operations)
