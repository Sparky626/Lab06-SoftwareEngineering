def menu():
    print("Menu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")

def encode():
    password = input("Please enter your password to encode: ")
    old_password = password
    for i in range(0, len(password)):
        int_changer = int(password[i])
        int_changer += 3
        password[i] = str(int_changer)
    print("Your password has been encoded and stored!")
    print(" ")
    return password

def decode(password):
    new_password = password
    for i in range(0, len(password)):
        int_changer = int(password[i])
        int_changer -= 3
        password[i] = str(int_changer)
    print("The encoded password is " + new_password + " , and the original password is " + password + ".")


def main():
    menu()
    password = None
    choice = int(input("Please enter an option: "))
    program_active = True
    while program_active:
        if choice == 1:
            password = encode()
        elif choice == 2:
            decode(password)
        else:
            program_active = False

if __name__ == "__main__":
    main()

