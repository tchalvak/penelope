import sys
import datetime

import pytest

sys.path.insert(0, "src")
from .. import minirepl
from .. import mutator


# If you provide a class to the minirepl, can it execute on that.
class TestMiniRepl:

    def test_can_pass_person(self):
        # Simple dummy class
        class Dummy:
            def __init__(self):
                self.name = 'Martha'
        
        mini = minirepl.MiniRepl(mutator.Mutator(Dummy()))
        assert len(str(mini)) > 20

