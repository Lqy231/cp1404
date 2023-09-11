from prac_09.unreliable_car import UnreliableCar

# Create a new taxi object, my_taxi, with name "Prius 1", 100 units of fuel and price of $1.23, reliability of 50%
my_taxi = UnreliableCar("Prius 1", 100, 50)
# Drive the taxi 40km
my_taxi.drive()
# Print the taxi's details and the current fare
print(my_taxi)
# Restart the meter (start a new fare) and then drive the car 100km
# my_taxi.start_fare()
my_taxi.drive()
# Print the details and the current fare
print(my_taxi)
