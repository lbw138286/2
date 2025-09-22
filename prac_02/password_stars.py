def main():
    password = get_password()
    print_asterisks(password)

def get_password():
    return input("Enter password: ")

def print_asterisks(password):
    print("*" * len(password))
main()