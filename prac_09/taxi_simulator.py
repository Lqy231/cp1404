"""
CP1404/CP5632 Practical
Client code to test Taxi and SilverServiceTaxi class
"""

from prac_09.taxi import Taxi
from silver_service_taxi import SilverServiceTaxi

MENU = "q)uit, c)hoose taxi, d)rive"


def main():
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2),
             SilverServiceTaxi("Hummer", 200, 4)]
    current_taxi = None
    date_bill = 0.0
    print("Let's drive!")
    print(MENU)
    user_choice = input(">>> ").lower()
    while user_choice != 'q':
        if user_choice == 'c':
            print("Taxis available:")
            taxi_number = display_taxis(taxis)
            number_choice = int(input("Choose taxi: "))
            if number_choice not in taxi_number.keys():
                print("Invalid taxi choice.")
            else:
                current_taxi = taxi_number[number_choice]
        elif user_choice == 'd':
            if current_taxi:
                drive_distance = int(input("Drive how far? "))
                current_taxi.start_fare()
                current_taxi.drive(drive_distance)
                print(f"Your {current_taxi.name} trip cost you ${current_taxi.get_fare():.2f}")
                date_bill += current_taxi.get_fare()
            else:
                print("You need to choose a taxi before you can drive")
        else:
            print("Invalid option.")
        print(f"Bill to date: ${date_bill:.2f}")
        print(MENU)
        user_choice = input(">>> ").lower()
    print(f"Total trip cost: ${date_bill:.2f}")
    display_taxis(taxis)


def display_taxis(taxis):
    """Display the taxis with assigned number."""
    taxi_number = {i: taxi for i, taxi in enumerate(taxis, 0)}
    for i in taxi_number.keys():
        print(f"{i} - {taxi_number[i]}")
    return taxi_number


if __name__ == '__main__':
    main()