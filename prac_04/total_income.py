def main():
    """Display income report for incomes over a given number of months."""
    incomes = []
    num_months = int(input("How many months? "))  # Renamed variable for clarity

    for month in range(1, num_months + 1):
        income = float(input(f"Enter income for month {month}: "))  # f-string used
        incomes.append(income)

    print_income_report(incomes, num_months)  # Separate function for printing the report


def print_income_report(incomes, num_months):
    """Print the income report given a list of incomes."""
    print("\nIncome Report\n-------------")
    total = 0
    for month in range(1, num_months + 1):
        income = incomes[month - 1]
        total += income
        print(f"Month {month:2} - Income: ${income:10.2f}         Total: ${total:10.2f}")


main()
