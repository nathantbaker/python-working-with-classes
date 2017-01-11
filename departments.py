# Create a Department class. Create some simple properties and methods on Department. You are going to create some derived classes that inherit from Department, so make sure that the properties/methods you add are general to all Departments (e.g. name, supervisor, employee_count, etc).

class Department(object):
    """Parent class for all departments

    Methods: __init__, get_name, get_supervisor, get_size, get_morale
    """

    def __init__(self, name, supervisor, employee_count, morale="in normal spirits"):
        self.name = name
        self.supervisor = supervisor
        self.size = employee_count
        self.morale = morale

    def __str__(self):

        return "Bagazon has a department named {}. It has {} employees under the direction of {}. The team is currently {}.".format(self.name, self.size, self.supervisor, self.morale)

    def get_name(self):
        """Returns the name of the department"""
        return self.name

    def get_supervisor(self):
        """Returns the name of the supervisor"""
        return self.supervisor

    def get_size(self):
        """Returns the size of the department"""
        return self.size

    def get_morale(self):
        """Returns the morale of the department"""
        return self.morale

Marketing = Department("Marketing", "Doug", 3)
print(Marketing)