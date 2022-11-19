import unittest
from classes.song import Song



class TestSong(unittest.TestCase):

    def setUp(self):
        self.song = Song("we will rock")

    def test_song_name(self):
        self.assertEqual("we will rock", self.song.name)
