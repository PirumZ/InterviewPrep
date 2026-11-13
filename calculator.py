def get_operands():
    while True:
        try:
            a = float(input("Please input a value for A: ")) #clean up text
            break
        except ValueError:
            print("Please enter a floating number.")

    while True:
        try:
            b = float(input("Please input a value for B: ")) #clean up text
            break
        except ValueError:
            print("Please enter a floating number.")

    return a, b

#def validate_number(num, type):



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