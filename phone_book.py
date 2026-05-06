import json
import os
from unittest import case
import keyboard

phone_book = {}


with open("phone_book.json", "r") as file:
    phone_book = json.load(file)
    
def save():
    with open("phone_book.json", "w") as file:
        json.dump(phone_book, file)
        
def clear():
    os.system("cls")

def add():
    clear()
    name = input("Write your name:")
    if not name.isalpha():
        print("Name can only contain letters")
        print("-------------------------------")
        return
    
    elif name in phone_book:
        print("Contact already exists")
        print("-------------------------------")
        return
    
    number = input("Write phone number:")
    if not number.isdigit():
        print("Phone number can only contain digits")
        print("-------------------------------")
        return
    
    elif number in phone_book:
        print("Phone number already exists")
        print("-------------------------------")
        return
    
    phone_book[name] = number
    save()
    print("Contact added")
    input('Press "enter" button to go back to the menu')

    print("-------------------------------")


def search():
    clear()
    name = input("Write a name to search for:")
    if name in phone_book:
        print(name, "phone number:", phone_book[name])
        input('Press "enter" button to go back to the menu')
    else:
        print("Contact does not exist")
        input('Press "enter" button to go back to the menu')
    
    print("-------------------------------")

        

def update():
    clear()
    name = input("Write name to update:")
    if not name.isalpha():
        print("Name can only contain letters")
        input('Press "enter" button to go back to the menu')

        print("-------------------------------")
        return
    if name in phone_book:
        new_number = input("Write new phone number:")
        if not new_number.isdigit():
            print("Phone number can only contain digits")
            input('Press "enter" button to go back to the menu')
            print("-------------------------------")
            return
    else:
        print("Contact does not exist")
        input('Press "enter" button to go back to the menu')
        print("-------------------------------")
        return

    phone_book[name] = new_number
    save()
    print("Contact updated")
    input('Press "enter" button to go back to the menu')

    print("-------------------------------")

def remove():
    clear()
    name = input("Write name to delete:")
    if name in phone_book:
        phone_book.pop(name)
        save()
        print("Contact deleted")
        input('Press "enter" button to go back to the menu')
    else:        
        print("Contact does not exist")
        input('Press "enter" button to go back to the menu')

    print("-------------------------------")

def view():
    clear()
    print("All contacts:")
    for name, number in phone_book.items():
        print(name, number)
        
    input('Press "enter" button to go back to the menu')
    print("-------------------------------")

    

def menu():
    while True:
        clear()
        print("Choose an option:")
        print("1. Add contact")
        print("2. Search contact")
        print("3. Update contact")
        print("4. Delete contact")
        print("5. View all contacts")
        print("6. Quit")

        choice = input("Choice:")
        match choice:
            case "1":
                add()
            case "2":
                search()
            case "3":
                update()
            case "4":
                remove()
            case "5":
                view()
            case "6":
                print("Quitting...")
                exit()
            case _:
                clear()
                print("Invalid choice, please try again.")

clear()
menu()
