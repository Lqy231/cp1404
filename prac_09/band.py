class Band:
    """Represent a Band object."""

    def __init__(self, name):
        """Initialize a Band with a name and a list of members."""
        self.name = name
        self.members = []

    def __str__(self):
        """Return a string representation of a Musician."""
        return f"{self.name} ({','.join(str(member) for member in self.members)})"

    def add(self, new_member):
        """Add a new member to the band."""
        self.members.append(new_member)

    def play(self):
        """Let musicians play."""
        return '\n'.join(member.play() for member in self.members)
