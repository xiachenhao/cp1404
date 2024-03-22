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

# In guitar_test.py
from guitar import Guitar


def test_guitar():
    """Test the Guitar class."""
    gibson = Guitar("Gibson L-5 CES", 1922, 16035.40)
    another_guitar = Guitar("Another Guitar", 2013, 0)

    assert gibson.get_age(2022) == 100
    assert another_guitar.get_age(2022) == 9
    assert gibson.is_vintage(2022) is True
    assert another_guitar.is_vintage(2022) is False

    print("All tests passed!")


test_guitar()


# In guitars.py
from guitar import Guitar


def main():
    """Main program to manage guitars."""
    print("My guitars!")
    guitars = []
    while True:
        name = input("Name: ")
        if not name:
            break
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        guitars.append(Guitar(name, year, cost))
        print(f"{name} ({year}) : ${cost:.2f} added.")
        print()

    print("\nThese are my guitars:")
    for i, guitar in enumerate(guitars, 1):
        vintage_string = " (vintage)" if guitar.is_vintage(2023) else ""
        print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f}{vintage_string}")


main()
