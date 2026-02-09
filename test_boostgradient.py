# test_boostgradient.py
"""
Tests for BoostGradient module.
"""

import unittest
from boostgradient import BoostGradient

class TestBoostGradient(unittest.TestCase):
    """Test cases for BoostGradient class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = BoostGradient()
        self.assertIsInstance(instance, BoostGradient)
        
    def test_run_method(self):
        """Test the run method."""
        instance = BoostGradient()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
