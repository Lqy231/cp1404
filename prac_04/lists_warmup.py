numbers = [3, 1, 4, 1, 5, 9, 2]
"""
numbers[0]
    3
numbers[-1]
    2
numbers[3]
    1
numbers[:-1]
    [3, 1, 4, 1, 5, 9]
numbers[3:4]
    [1]
5 in numbers
    True
7 in numbers
    False
"3" in numbers
    False
numbers + [6, 5, 3]
    [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]

In the same Python file, write statements to achieve the following:

Change the first element of numbers to "ten" (the string, not the number 10)
Change the last element of numbers to 1
Print all the elements from numbers except the first two (slice)
Print whether 9 is an element of numbers
"""

numbers[0] = "ten"
print(numbers)

numbers[-1] = 1
print(numbers)

print(numbers[2:])

print(9 in numbers)
