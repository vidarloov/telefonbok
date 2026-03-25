telefonbok = {}

def läggtill():
    namn = input("Skriv namn:")
    nummer = input("Skriv telefonnummer:")
    telefonbok[namn] = nummer
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
        telefonbok[namn] = nyttnummer
        print("Uppdaterat")
    meny()

def tabort():
    namn = input("Skriv namn för att ta bort kontakt:")
    if namn in telefonbok:
        telefonbok.pop(namn)
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
        läggtill()
    elif val == "2":
        sök()
    elif val == "3":
        uppdatera()
    elif val == "4":
        tabort()
    elif val == "5":
        visa()
    elif val == "6":
        print("Slut")

meny()
