import mysql.connector
from os import name, system



def clear_terminal():
    if name == 'nt':
        system('cls')
    else:
        system('çlear')

def menu():

    print("======== BASIC CRUD APPLICATION EXAMPLE ========\n")

    print("1. Create\n")
    print("2. Read\n")
    print("3. Update\n")
    print("4. Delete\n")

    choice = input("Please input the number here: ")

    if choice == "1":
        print( "Create Option Chosen")
        clear_terminal()
        create()
    elif choice == "2":
        print( "Read Option Chosen")
        clear_terminal()
        read()
       
    elif choice == "3":
        print( "Update Option Chosen")
        clear_terminal()
        update()

    elif choice == "4":
        print( "Delete Option Chosen")
        clear_terminal()
        delete()

    else:
        print("Invalid Input")
        clear_terminal()
        menu()


def create():
    print("======== CREATE ========\n")
    create_input = input("Input here the item name you want to add: ")



def read():
    print("======== READ ========\n")

def update():
    print("======== UPDATE ========\n")

def delete ():
    print("======== DELETE ========\n")


        

if __name__ == '__main__':
     menu()