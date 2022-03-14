import csv
items = [{"Name" : "mleko","Quantity": 10,"Unit": "litr","Unit_price": 2},
        {"Name" : "cukier","Quantity": 10,"Unit": "kg","Unit_price": 4},
        {"Name" : "chleb","Quantity": 10,"Unit": "szt","Unit_price": 5}]

sold_list = [] #lista sprzedanych tow.

def load_items_from_csv():
    with open('Magazyn.csv', newline='') as csvfile:
        csvreader = csv.DictReader(csvfile)
        for i in csvreader:
            items.append ({"Name" : i['Name'], "Quantity" : float(i['Quantity']), "Unit" : i['Unit'], "Unit_price" : float(i['Unit_price'])})

def export_items_to_csv():
    with open('Magazyn.csv', mode='w') as csv_file:
        fieldnames = ['Name', 'Quantity', 'Unit', 'Unit_price']
        csvwriter = csv.DictWriter(csv_file, fieldnames=fieldnames)
        csvwriter.writeheader()
        for n in items:
            csvwriter.writerow(n)

def export_sales_to_csv():
    with open('Magazyn_sold.csv', mode='w') as csv_file:
        fieldnames = ['Name', 'Quantity', 'Unit', 'Unit_price']
        csvwriter = csv.DictWriter(csv_file, fieldnames=fieldnames)
        csvwriter.writeheader()
        for n in sold_list:
            csvwriter.writerow(n)

def costs_items (items):
    sum_list = []
    for i in items:
        sum_list.append (i["Quantity"] * i["Unit_price"])
    return sum(sum_list)

def print_costs_items (items):
    cost = costs_items(items)
    print (f"Koszt zakupu towarów to: {cost} PLN")

def get_income (sold_list):
    sub_list = []
    for i in sold_list:
        sub_list.append (i["Quantity"] * i["Unit_price"])
    return sum(sub_list)
    
def print_get_income (items):
    profit = get_income (sold_list)
    print (f"Zyski uzyskane ze sprzedaży towarów to: {profit} PLN")

def show_revenue ():
    profit = get_income (sold_list)
    cost = costs_items (items)
    revenue = profit - cost
    print (f"Bilans Twoich zysków to: {revenue}")

def get_items ():
    sort_items = sorted(items, key=lambda x: (x['Name']))
    print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
    print("NAZWA:\tILOŚĆ:\tJEDN.:\tCENA JEDN.(PLN):")
    for i in sort_items:
        print (f"{i['Name']},\t{i['Quantity']},\t {i['Unit']},\t{i['Unit_price']}")

def add_items (name, quantity, unit, price):
    dict = {"Name": name, "Quantity" : quantity, "Unit" : unit, "Unit_price" : price}
    items.append(dict)
    get_items ()
    print (f"\nDODAŁEM: {name}")

def sell_items (sell_name, sell_quantity):
    for i in items:
        if  i['Name'] == sell_name:
            quant_numb = i['Quantity']
            sell_quant_sum = quant_numb - sell_quantity
            i['Quantity'] = sell_quant_sum
            sold_list.append ({"Name": sell_name, "Quantity" : sell_quantity, "Unit" : i["Unit"], "Unit_price" : i["Unit_price"]})
            print (f"Sprzedaję {sell_quantity} {sell_name}, pozostało {sell_quant_sum}")

if __name__ == "__main__":
    print ("\nWitaj w menadżerze Twojego Magazynu. Co chciałbyś zrobić?")
    items.clear()
    load_items_from_csv()
while True:
    print("\n-------------------------------------------------------------------------")
    print ("MENU:|show=pokaż||add=kup||sell=sprzedaj||b=bilans||s=zapisz||end=wyjdż|")
    print("-------------------------------------------------------------------------")
    resp = input("WYBIERZ: ")
    if  resp == "show":
        get_items()
        continue
    elif resp == "add":
            name = input ("NAZWA ARTYKUŁU: ")
            quantity = float(input ("ILOŚĆ: "))
            unit = input ("JEDNOSTKA: ")
            price = float(input ("CENA: "))
            add_items (name, quantity, unit, price)
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
    elif resp == "b":
            costs_items (items)
            print_costs_items (items)
            get_income (sold_list)
            print_get_income (items)
            show_revenue ()
    elif resp == "s":
            export_items_to_csv()
            export_sales_to_csv()
            print ("Zapisuję do pliku...\nI gotowe! ;)")
    elif resp == "end":
            print ("Zamykam... Do zobaczenia! ;)")
            break
    else:
        print ("*Wybierz poprawną komendę z menu:*")
        continue
