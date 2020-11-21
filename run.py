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

def kerry():

    while True:
        print("Welcome to the password locker")
        print('\n')
        print("Please select a short code to navigate through: if you are a new user use 'nw': to login into your account use 'lg' or 'fp' for find cridential 'ex' to exit ")
        short_code = input().lower()
        print('\n')

        if short_code == 'nw':
            print("please create username")
            created_user_name = input()

            print("create password")
            created_user_password = input()

            print("Please confirm your password")
            confirm_password = input()

            while confirm_password != created_user_password:
                print("Missmatch password")
                print("please enter your password")
                created_user_password = input()

                print("confirm password")
                confirm_password = input()

            else:
                print(f"Congratulations {created_user_name}!! account created succesfully")
                print('\n')
                print("Procced to login")
                print("enter your username")
                entered_username = input()

                print("enter your password")
                entered_password = input()

            while entered_username != created_user_name or entered_password != created_user_password:
                print("Invalid Password or Usernmae")
                print("please username")
                entered_username = input()
                
                print("enter your password")
                entered_password = input()

            else:
                print(f"Hello {entered_username}, Welcome to your account")  
                print('\n')  

        elif short_code == 'lg':
            print("Hello, Welcome back again") 
            print("Please enter your username") 
            default_user_name = input ()

            print("Enter password")
            default_password = input()

            print('\n')

            while default_user_name != "kerry" or default_password != "joker1234":
                print("Wrong user name or Password. hint username kerry")
                print("Enter username")
                default_user_name = input()

                print("Enter your password")
                default_password = input()
                print('\n')

            else:
                print(f"Hello {default_user_name}, login success")   
                print('\n')
                print('\n')  
       
     
 
        elif short_code == 'fp':

                            
                print("Enter the number you want to search for")

                search_number = input()
                if check_existing_contacts(search_number):
                    search_contact = find_user(search_number)
                    print(f"{search_contact.password}")
                    print('-' * 20)

                    print(f"Username.......{search_contact.f_username}")
                    print(f"password.......{search_contact.f_password}")
                else:
                    print("That password does not exist")

        elif short_code == 'ex':
            break
        else:
            print("Please enter valid code to continue. eg lg to login")       

if __name__ == "__main__":
    kerry()