# In guitar.py
class Guitar:
    """Represent a Guitar object."""

    def __init__(self, name="", year=0, cost=0):
        """Initialise a Guitar instance."""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return a string representation of the Guitar."""
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"

    def get_age(self, current_year):
        """Return the age of the guitar."""
        return current_year - self.year

    def is_vintage(self, current_year):
        """Return True if the guitar is vintage (50 or more years old), False otherwise."""
        return self.get_age(current_year) >= 50

    def __lt__(self, other):
        """Less than comparison based on guitar year."""
        return self.year < other.year

    # In guitars.py
    from guitar import Guitar

    def load_guitars(filename):
        """Load guitars from file."""
        guitars = []
        with open(filename, "r") as file:
            for line in file:
                name, year, cost = line.strip().split(",")
                guitars.append(Guitar(name, int(year), float(cost)))
        return guitars

    def save_guitars(filename, guitars):
        """Save guitars to file."""
        with open(filename, "w") as file:
            for guitar in guitars:
                file.write(f"{guitar.name},{guitar.year},{guitar.cost}\n")

    def display_guitars(guitars):
        """Display guitars."""
        for i, guitar in enumerate(guitars, 1):
            print(f"Guitar {i}: {guitar}")

    def main():
        """Main program to manage guitars."""
        print("My guitars!")
        guitars = load_guitars("guitars.csv")
        display_guitars(guitars)

        while True:
            name = input("Name: ")
            if not name:
                break
            year = int(input("Year: "))
            cost = float(input("Cost: $"))
            guitars.append(Guitar(name, year, cost))
            print(f"{name} ({year}) : ${cost:.2f} added.")
            print()

        guitars.sort()  # Sort guitars by year
        print("\nThese are my guitars (sorted by year):")
        display_guitars(guitars)

        save_guitars("guitars.csv", guitars)

    if __name__ == '__main__':
        main()