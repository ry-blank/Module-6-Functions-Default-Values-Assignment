import unittest
from more_functions import validate_input_in_functions as validate


class MyTestCase(unittest.TestCase):
    def test_score_input_test_name(self):
        self.assertEqual(validate.score_input("TestScore"), 'TestScore: 0')

    def test_score_input_test_score_valid(self):
        self.assertEqual(validate.score_input("UnitTest", test_score=50), 'UnitTest: 50')

    def test_score_input_test_score_below_range(self):
        self.assertEqual(validate.score_input("UnitTest", -50), 'Invalid test score, try again!')

    def test_score_input_test_score_above_range(self):
        self.assertEqual(validate.score_input("UnitTest", 150), 'Invalid test score, try again!')

    def test_test_score_non_numeric(self):
        self.assertEqual(validate.score_input("UnitTest", 'Value'), 'Invalid test score, try again!')

    def test_score_input_invalid_message(self):
        self.assertEqual(validate.score_input("UnitTest", 'Invalid'), 'Invalid test score, try again!')


if __name__ == '__main__':
    unittest.main()
