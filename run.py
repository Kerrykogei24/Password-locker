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