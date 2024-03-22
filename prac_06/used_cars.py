from prac_06.car import Car


def main():
    """Demo test code to show how to use car class."""
    limo = Car(100, "Limo")  # Create a named car object with 100 units of fuel
    limo.add_fuel(20)  # Add 20 more units of fuel
    print(f"Fuel in {limo.name}: {limo.fuel}")  # Print the amount of fuel in the car
    limo.drive(115)  # Attempt to drive the car 115 km
    print(limo)  # Print the car object using the __str__ method


main()

