import sys
import datetime

import pytest

from ..minirepl import MiniRepl
from ..person import Person
from ..mutator import Mutator


# If you provide a class to the minirepl, can it execute on that.
class TestMiniRepl:

    def test_can_pass_person(self):
        # Simple dummy class
        class Dummy:
            def __init__(self):
                self.name = 'Martha'
        
        mini = MiniRepl(Mutator(Dummy()))
        assert len(str(mini)) > 20

