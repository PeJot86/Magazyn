items = [{"Name" : "mleko","Quantity": 10,"Unit": "litr","Unit_price": 2},
        {"Name" : "cukier","Quantity": 10,"Unit": "kg","Unit_price": 3},
        {"Name" : "chleb","Quantity": 10,"Unit": "szt","Unit_price": 5}]

sort_items = sorted(items, key=lambda x: (x['Name']))
sum_list=[]
div = 0

for i in items:     
    div = i["Quantity"] * i["Unit_price"]
    sum_list.append (div)
    sum_price = sum(sum_list)

def get_items (sort_items):
    sort_items = sorted(items, key=lambda x: (x['Name']))
    print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
    print("NAZWA:\tILOŚĆ:\tJEDN.:\tCENA JEDN.(PLN):")
    for i in sort_items:
        print (f"{i['Name']},\t{i['Quantity']},\t {i['Unit']},\t{i['Unit_price']}")

def add_items (name, quantity, unit, price):       
    dict = {"Name": name, "Quantity" : quantity, "Unit" : unit, "Unit_price" : price}
    items.append(dict)
    get_items (sort_items)
    print (f"\nDODAŁEM: {name}")

def sell_items (sell_name, sell_quantity):
    quant_numb = 0
    for i in items:
        if  i['Name'] == sell_name:
            quant_numb = i['Quantity']
            sell_quant_sum = quant_numb - sell_quantity
            i['Quantity'] = sell_quant_sum
            print (f"Sprzedaję {sell_quantity} {sell_name}, pozostało {sell_quant_sum}")

if __name__ == "__main__":
    print ("\nWitaj w menadżerze Twojego Magazynu. Co chciałbyś zrobić?")     
while True:  
    print("\n--------------------------------------------------------------------")
    print ("MENU:\t|show=pokaż|\t|add=dodaj|\t|sell=sprzedaj|\t\t|end=wyjdż|")
    print("--------------------------------------------------------------------")
    resp = input("WYBIERZ: ")
    if  resp == "show":
        get_items(sort_items)
        print (f"\t\t\tRAZEM KOSZTY(PLN) {sum_price}")
        continue
    elif resp == "add":
            name = input ("NAZWA ARTYKUŁU: ")
            quantity = float(input ("ILOŚĆ: "))
            unit = input ("JEDNOSTKA: ")
            price = float(input ("CENA: "))
            add_items (name, quantity, unit, price)
            div = quantity * price
            sum_list.append (div)
            sum_price = sum(sum_list)
            continue
    elif  resp == "sell":
            sell_name = input ("Co sprzedajemy?: ")
            for i in items:
                if  i['Name'] == sell_name:
                    print ("Jest!")
                    break
            else:   
                print ("Nie posiadamy takiego towaru!")
                continue                       
            sell_quantity = float(input("Podaj ilość: "))
            sell_items (sell_name, sell_quantity)                                          
            continue
    elif resp == "end":
            print ("Zamykam... Do zobaczenia! ;)")
            break
    else:
        print ("*Wybierz poprawną komendę z menu:*")
        continue