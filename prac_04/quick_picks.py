import random

MIN_NUMBER = 1
MAX_NUMBER = 45
NUMBERS_PER_LINE = 6


def generate_quick_pick():
    return sorted(random.sample(range(MIN_NUMBER, MAX_NUMBER + 1), NUMBERS_PER_LINE))


def main():
    try:
        num_quick_picks = int(input("How many quick picks? "))
        for _ in range(num_quick_picks):
            quick_pick = generate_quick_pick()
            print(" ".join(f"{num:2d}" for num in quick_pick))
    except ValueError:
        print("Please enter a valid number.")


main()
