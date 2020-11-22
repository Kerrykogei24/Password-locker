import random
import string

class User:

    """
    class that genarate intance of user
    user_list password
    """

    user_list = []

    def __init__(self,username,password):
        self.username = username
        self.password  = password

    def save_user(self):
        """
        save_user method saves a new user object to contact list
        """

        User.user_list.append(self)

    def delete_user(self):

        '''
        delete_contact method deletes a saved contact from the contact_list
        '''

        User.user_list.remove(self)

    
    @classmethod   
    def display_user(cls):
        return cls.user_list

class Creditials:


    creditials_list = []

    def __init__(self,account,username,password):

        self.account = account
        self.password = password
        self.username  = username

    @classmethod
    def verify_user(cls,username,password):
        a_user = ""
        for user in User.user_list:
            if(user.username == username and user.password == password):
                a_user == user.username
        return a_user

    def save_user_creditials(self):
        
        """
        save_user_creditials method saves a new user object to creditials list
        """

        Creditials.creditials_list.append(self)

    def delete_creditials(self):
        '''
        delete_credentials method deletes a saved creditials list
        '''

        Creditials.creditials_list.remove(self) 

    @classmethod
    def find_by_number(cls,account):
        '''
        Method that takes in a password and returns a password that matches that number.

        Args:
        number: password number to search for
        Returns :
        password of person that matches the number.
        '''

        for creditial in cls.creditials_list:
            if (creditial.account == account):
                return creditial

    @classmethod
    def creditials_exist(cls,account):
        '''
        Method that checks if a contact exists from the user details list.
        Args:
        number: Phone number to search if it exists
        Returns :
        Boolean: True or false depending if the user details exists
        '''
        for creditial in cls.creditials_list:
            if creditial.account == account:
                return True

        return False

    def generate_password(self):

        """
        generate a random password consisting of letters
        """
        password = string.ascii_uppercase + string.ascii_lowercase + "havertz"
        return ''.join(random.choice(password) for i in range(1,9))