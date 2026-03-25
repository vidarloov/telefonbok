import json
import os

telefonbok = {}


with open("telefonbok.json", "r") as fil:
    telefonbok = json.load(fil)
    
def spara():
    with open("telefonbok.json", "w") as fil:
        json.dump(telefonbok, fil)
        
def rensa():
    os.system("cls")

def läggtill():
    namn = input("Skriv namn:")
    nummer = input("Skriv telefonnummer:")
    if not nummer.isdigit():
        print("Telefonnummeret får bara innehålla siffror")
        meny()
        return
    
    telefonbok[namn] = nummer
    spara()
    print("tillagd")
    meny()

def sök():
    namn = input("Skriv ett namn att söka efter:")
    if namn in telefonbok:
        print(namn, "telefonnummer:", telefonbok[namn])
    meny()

def uppdatera():
    namn = input("Skriv namn för att uppdatera:")
    if namn in telefonbok:
        nyttnummer = input("Skriv nytt telefonnummer:")
        if not nyttnummer.isdigit():
            print("Telefonnummeret får bara innehålla siffror")
            meny()
            return

        telefonbok[namn] = nyttnummer
        spara()
        print("Uppdaterat")
    meny()

def tabort():
    namn = input("Skriv namn för att ta bort kontakt:")
    if namn in telefonbok:
        telefonbok.pop(namn)
        spara()
        print("borttagen")
    meny()

def visa():
    print("Alla kontakter:")
    for namn, nummer in telefonbok.items():
        print(namn, nummer)
    meny()

def meny():
    print("Välj en")
    print("1. Lägg till kontakt")
    print("2. Sök kontakt")
    print("3. Uppdatera kontakt")
    print("4. Ta bort kontakt ")
    print("5. Visa alla kontakter")
    print("6. Avsluta")

    val = input("val:")

    if val == "1":
        rensa()
        läggtill()
    elif val == "2":
        rensa()
        sök()
    elif val == "3":
        rensa()
        uppdatera()
    elif val == "4":
        rensa()
        tabort()
    elif val == "5":
        rensa()
        visa()
    elif val == "6":
        rensa()
        print("Slut")
    else:
        rensa()
        print("Finns inte, försök igen.")
        meny()

meny()
