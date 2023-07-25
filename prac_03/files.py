# Part 1: Write name to file
name = input("Enter your name: ")
with open("name.txt", "w") as name_file:
    name_file.write(name)

# Part 2: Read name from file and print
with open("name.txt", "r") as name_file:
    name = name_file.read().strip()
print(f"Your name is {name}")

# Part 3: Read first two numbers from file and print sum
with open("numbers.txt", "r") as name_file:
    first_number = int(name_file.readline())
    second_number = int(name_file.readline())
print(f"The sum of the first two numbers is {first_number + second_number}")

# Part 4: Read all numbers from file and print sum
total = 0
with open("numbers.txt", "r") as name_file:
    for line in name_file:
        total += int(line)
print(f"The sum of all numbers is {total}")

