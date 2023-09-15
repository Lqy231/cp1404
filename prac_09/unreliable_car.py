from prac_09.car import Car


class UnreliableCar(Car):
    def __init__(self, name, fuel, reliability):
        """Initialise a UnreliableCar instance, based on parent class Car."""
        super().__init__(name, fuel)
        self.reliability = reliability

    def __str__(self):
        """Return a string representation like a Car but with reliability."""
        return f"{super().__str__()}, reliability={self.reliability}"

    def drive(self):
        import random
        random_number = random.randint(0, 100)
        while random_number > self.reliability:
            random_number = random.randint(0, 100)
        distance_driven = super().drive(random_number)
        return distance_driven
            
