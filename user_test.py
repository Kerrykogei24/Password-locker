import unittest
from user import User
from user import Creditials

class TestClass(unittest.TestCase):
  
    def setUp(self):
        """
        a method that runs before the test
        """
        self.new_user = User("kerry","joker1234")