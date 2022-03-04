items = [{"Name" : "Mleko","Quantity": "100","Unit": "litr","Unit_price": "2,40"},
        {"Name" : "Cukier","Quantity": "150","Unit": "kg","Unit_price": "3,60"},
        {"Name" : "Chleb","Quantity": "50","Unit": "szt","Unit_price": "4,50"}]

def get_items (items):
    print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
    print("NAZWA:\tILOŚĆ:\tJEDN.:\tCENA(PLN):")
    for i in items:
        print (f"{i['Name']},\t{i['Quantity']},\t {i['Unit']},\t{i['Unit_price']}")
   


def add_items ():
    dict = {"Name": var_name, "Quantity" : var_quantity, "Unit" : var_unit, "Unit_price" : var_price}
    items.append(dict)
    get_items (items)
    print (f"\nDODAŁEM: {var_name}")

if __name__ == "__main__":

    print ("\nWitaj w menadżerze Twojego Magazynu. Co chciałbyś zrobić?")
     
while True:  
    print("\n--------------------------------------------------------------------")
    print ("MENU:\t|show=pokaż|\t|add=dodaj|\t|sub=usuń|\t|end=wyjdż|")
    print("--------------------------------------------------------------------")
    resp = input("WYBIERZ:")
    if  resp == "show":
        get_items(items)
        continue
    elif resp == "add":
            var_name = input ("NAZWA ARTYKUŁU:")
            var_quantity = input ("ILOŚĆ:")
            var_unit = input ("JEDNOSTKA:")
            var_price = input ("CENA JEDNOSTKOWA:")
            add_items ()
            continue
    elif resp == "end":
            print ("Zamykam... Do zobaczenia! ;)")
            break
    else:
        print ("*Wybierz poprawną komendę z menu:*")
        continue