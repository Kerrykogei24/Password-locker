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

    
    @classmethod   
    def display_user(cls):
        return cls.user_list

class Creditials:


    creditials_list = []

    def __init__(self,f_username,f_password):

        self.f_password = f_password
        self.f_username  = f_username

    @classmethod
    def verify_user(cls,user_name,password):
        entered_default = ""
        for user in User.user_list:
            if(user.user_name  == user_name  and user.password == password):
                entered_default == user.user_name 
        return  entered_default

    def save_user_creditials(self):
        
        """
        save_user_creditials method saves a new user object to creditials list
        """

        Creditials.creditials_list.append(self)