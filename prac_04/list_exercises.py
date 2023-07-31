"""
Write a program that prompts the user for 5 numbers and then stores each of these in a list called numbers.
The program should then output information about these numbers, as in the output below.
Note that you can use the functions min, max, sum and len, and you can use the append method to add a number to a list.

   Number: 5
   Number: 20
   Number: 1
   Number: 2
   Number: 3
   The first number is 5
   The last number is 3
   The smallest number is 1
   The largest number is 20
   The average of the numbers is 6.2

"""
NUMBER_OF_REQUESTS = 5
usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn',
             'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']
numbers = []


print("Enter 5 numbers: ")

for i in range(NUMBER_OF_REQUESTS):
    number = int(input("Number: "))
    numbers.append(number)

print("The first number is {}".format(numbers[0]))
print("The last number is {}".format(numbers[-1]))
print("The smallest number is {}".format(min(numbers)))
print("The largest number is {}".format(max(numbers)))
print("The average of the numbers is {}".format(sum(numbers)/len(numbers)))

# Ask the user for their username. If the username is in the above list of authorised users, print "Access granted", otherwise print "Access denied".
username = input("Enter username: ")
if username in usernames:
    print("Access granted")
else:
    print("Access denied")
