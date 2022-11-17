import unittest

from src.high_scores import latest, personal_best, personal_top_three

# Tests adapted from `problem-specifications//canonical-data.json` @ v4.0.0


class HighScoresTest(unittest.TestCase):
    
    # Tests

    # Test latest score (the last thing in the list)
    def test_latets_score(self):
        scores = [12909, 7324, 903, 9023, 38, 209]
        expected_output = 209
        actual_output = latest(scores)
        self.assertEqual(expected_output,actual_output )
    # Test personal best (the highest score in the list)
    def test_personal_best(self):
        scores = [12909, 7324, 903, 9023, 38, 209]
        expected_output = 12909
        actual_output = personal_best(scores)
        self.assertEqual(expected_output,actual_output )

    # Test top three from list of scores

    # Test ordered from highest tp lowest

    # Test top three when there is a tie

    # Test top three when there are less than three

    # Test top three when there is only one
    
