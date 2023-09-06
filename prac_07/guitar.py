class Guitar(object):
    def __init__(self, name="", year=0, cost=0):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return a string representation of a Guitar object."""
        return "{} ({}) : ${}".format(self.name, self.year, self.cost)

    def get_age(self):
        """Return the age of a Guitar object."""
        age = 2023 - self.year
        return age

    def is_vintage(self):
        """Return True if a Guitar object is vintage, False otherwise."""
        if self.get_age() >= 50:
            return True
        else:
            return False

    def __lt__(self, other):
        """Return True if a Guitar object is less than another Guitar object, False otherwise."""
        return self.year < other.year

    def __repr__(self) -> str:
        """Return a string representation of a Guitar object."""
        return "{} ({}) : ${}".format(self.name, self.year, self.cost)