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