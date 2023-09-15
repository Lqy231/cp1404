from silver_service_taxi import SilverServiceTaxi


def main():
    new_silver_taxi = SilverServiceTaxi("Sylva", 160, 34.2)
    new_silver_taxi.drive(80)
    print(new_silver_taxi)
    print(f"The fare for a 80km trip is ${new_silver_taxi.get_fare():.2f}")
    another_silver_taxi = SilverServiceTaxi("Silva", 50, 2)
    another_silver_taxi.drive(18)
    print(f"For an 18 km trip in a SilverServiceTaxi with fanciness of 2, the fare should be $48.78."
          f" Our output fare is ${another_silver_taxi.get_fare():.2f}")


main()
