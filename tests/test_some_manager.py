# the inclusion of the tests module is not meant to offer best practices for
# testing in general, but rather to support the `find_packages` example in
# setup.py that excludes installing the "tests" package

from unittest import TestCase

from sample.some_manager import SomeManager

def test_success():
    assert True

class TestSomeManager(TestCase):
    def test_fun(self):
        s = SomeManager()
        s.fun()
