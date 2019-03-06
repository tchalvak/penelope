import sys
import datetime

import pytest

from ..minirepl import MiniRepl
from ..person import Person
from ..mutator import Mutator

# A trivial person object to act upon in testing
@pytest.yield_fixture()
def resource():
    print("setup")
    person = Person(
        "Jane",
        "Doe",
        datetime.date(1992, 3, 12),
        "No. 12 Short Street, Greenville",
        "555 456 0987",
        "jane.doe@example.com",
    )
    yield person
    print("teardown")


# If you provide a class to the minirepl, can it execute on that.
class TestMiniRepl:

    def test_can_pass_person(self, resource):
        mini = MiniRepl(Mutator(resource))
        assert len(str(mini)) > 20

