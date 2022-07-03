#!/usr/bin/python3
"""
Unittest for class State
"""
import unittest
from models.state import State


class TestState(unittest.TestCase):
    """
    basic tests for State
    """
    def test_state(self):
        """
        method that tests State
        """
        my_state = State()
        my_state.name = "California"
        my_state.my_number = 22
        my_state.save()
        my_state_json = my_state.to_dict()

        self.assertEqual(type(my_state).__name__, "State")
        self.assertEqual(my_state.name, "California")
        self.assertEqual(my_state.my_number, 22)
        self.assertEqual(type(my_state.__dict__), dict)


if __name__ == "__main__":
    unittest.main()
