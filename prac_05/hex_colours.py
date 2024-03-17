COLOR_CODES = {
    "Absolute Zero": "#0048ba",
    "Acid Green": "#b0bf1a",
    "AliceBlue": "#f0f8ff",
    "Alizarin crimson": "#e32636",
    "Amaranth": "#e52b50",
    "Amber": "#ffbf00",
    "Amethyst": "#9966cc",
    "AntiqueWhite": "#faebd7",
    "AntiqueWhite1": "#ffefdb",
    "AntiqueWhite2": "#eedfcc"
}


def lookup_color(color_name):
    return COLOR_CODES.get(color_name.capitalize(), "Invalid color name")


def main():
    while True:
        color_name = input("Enter a color name (or blank to quit): ").strip()
        if not color_name:
            break
        color_code = lookup_color(color_name)
        print(f"{color_name}: {color_code}")


main()
