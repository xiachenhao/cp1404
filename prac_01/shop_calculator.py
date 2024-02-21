def calculate_total_price(num_items, prices):
    total_price = sum(prices)
    if total_price > 100:
        total_price *= 0.9  
    return total_price


def get_valid_num_items():
    num_items = -1
    while num_items < 0:
        num_items_input = input("Number of items: ")
        if num_items_input.isdigit():
            num_items = int(num_items_input)
            if num_items < 0:
                print("Invalid number of items!")
        else:
            print("Invalid input! Please enter a valid integer.")
    return num_items


def get_valid_prices(num_items):
    prices = []
    for i in range(num_items):
        price = -1
        while price < 0:
            price_input = input(f"Price of item {i+1}: ")
            if price_input.replace('.', '', 1).isdigit():
                price = float(price_input)
                if price < 0:
                    print("Invalid price! Price cannot be negative.")
                else:
                    prices.append(price)
            else:
                print("Invalid input! Please enter a valid number.")
    return prices


def main():
    num_items = get_valid_num_items()
    prices = get_valid_prices(num_items)

    total_price = calculate_total_price(num_items, prices)
    print(f"Total price for {num_items} items is ${total_price:.2f}")
    main()



