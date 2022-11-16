import unittest
from src.pub import Pub 
from src.drinks import Drinks
from src.customer import Customer
from src.food import Food

class TestPub(unittest.TestCase):
    
    def setUp(self):
        self.pub = Pub("The Prancing Pony", 100.00)
        self.drink = Drinks("Sprite", 3.5)
        self.customer = Customer("Michael Scot", 50, 20)
        self.food = Food("Pasta", 7, 1)


    def test_pub_has_name(self):
        self.assertEqual("The Prancing Pony", self.pub.name)


    def test_pub_has_till(self):
        self.assertEqual(100.00, self.pub.till)

    def test_increase_till(self):
        self.pub.increase_till(2.50)
        self.assertEqual(102.50, self.pub.till)


    def test_drinks_has_name(self):
        self.assertEqual("Sprite", self.drink.name)

    def test_drinks_has_price(self):
        self.assertEqual(3.5, self.drink.price)

    def test_sell_drink(self):
        self.pub.increase_till(self.drink.price)
        self.assertEqual(103.5, self.pub.till)

    def test_customer_has_name(self):
        self.assertEqual("Michael Scot", self.customer.name)

    def test_customer_has_money(self):
        self.assertEqual(50, self.customer.wallet)

    def test_customer_buy_drink(self):
        self.pub.buy_drink(self.customer, self.drink)
        self.assertEqual(103.5, self.pub.till)
        self.assertEqual(46.5, self.customer.wallet)
        
    def test_customer_buy_drink_no(self):
        customer = Customer("Michael Scot", 50, 16)

        self.pub.buy_drink(customer, self.drink)
        self.assertEqual(100, self.pub.till)
        self.assertEqual(50, customer.wallet)

    def test_customer_age(self):
        self.assertEqual(20, self.customer.age)
    

    def test_customer_age(self):
        result = self.pub.check_age(self.customer)
        self.assertTrue(result)
    
    def test_customer_underage(self):
        customer = Customer("Michael Scot", 50, 16)
        result = self.pub.check_age(customer)
        self.assertFalse(result)

    def test_drunkenness(self):
        self.customer.drunken(self.drink)
        self.assertEqual(2, self.customer.drunk)

    def test_intoxication_to_sell(self):
        self.customer.drunk = 2
        self.pub.check_drunkenness(self.customer, self.drink)
        self.assertEqual(4, self.customer.drunk)

    def test_intoxication_to_drunk(self):
        self.customer.drunk = 6
        result = self.pub.check_drunkenness(self.customer, self.drink)
        self.assertEqual("you are to drunk", result)


    # def test_intoxication_to_drunk(self):
    #     self.customer.drunk = 6
    #     result = self.pub.check_drunkenness(self.customer, self.drink)
    #     self.assertFalse(result)


    def test_food_name(self):
        self.assertEqual("Pasta", self.food.name)

    def test_buy_food(self):
        self.customer.drunk = 6
        self.pub.buy_food(self.customer, self.food)
        self.assertEqual(43, self.customer.wallet)
        self.assertEqual(107, self.pub.till)
        self.assertAlmostEqual(5, self.customer.drunk)
