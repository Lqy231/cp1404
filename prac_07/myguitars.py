from prac_07.guitar import Guitar


def main():
    guitars = []
    infile = open("guitars.csv", "r")
    for line in infile:
        parts = line.strip().split(",")
        guitars.append(Guitar(parts[0], int(parts[1]), float(parts[2])))
    infile.close()

    # sort guitars by year
    guitars.sort()

    # display guitars
    display_guitars(guitars)
    # ask user for new guitar
    print("add new guitar!")
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: $ "))
        guitars.append(Guitar(name, year, cost))
        print("{} ({}) : ${} added.".format(name, year, cost))
        name = input("Name: ")

    # display guitars
    display_guitars(guitars)
    # save guitars to file
    with open("guitars.csv", "w") as outfile:
        for guitar in guitars:
            print("{},{},{}".format(guitar.name, guitar.year, guitar.cost), file=outfile)


def display_guitars(guitars):
    print("These are my guitars(initially):")
    for i, guitar in enumerate(guitars):
        vintage_string = ""
        if guitar.is_vintage():
            vintage_string = "(vintage)"
        print("Guitar {}: {:>20} ({}), worth ${:10,.2f} {}".format(i + 1, guitar.name, guitar.year, guitar.cost,
                                                                   vintage_string))


main()
