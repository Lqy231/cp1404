from prac_06.guitar import Guitar


def main():
    """Guitar play code."""
    guitars = []
    print("My guitars!")
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: $ "))
        guitars.append(Guitar(name, year, cost))
        print("{} ({}) : ${} added.".format(name, year, cost))
        name = input("Name: ")
    print("These are my guitars:")
    for i, guitar in enumerate(guitars):
        vintage_string = ""
        if guitar.is_vintage():
            vintage_string = "(vintage)"
        print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f}{vintage_string}")

main()
