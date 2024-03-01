# Task 1: Writing user's name to a file
name = input("Enter your name: ")
with open('name.txt', 'w') as file:
    file.write(name)

# Task 2: Reading name from the file and printing it
with open('name.txt', 'r') as file:
    name = file.read().strip()
    print(f"Your name is {name}")

# Task 3: Reading first two numbers from "numbers.txt" and adding them
with open('numbers.txt', 'r') as file:
    num1 = int(file.readline())
    num2 = int(file.readline())
    total = num1 + num2
    print("Total of first two numbers:", total)

# Task 4: Reading all numbers from "numbers.txt" and calculating total
total = 0
with open('numbers.txt', 'r') as file:
    for line in file:
        total += int(line)
print("Total of all numbers:", total)