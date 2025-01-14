# Template for crud applications for future me

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

    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="name_list_python"
    )

    cursor = db.cursor()

    sql = "INSERT INTO item (itemName) VALUES (%s)"
    val = (create_input,)

    try:
        cursor.execute(sql,val)
        db.commit()
        print(cursor.rowcount, "record inserted")
    except mysql.connector.Error as err:
        print("Error: {}".format(err))
    finally:
        cursor.close
        db.close

    exit_input = input("Press 'enter' to go back to main menu: ")       


    if exit_input == "enter":
        menu()
    else:
        menu()
     

def read():
    print("======== READ ========\n")

    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="name_list_python"
    )

    cursor = db.cursor()
    sql = "SELECT * FROM item"

    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        for row in results:
            print(row)

    except mysql.connector.Error as err:
        print("Error: {}".format(err))
    finally:
        cursor.close
        db.close

    exit_input = input("Press 'enter' to go back to main menu: ")       


    if exit_input == "enter":
        clear_terminal()
        menu()
    else:
        clear_terminal()
        menu()

def update():
    print("======== UPDATE ========\n")

    update_input = input("Input here the itemID you want to update: ")
    update_change_to = input("Input here the new value: ")


    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="name_list_python"
    )

    cursor = db.cursor()

    sql = "UPDATE item SET itemName = %s WHERE itemId = %s"
    val = (update_change_to, update_input)

    try:
        cursor.execute(sql,val)
        db.commit()
        print(cursor.rowcount, "record updated")
    except mysql.connector.Error as err:
        print("Error: {}".format(err))
    finally:
        cursor.close
        db.close


    exit_input = input("Press 'enter' to go back to main menu: ")       

    if exit_input == "enter":
        clear_terminal()
        menu()
    else:
        clear_terminal()
        menu()

def delete ():
    print("======== DELETE ========\n")

    delete_input = input("Input here the ItemId you want to delete: ")

    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="name_list_python"
    )

    cursor = db.cursor()

    sql = "DELETE FROM item WHERE itemId = %s"
    val = (delete_input,)

    try:
        cursor.execute(sql,val)
        db.commit()
        print(cursor.rowcount, "record deleted")
    except mysql.connector.Error as err:
        print("Error: {}".format(err))
    finally:
        cursor.close
        db.close

    exit_input = input("Press 'enter' to go back to main menu: ")       

    if exit_input == "enter":
        clear_terminal()
        menu()
    else:
        clear_terminal()
        menu()
        

if __name__ == '__main__':
     menu()