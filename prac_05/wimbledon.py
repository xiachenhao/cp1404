def read_data(filename):
    champions = {}
    countries = set()
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        for line in in_file:
            # Assuming the CSV file has two columns: Champion, Country
            champion, country = line.strip().split(',')
            champions[champion] = champions.get(champion, 0) + 1
            countries.add(country)
    return champions, countries


def display_champions(champions):
    print("Wimbledon Champions:")
    for champion, count in champions.items():
        print(f"{champion} {count}")


def display_countries(countries):
    sorted_countries = sorted(countries)
    countries_str = ', '.join(sorted_countries)
    print(f"These {len(sorted_countries)} countries have won Wimbledon:")
    print(countries_str)


def main():
    filename = "wimbledon.csv"
    champions, countries = read_data(filename)
    display_champions(champions)
    display_countries(countries)


main()
