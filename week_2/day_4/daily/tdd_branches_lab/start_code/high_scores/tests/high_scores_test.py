import unittest

from src.high_scores import latest, personal_best, personal_top_three, list_high_low

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
    def test_top_three(self):
        scores = [12909, 7324, 903, 9023, 38, 209]
        expected_output = [12909, 9023, 7324]
        actual_output = personal_top_three(scores)
        self.assertEqual(expected_output,actual_output )

    # Test ordered from highest tp lowest
    def test_high_low(self):
        scores = [12909, 7324, 903, 9023, 38, 209]
        expected_output = [12909, 9023, 7324, 903, 209, 38 ]
        actual_output = list_high_low(scores)
        self.assertEqual(expected_output,actual_output )

    # Test top three when there is a tie
    def test_top_three_tie(self):
        scores = [233, 45, 89, 90, 90]
        expected_output = [233, 90, 90 ]
        actual_output = personal_top_three(scores)
        self.assertEqual(expected_output,actual_output )

    # Test top three when there are less than three
    def test_top_three_not_enough(self):
        scores = [233, 45,]
        expected_output = [233, 45 ]
        actual_output = personal_top_three(scores)
        self.assertEqual(expected_output,actual_output )


    # Test top three when there is only one

    def test_top_three_just_one(self):
        scores = [233]
        expected_output = [233 ]
        actual_output = personal_top_three(scores)
        self.assertEqual(expected_output,actual_output )
    
