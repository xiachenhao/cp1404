import random


def main():
    user_score = float(input("Enter your score: "))
    print(calculate_score_result(user_score))

    # Generate a random score
    random_score = random.randint(0, 100)
    print("Random score:", random_score)
    print("Result:", calculate_score_result(random_score))


def calculate_score_result(score):
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


main()
