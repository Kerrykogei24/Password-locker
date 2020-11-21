import random
import string

class User:

    """
    class that genarate intance of user
    user_list password
    """

    user_list = []

    def __init__(self,user_name,password):
        self.user_name = user_name
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