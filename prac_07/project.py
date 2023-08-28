"""
estimate time: 30 minutes
actual time: 20 minutes
"""


class Project:
    def __init__(self, name="", description="", start_date="", due_date="", priority=""):
        self.name = name
        self.description = description
        self.start_date = start_date
        self.due_date = due_date
        self.priority = priority

    def __str__(self):
        """return string representation of project"""
        return "{}, {}, {}, {}, {}".format(self.name, self.description, self.start_date, self.due_date, self.priority)

    def __repr__(self):
        """return string representation of project"""
        return str(self)

    def __lt__(self, other):
        """less than operator for priority"""
        return self.priority < other.priority
