# Wrap the object by composition and act as ducktype
class Mimic:
    def __init__(self, core):
        self._core = core
        self._internal_props = {}

    # Get results from dict or the internal object
    def __getattr__(self, attr):
        if attr in self._internal_props:
            return self._internal_props[attr]
        # get the wrapped object
        return getattr(self._core, attr)

    # Add a prop and val to the internal dict
    def __setattr__(self, prop, val):
        # TODO: Throw error on type incompatibility later
        self.__dict__[prop] = val
        return self.__dict__[prop]


# A wrapper for handling command mutation and examination of a composed object
class Mutator:
    def __init__(self, target=None):
        self._mimic = Mimic(target)

    # Parse a command into its parts, and run
    def command(self, command):
        prefix, suffix = command.split(" ")
        prefix = prefix.lower()  # Normalize
        # TODO: Consider command pattern here
        if prefix == "get":
            if suffix == "*":
                return self.render()
            else:
                return self.get_prop(suffix)
        elif prefix == "set":
            nprop, nval = suffix.split("=")
            self.set_prop(nprop, nval)
        else:
            raise ValueError(f"Invalid command structure for command: {command}")

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
        some = vars(self._mimic._core)
        rest = self._mimic._internal_props
        # Join the parts of the wrapped object and the dict
        members = {**some, **rest}
        return "[list] " + str(members)

    def __str__(self):
        return self.render()

    def __repr__(self):
        return self.render()

    # Write the object with new props
    def write(self):
        # Return compositional subclass
        return self._mimic
