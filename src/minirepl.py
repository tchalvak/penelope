import code
import datetime

from .mutator import Mutator
from .person import Person

# Simple Python Repl https://dev.to/rpalo/your-own-python-repl-in-twenty-lines-or-less

# Perform mutation operations depending on the commands involved
class MiniRepl:
    def __init__(self, mutant):
        self.size = 50
        self._mutant = mutant

    # Run the command string passed in
    def command(self, command):
        self._mutant.command(command)

    def __repr__(self):
        return f"Final core object: {str(self._mutant)}"

# Handle the interactivity
def interact(manipulatee):
    mutant = Mutator(manipulatee)
    rep = MiniRepl(mutant)
    command_list = {
        "GET *": rep.command,
        "SET": rep.command,
    }
    venn = {**command_list, **locals()}
    code.interact(
        banner="Input commands to interact with your object, for example GET name, SET name=Will, GET *",
        local=venn,
        exitmsg="Exiting interactive portion"
    )
    return mutant.render()

#Execute the mini-repl
if __name__ == "__main__":
    person = Person(
        "Jane",
        "Doe",
        datetime.date(1992, 3, 12),
        "No. 12 Short Street, Greenville",
        "555 456 0987",
        "jane.doe@example.com",
    )
    result = interact(person)
    print(f"Final result: {result}")
    