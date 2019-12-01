#!/usr/bin/python3
from generate import Generator
from user import User
from getpass import getpass

def create_user(fname, lname, passwordd):
    new_user = User(fname,lname,passwordd)
    return new_user

def save_users(user):
    user.save_user()

def create_social(g_media, g_account, g_password):
    new_social = Generator(g_media, g_account, g_password)
    return new_social

def save_password(generate):
    generate.save_passwords()

def generate(number):
    return Generator.password(number)

def display_user_list():
    return User.display_users()

def display_existing_accounts():
    return Generator.display_passwords()

def findByName(name):
    return User.find_by_name(name)

def main():
    print("-" * 35)
    print("Welcome to ****password-locker**** ")
    print("-" * 35)
    print('\n')
    while True:
        print("create account - ca")
        print("-" * 10)
        print("login - login")
        print("-" * 10)
        print("quit - quit")
        print("-" * 10)
        choice = input()
        choice = choice.lower()
        print("-" * 10)
        print('\n')

        if choice == 'ca':
            print("****create new user****")
            print("-" * 20)
            print("Enter your first name")
            fname = input()
            print("-" * 20)
            print("Enter your second name")
            lname = input()
            print("-" * 20)
            passwordd = getpass("Enter your password:")
            print('\n')

            save_users(create_user(fname,lname,passwordd))
            print("-" * 20)
            print(f"New User {fname} {lname} created")
            print("-" * 20)
            print('\n')

        elif choice == 'login':
            print("***login***")
            print("-" * 20)
            print('\n')
            print("Enter your first name: ")
            first_name = input()
            found_user = findByName(first_name)
            print("-" * 20)
            authentication = getpass(f"Enter password for {found_user.firstName} {found_user.secondName}: ")
            print('\n')
            if authentication == found_user.password:
                print(f"***Welcome {found_user.firstName}***")
                print("-" * 20)
                while True:
                    print("create social account - create")
                    print("-" * 10)
                    print("view social accounts - view")
                    print("-" * 10)
                    print("quit - quit")
                    print("-" * 10)
                    decision = input()
                    decision = decision.lower()
                    print("-" * 10)
                    print('\n')

                    if decision == 'create':
                        print("****create new social account****")
                        print("-" * 20)
                        print("Enter the apps name")
                        g_media = input()
                        print("-" * 20)
                        print("Enter your accounts name")
                        g_account = input()
                        print("-" * 20)
                        g_password = getpass("Enter your password or leave blank to generate password")
                        print('\n')

                        save_password(create_social(g_media,g_account,g_password))
                        print("-" * 20)
                        print(f"New Account for {g_media} @ {g_account} created")
                        print("-" * 20)
                        print('\n')

                    elif decision == 'view':
                        if display_existing_accounts():
                            print("****existing accounts****")
                            print("-" * 20)

                            for acc in display_existing_accounts():
                                print(f"{acc.media}................{acc.account}")
                                print("-" * 20)

                        print('\n')


                    elif decision == 'quit':
                        break

                    else:
                        print("I didnt get you there")

            else:
                print("Wrong password")

        elif choice ==  'quit':
            break

        else:
            print("sorry cant get you")

        # while true:
        #     print("display users - du")
        #     print("-" * 10)
        #     print("store new social")
        #     ans = input()
        #     ans = ans.upper()


        # if ans == 'Y':

if __name__ == '__main__':
    main()
