import unittest
from classes.guest import Guest
from classes.room import Room
from classes.song import Song

class TestRoom(unittest.TestCase):
    
    def setUp(self):
        # self.guest = Drink("beer", 2.00)
        # self.drink_2 = Drink("wine", 3.00)
        # self.drink_3 = Drink("gin", 4.00)
        self.room = Room("pop", 7)
        self.guest = Guest("Frodo", 10.00)
        self.song = Song("we will rock")
        
    
    def test_room_has_name(self):
        self.assertEqual("pop", self.room.name)

    def test_room_capacity(self):
        self.assertEqual(7, self.room.capacity)
    
    def test_add_guest_to_room(self):
        actual_output = Room.add_guest(self.guest)
        self.assertEqual(["Frodo"], actual_output)
        # self.assertEqual(1, actual_output)\

    def test_add_one_to_room(self):
        actual_output = Room.add_one_to_room(self)
        self.assertEqual(1, actual_output)


    def test_add_song(self):
        actual_output = Room.add_song_to_room(self.song)
        self.assertEqual(["we will rock"], actual_output)


