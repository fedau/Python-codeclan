import unittest
from src.modules.Car import *
from src.modules.Engine import *
from src.modules.Gearbox import *


class TestCar(unittest.TestCase):

    def setUp(self):
        self.engine = Engine(2)
        self.gearbox = GearBox(6)
        self.car = Car("Red", "Opel" ,self.engine, self.gearbox)

    

    # @unittest.skip("delete this line to run the test")
    def test_car_has_colour(self):
        self.assertEqual("Red", self.car.colour)

        # @unittest.skip("delete this line to run the test")
    def test_car_has_engine(self):
        self.assertEqual(2, self.car.engine.volume)

        # @unittest.skip("delete this line to run the test")

    def test_colour_can_be_changed(self):
        self.car.colour = "Blue"
        self.assertEqual("Blue", self.car.colour)
       
        # @unittest.skip("delete this line to run the test")

    def test_clutch_engage(self):
        self.assertEqual("clutch engaged", self.car.gearBox.engage())


        # @unittest.skip("delete this line to run the test")
    def test_engine_starts(self):
        self.assertEqual("Engine started", self.car.engine.ignite())

    def test_miles(self,):
    
        self.car.add_miles(True)
        self.assertEqual(5, self.car.miles)