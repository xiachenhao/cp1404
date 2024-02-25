def main():
    score = get_valid_score()
    choice = ""
    while choice != "Q":
        print("\nMenu:")
        print("(P)rint result")
        print("(S)how stars")
        print("(Q)uit")
        choice = input(">>> ").upper()
        if choice == "P":
            print_result(score)
        elif choice == "S":
            show_stars(score)
        elif choice != "Q":
            print("Invalid input. Please try again.")
    print("Goodbye!")


def calculate_score_result(score):
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


def get_valid_score():
    score = -1
    while score < 0 or score > 100:
        score_input = input("Enter a score (0-100 inclusive): ")
        if score_input.isdigit():
            score = float(score_input)
            if 0 <= score <= 100:
                return score
        print("Invalid score. Please enter a score between 0 and 100 inclusive.")


def print_result(score):
    print("Result:", calculate_score_result(score))


def show_stars(score):
    print("Stars:", "*" * int(score))


main()
