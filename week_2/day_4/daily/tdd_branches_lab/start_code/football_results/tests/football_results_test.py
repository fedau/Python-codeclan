import unittest
from src.football_results import *

class FootballResultsTest(unittest.TestCase):
    def setUp(self):
       self.final_scores = {    
    "home_score": 3,
    "away_score": 1
}
    # Test we get the right result string for a final score dictionary representing -
    def test_home_win(self):
        actual_output = get_result(self.final_scores)
        self.assertEqual("Home win", actual_output )
        # Home win
        

        # Away win
    def test_away_win(self):
        scores =  {"home_score": 2, "away_score": 3}
        actual_output = get_result(scores)
        self.assertEqual("Away win", actual_output )

        # Draw
    def test_tie(self):
        scores =  {"home_score": 3, "away_score": 3}
        actual_output = get_result(scores)
        self.assertEqual("Tie", actual_output )

    # Test we get right list of result strings for a list of final score dictionaries. 
    def test_get_result(self):
        list_scores = [{"home_score": 3,"away_score": 1}, {"home_score": 3,"away_score": 4},{"home_score": 3,"away_score": 5}]
        actual_output = get_results(list_scores)
        self.assertEqual(["Home win", "Away win", "Away win"], actual_output )



