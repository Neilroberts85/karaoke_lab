import unittest
from src.guest import Guest

class TestGuest(unittest.TestCase):
    
    def setUp(self):
        self.guest1 = Guest("Happy", 2)
        self.guest2 = Guest("Sleepy", 3)
        self.guest3 = Guest("Dozy", 0)
        self.guest4 = Guest("Graham", 2)
        self.guest5 = Guest("Ian", 2)
        self.guest6 = Guest("Phil", 2)
        self.guest7 = Guest("Gary", 2)
        
    def test_guest_has_same_name(self):
        self.assertEqual("Happy", self.guest1.name)

   