"""
estimate time: 30 minutes
actual time: 20 minutes
"""


class Project:
    def __init__(self, name, start_date, priority,cost, completed):
        self.name = name
        self.start_date = start_date
        self.cost = cost
        self.priority = priority
        self.completed = completed

    def __str__(self):
        """return string representation of project"""
        return "{}, start : {}, priority {}, estimate: {}, completion: {}".format(self.name, self.start_date,  self.priority,self.cost, self.completed)

    def __repr__(self):
        """return string representation of project"""
        return str(self)

    def __lt__(self, other):
        """less than operator for priority"""
        return self.priority < other.priority
    
    def time_compare(self, other):
        """less than operator for priority"""
        return self.start_date < other.start_date


