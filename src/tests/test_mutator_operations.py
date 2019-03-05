import datetime

class Person:

    def __init__(self, name, surname, birthdate, address, telephone, email):
        self.name = name
        self.surname = surname
        self.birthdate = birthdate

        self.address = address
        self.telephone = telephone
        self.email = email

    def age(self):
        today = datetime.date.today()
        age = today.year - self.birthdate.year

        if today < datetime.date(today.year, self.birthdate.month, self.birthdate.day):
            age -= 1

        return age


# A wrapper for handling command mutation and examination of a composed object
class Mutator:
    def __init__(self, target):
        self._commands = []
        self._target = target
    
    def store(self, command):
        self._commands.append(command)

    def execute(self):
        for command in self._commands:
            self.parse(command)

    # Parse is just a stub for now
    def parse(self, command):
        return 'GET'

    # Get return the current value of a target prop
    def get(self, prop):
        return None

    # Set will set the contents of a prop
    def set(self, prop, val):
        return None


class TestMutatorOperations:

    # it should be able to instantiate Mutator and a target class
    def test_mutator_can_instantiate(self):
        person = Person(
            "Jane",
            "Doe",
            datetime.date(1992, 3, 12), # year, month, day
            "No. 12 Short Street, Greenville",
            "555 456 0987",
            "jane.doe@example.com"
        )
        mutator = Mutator(person)
        assert(type(mutator) is Mutator)
        assert(callable(getattr(mutator, 'get')))



    # it should have a class that it can instantiate

    # it should be able to set an arbitrary non-clashing property

    # it should be able to set then get a custom property

    # it should be able to override an existing property

    # it should error when trying to override an existing property of an incompatible type

    # When the list operation is called, it should print out starting and set properties

    # When I reach this point, refactor