# Wrap the object by composition and act as ducktype
class Mimic:
    def __init__(self, core_object):
        self._core_object = core_object
        self._internal_props = {}

    # Get results from dict or the internal object 
    def __getattr__(self, attr):
        if attr in self._internal_props:
            return self._internal_props[attr]
        # get the wrapped object
        return getattr(self._core_object, attr)

    # Add a prop and val to the internal dict
    def __setattr__(self, prop, val):
        # TODO: Throw error on type incompatibility later
        self.__dict__[prop] = val
        return self.__dict__[prop]

        


# A wrapper for handling command mutation and examination of a composed object
class Mutator:
    def __init__(self, target=None):
        self._mimic = Mimic(target)

    # Parse a command into its parts
    def parse_command(self, command):
        parts = command.split(' ')
        prefix = parts[0].lower()
        suffix = parts[1]
        if(prefix is 'get'):
            self.get_prop(suffix)
        else:
            if(suffix is '*'):
                return self.render()
            else:
                set_prop = suffix.split('=')[0]
                set_val = suffix.split('=')[1]
                self.set_prop(set_prop, set_val)

    # Get return the current value of a target prop
    def get_prop(self, prop):
        return getattr(self._mimic, prop)

    # Set will set the contents of a prop
    def set_prop(self, prop, val):
        # Check that the types are comparable
        setattr(self._mimic, prop, val)
        return val

    # Print out object props and current values
    def render(self):
        # Return a : delimited string
        some = vars(self._mimic._core_object)
        rest = self._mimic._internal_props
        # Join the parts of the wrapped object and the dict
        members = {**some, **rest}
        return '[list] ' + str(members)

    def __str__(self):
        return self.render()

    def __repr__(self):
        return self.render()

    # Write the object with new props
    def write(self):
        # Return compositional subclass
        return self._mimic