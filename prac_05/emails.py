def extract_name(email):
    username = email.split('@')[0]
    parts = username.split('.')
    name = ' '.join(parts).title()
    return name


def main():
    user_data = {}
    email = input("Email: ")
    while email:
        name = extract_name(email)
        confirmation = input(f"Is your name {name}? (Y/n) ").strip().lower()
        if confirmation in ('', 'y', 'yes'):
            user_data[email] = name
        else:
            name = input("Name: ")
            user_data[email] = name
        email = input("Email: ")

    print("Name: Email")
    for email, name in user_data.items():
        print(f"{name} ({email})")


main()

