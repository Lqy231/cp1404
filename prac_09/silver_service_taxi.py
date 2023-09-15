from prac_09.taxi import Taxi


class SilverServiceTaxi(Taxi):
    """A specific variation of Taxi class."""

    flagfall = 4.50

    def __init__(self, name, fuel, fanciness: float):
        """Construct a silver service taxi instance."""
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km *= fanciness

    def __str__(self):
        """Return a string representation of a SilverServiceTaxi."""
        return f"{super().__str__()}, the fanciness is {self.fanciness}, plus flagfall is ${self.flagfall:.2f}."

    def get_fare(self):
        """Return the silver service taxi fare."""
        return super().get_fare() + self.flagfall
