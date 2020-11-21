import unittest
from user import User
from user import Creditials

class TestClass(unittest.TestCase):
  
    def setUp(self):
        """
        a method that runs before the test
        """
        self.new_user = User("kerry","joker1234")

    def test_init(self):
        """
        test case to check if the object in initialized correctly
        """
        self.assertEqual(self.new_user.user_name,'kerry')
        self.assertEqual(self.new_user.password,'joker1234')

    def test_save_user(self):
        '''
        test case to check if the new instance of the user object has been created
        '''
        
        self.new_user.save_user()
        self.assertEqual(len(User.user_list),1)

class TestCreditials(unittest.TestCase):   
    """
    A test class that defines test cases for credentials class

    """ 
    def setUp(self):
        '''
        Method that runs before each individual credentials test methods run.
        '''
        self.new_creditials = Creditials('kerry','joker1234')

if __name__ == '__main__':
        unittest.main()