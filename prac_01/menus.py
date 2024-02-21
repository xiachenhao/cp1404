def display_menu():
    print("(H)ello")
    print("(G)oodbye")
    print("(Q)uit")


def get_choice():
    return input(">>> ").upper()


def say_hello(name):
    print(f"Hello {name}")


def say_goodbye(name):
    print(f"Goodbye {name}")


def main():
    name = input("Enter name: ")
    display_menu()
    choice = get_choice()

    while choice != 'Q':
        if choice == 'H':
            say_hello(name)
        elif choice == 'G':
            say_goodbye(name)
        else:
            print("Invalid choice")
        display_menu()
        choice = get_choice()
    print("Finished.")

    main()
