items = [{"Name" : "Mleko","Quantity": "100","Unit": "litr","Unit_price": "2,40"},
        {"Name" : "Cukier","Quantity": "150","Unit": "kg","Unit_price": "3,60"},
        {"Name" : "Chleb","Quantity": "50","Unit": "szt","Unit_price": "4,50"}]

def get_items (items):
    print("NAZWA:\t\t\tILOŚĆ:\t\t\tJEDN.:\t\t\tCENA(PLN):")
    for i in items:
        print (f"{i['Name']},\t\t\t {i['Quantity']},\t\t\t {i['Unit']},\t\t\t{i['Unit_price']}")

def add_items (Name, Quantity, Unit, Unit_price):
    print ("Dodaję do magazynu")

if __name__ == "__main__":

    print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
    print ("Witaj w menadżerze Twojego Magazynu. Co chciałbyś zrobić?")
     


while True:  
    print("---------------------------------------------------------")
    print ("MENU:\t|show=pokaż|\t|add=dodaj|\t|end=wyjdż|")
    print("---------------------------------------------------------")
    resp = input("WYBIERZ:")
    if  resp == "show":
        get_items(items)
        continue
    elif resp == "add":
            add_items()
            continue
    elif resp == "end":
            print ("Zamykam... Do zobaczenia! ;)")
            break
    else:
        print ("*Wybierz poprawną komendę z menu:*")
        continue