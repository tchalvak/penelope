import datetime
import pytest

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

# Wrap the object by composition and act as ducktype
class GlassBox:
    def __init__(self, core_object, new_props):
        self._core_object = core_object
        for prop, value in new_props:
            self.prop = value


# A wrapper for handling command mutation and examination of a composed object
class Mutator:
    def __init__(self, target=None):
        self._commands = {
            'get': 'get',
            'set': 'set',
            '*': '__repr__'
        }
        self._original_instance = target
        self._properties = {}

    # Parse a command into its parts
    def parse_command(self, command):
        parts = command.split(' ')
        prefix = parts[0].lower()
        suffix = parts[1]
        if(prefix is 'get'):
            self.get_prop(suffix)
        else:
            if(suffix is '*'):
                return self.list()
            else:
                set_prop = suffix.split('=')[0]
                set_val = suffix.split('=')[1]
                self.set_prop(set_prop, set_val)

    # Get return the current value of a target prop
    def get_prop(self, prop):
        return self._properties[prop]

    # Set will set the contents of a prop
    def set_prop(self, prop, val):
        # Check that the types are comparable
        self._properties[prop] = val
        return self._properties[prop]

    # Print out object props and current values
    def list(self):
        result = ''
        
        # Return a : delimited string
        return '[list] '.join([f'{prop}: {value}' for prop, value in self._properties])

    def __str__(self):
        return self.list()

    def __repr__(self):
        return self.list()

    # Write the object with new props
    def write(self):
        # Create a subclass of the target object and return it by composition
        return GlassBox(self._target, self._properties)


@pytest.fixture()
def resource():
    print("setup")
    person = Person(
        "Jane",
        "Doe",
        datetime.date(1992, 3, 12),
        "No. 12 Short Street, Greenville",
        "555 456 0987",
        "jane.doe@example.com"
    )
    yield person
    print("teardown")

class TestMutatorOperations:
    # it should be able to instantiate Mutator and a target class
    def test_mutator_can_instantiate(self, resource):
        mutator = Mutator(resource)
        assert(type(mutator) is Mutator)
        assert(callable(getattr(mutator, 'get_prop')))

    # it should have a class that it can instantiate
    def test_target_exists_to_operate_on(self, resource):
        assert(resource is not None)
        assert(isinstance(resource, Person))
        assert(resource.name is "Jane")

    # it should be able to set an arbitrary non-clashing property
    def test_mutator_can_create_prop(self, resource):
        simple_dummy_string = 'dummy string'
        mutator = Mutator(resource)
        result = mutator.set_prop('best_new_prop', simple_dummy_string)
        assert(result is simple_dummy_string)

    # it should be able to set then get a custom property
    def test_mutator_can_get_prop(self, resource):
        random_chars = 'random chars for testing'
        mutator = Mutator(resource)
        mutator.set_prop('mutant', random_chars)
        assert(mutator.get_prop('mutant') == random_chars) 

    # it should be able to override an existing property
    def test_it_can_override_existing_prop(self, resource):
        random_chars = 'Roy Ronalds'
        mutator = Mutator(resource)
        mutator.set_prop('name', random_chars)
        assert(mutator.get_prop('name') == random_chars) 

    @pytest.mark.skip(reason="not yet implemented")
    # it should error when trying to override an existing property of an incompatible type
    def test_it_should_error_on_incompatible_types(self, resource):
        with pytest.raises(Exception):
            mutator = Mutator(resource)
            mutator.set_prop('name', 5)

    # When the list operation is called, it should print out starting and set properties
    def test_partial_list_outputs(self, resource):
        mutator = Mutator(resource)
        assert(mutator.list() is not None)
        assert(type(mutator.list()) is str)
        assert(mutator.list() is not '')
        assert('name' in mutator.list())
        assert('Jane' in mutator.list())

    def test_more_full_list_output_of_mutator(self, resource):
        mutator = Mutator(resource)
        more_matches = ['birthdate', 'telephone', 'email', 'age']
        assert(mutator.list() is not '')
        assert('birthdate' in str(mutator))
        assert(all([x in str(mutator) for x in more_matches]))

    @pytest.mark.skip(reason="not yet implemented")
    def test_extract_the_object_can_run_methods(self, resource):
        mutator = Mutator(resource)
        assert(mutator.age() == 20)

    @pytest.mark.skip(reason="not yet implemented")
    def test_the_mutator_cannot_set_props_that_override_existing_methods(self, resource):
        with pytest.raises(Exception):
            mutator = Mutator(resource)
            mutator.set_prop('age', 999)

    # When I reach this point, refactor