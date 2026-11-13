def get_operands():
    a = input("Please input a value for A: ") #clean up text
    a = validate_float(a)

    b = input("Please input a value for B: ") #clean up text
    b = validate_float(b)
    return a, b

def validate_float(num):
    while True:
        try:
            num = float(num)
            break
        except ValueError:
            num = input("Please enter a valid number: ")
    return num


def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by 0")
    else:
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

        while choice < 1 or choice > len(operations):
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

        print(operations[choice](a, b))