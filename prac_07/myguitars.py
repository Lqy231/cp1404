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
    print("These are my guitars:")
    print(guitars)


main()
