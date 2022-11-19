import unittest
from classes.guest import Guest

class TestGuest(unittest.TestCase):
    
    def setUp(self):
#         self.guest = Drink("beer", 2.00)
#         self.drink_2 = Drink("wine", 3.00)
#         self.drink_3 = Drink("gin", 4.00)
#         self.pub = Pub("The Prancing Pony", 100.00)
        self.guest1 = Guest("Frodo", 10.00)
        
    
    def test_guest_has_name(self):
        self.assertEqual("Frodo", self.guest1.name)
    
    def test_guest_cash(self):
        self.assertEqual(10, self.guest1.cash)

