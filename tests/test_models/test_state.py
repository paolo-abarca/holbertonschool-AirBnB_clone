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

    def test_update_state(self):
        """
        method 2 that tests State update
        """
        my_state_2 = State()
        my_state_2.name = "California_2"
        my_state_2.my_number = 50
        hour_1 = my_state_2.updated_at
        my_state_2.save()
        my_state_2_json = my_state_2.to_dict()

        my_state_2.name = "California_2.0"
        my_state_2.my_number = 55
        hour_2 = my_state_2.updated_at
        my_state_2.save()
        my_state_2_json_2 = my_state_2.to_dict()

        self.assertNotEqual(hour_1, hour_2)
        self.assertNotEqual(my_state_2_json, my_state_2_json_2)


if __name__ == "__main__":
    unittest.main()
