# penelope
Python cli for testing and state manipulation.


# Install
Check that you have python3 installed, I am running version 3.7:

    python3 --version
    Python 3.7.2

Install from the requirements:
   pip3 install -r requirements.txt

Create a virtual environment for yourself:

    cd src/invoker
    python3 -m venv env
    ./env/bin/pip3 install -r requirements.txt

(That's a good practice for if you need to work with AWS lambda)

# Build
Since we're not using lambda currently, the build step can be skipped for now.

# Test

  python3 -m pytest src/tests




# Run
