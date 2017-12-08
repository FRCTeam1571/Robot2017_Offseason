# --builtin option allows you to run the builtin tests without needing to create a tests directory.
# coverage.py
from pyfrc.tests import *

def two_plus(arg):
    return 2 + arg

def test_addition():
    assert two_plus(2) == 4
