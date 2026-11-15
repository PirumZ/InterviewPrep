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
        1: add,
        2: subtract,
        3: divide,
        4: multiply,
        5: exit
    }

    while running:

        choice = -1

        while choice not in operations:
            try:
                choice = int(input('What operation would you like to compute?\n'
                               '1. Addition\n'
                               '2. Subtraction\n'
                               '3. Division\n'
                               '4. Multiplication\n'
                               '5. Exit\n'))

            except ValueError:
                print("Please print a valid integer in range.\n")
                continue

        if operations[choice] == exit:
            running = False
            break

        a, b = get_operands()

        if operations[choice] == divide:
            b = validate_divide_by_0(b)

        print(operations[choice](a, b))