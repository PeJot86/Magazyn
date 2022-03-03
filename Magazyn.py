items = [{"Name" : "Mleko w proszku","Quantity": "100","Unit": "litr","Unit_price": "2,40"},
        {"Name" : "Cukier","Quantity": "150","Unit": "kg","Unit_price": "3,60"},
        {"Name" : "Chleb","Quantity": "50","Unit": "szt","Unit_price": "4,50"}]

def get_items (items):
    print("NAZWA:\t\t\tILOŚĆ:\t\t\tJEDN.:\t\t\tCENA(PLN):")
    for i in items:
        print (f"{i['Name']},\t\t\t {i['Quantity']},\t\t\t {i['Unit']},\t\t\t{i['Unit_price']}")


if __name__ == "__main__":

    print("---------------------------------------------------------")
    print ("Witaj w menadżerze Twojego Magazynu. Co chciałbyś zrobić?\n\nMENU: |exit=wyjdż|\t|show=pokaż|")
    print("---------------------------------------------------------")   
    
while True:  
    while (input() == "show"):
        get_items(items)
    
    
    (input("Zamknij=ENTER") == "end")
    print ("Zamykam... Do zobaczenia!")
    break
   

            
        