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
