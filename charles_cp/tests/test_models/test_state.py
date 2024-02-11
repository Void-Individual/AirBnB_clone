#!/usr/bin/python3
"""Unit tests for State class."""
import unittest
from models.state import State


class TestState(unittest.TestCase):
    """Test cases for State class."""

    def test_attributes(self):
        """Test State class attributes."""
        state = State()
        self.assertTrue(hasattr(state, 'name'))
        self.assertEqual(state.name, "")


if __name__ == "__main__":
    unittest.main()
