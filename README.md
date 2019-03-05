# penelope
Python cli for testing and state manipulation.


# Install
Check that you have python3 installed, I am running version 3.7:

    python3 --version
    Python 3.7.2

Install from the requirements:
   pip3 install -r requirements.txt

Create some virtual environments:

    python3 -m venv .venv
    source .venv/bin/activate
    pip3 install -r requirements.txt

# Build
The build step could be useful for building lambda requirements in the future, but can be skipped for now.

# Test

  pytest


# Run

To get the benefits of the mutator directly, you'll want to run it from within your own code, to mutate a class of your own creation.

However, in the meantime, you can run an example command console via:

    python3 src/mutator/example.py

