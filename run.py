#!/usr/bin/env python3.6
from user import User,Creditials


def create_new_user(user_name,password):
    '''
    function that creates a user using a password and username
    '''
    new_user = User(user_name,password) 
    return new_user
def save_user(user):
    '''
    function that saves a new user
    '''
    user.save_user()

def display_user(user):
    '''
    function that displays user
    '''
    return User.display_user()

def login_user(password,user_name):
    '''
    a fumction that checks if the users already exist 
    '''
    checked_user = Creditials.verify_user(password,user_name)
    return checked_user

def create_new_credential(f_username,f_password):
    '''
    function that create new credential details for a new user
    '''
    new_credential = Creditials(f_username,f_password)
    return new_credential

def delete_credentials(credentials):
    '''
    function that deletes credentials from the credential list
    '''
    credentials.delete_creditials()
def find_credential(user_name):
    """
    Function that finds a Credentials by an account name and returns the Credentials that belong to that account
    """
    return Creditials.find_by_number(user_name)

def check_credentials(account):
    '''
    function that checks if the credentials of the searched name exist and return true or falsd
    '''
    return Creditials.creditials_exist(account)

def generate_password(self):
    ''' 
    function tht generates password randomely
    '''
    auto_password = Creditials.generate_password(self)
    return auto_password