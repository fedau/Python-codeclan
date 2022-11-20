import unittest
from classes.guest import Guest
from classes.room import Room
from classes.song import Song

class TestRoom(unittest.TestCase):
    
    def setUp(self):
        # self.guest = Drink("beer", 2.00)
        # self.drink_2 = Drink("wine", 3.00)
        # self.drink_3 = Drink("gin", 4.00)
     
        self.guest = Guest("Frodo", 10.00)
        self.guest2 = Guest("William", 17.00)
        self.guest4 = Guest("William", 17.00)

        self.guest3 = Guest("David", 20.00)
        self.song = Song("we will rock")
        self.room1 = Room("pop", 7, [self.guest2, self.guest3])
        self.room2 = Room("Rock", 2,[self.guest4, self.guest3])
 
    
    def test_room_has_name(self):
        self.assertEqual("pop", self.room1.name)

    def test_room_capacity(self):
        self.assertEqual(7, self.room1.capacity)

    def test_people_in_room(self):
        actual_output = self.room1.amount_in_room()
        self.assertEqual(2, actual_output) 

    def test_add_guest_to_room(self):
        actual_output = self.room1.add_guest(self.guest)
        print(self.room1.revenue)
        self.assertEqual([self.guest2, self.guest3,self.guest], actual_output)


    def test_add_room_full(self):
        actual_output = self.room2.add_guest(self.guest)
        self.assertEqual("room is full", actual_output)

    def test_add_song(self):
        actual_output = self.room1.add_song_to_room(self.song)
        self.assertEqual(["we will rock"], actual_output)

    def test_revenue(self):
        pass

    def test_frodo_same(self):
        self.assertEqual(self.room1.people_in_room[0].name, self.room2.people_in_room[0].name)

