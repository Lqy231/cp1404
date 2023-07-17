
MINIMUM_LENGTH = 8

def main():
    password = get_password()

    while len(password) < MINIMUM_LENGTH : 
        print(f"error input")
        password = get_password()

    print_asterisk(password)


def print_asterisk(password):
    print("*" * len(password))


def get_password():
    password = input("password: ")
    return password