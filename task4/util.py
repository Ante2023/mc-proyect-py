def form_nuevo_item():
    print("New Producto:")
    name=get_name()
    cant=get_cant()
    price= get_price()

    return name,cant,price


def show_menu():
    print("\nSelect a number from the menu")
    print(" 1: List product ")
    print(" 2: Add product ")
    print(" 3: Update producto ")
    print(" 4: Delete product ")
    print(" 5: Graficar metricas")
    print(" 6: exit menu ")
    option = input("Select an option: ")
    print("")
    return option


def get_name():
    while True:
        name=input(" - Product name \"String\": ")
        if  name:
            return name
        else:
            print("Write  a name: ")


def get_cant():
    while True:
        cant=input(" - Quantity \"Natural\" [0-1000]: ")
        if cant.isdigit() and 0 < int(cant)<= 1000:
            return cant
        else:
            print("The cant is incorrect, please enter a valid number: ")


def get_price():
    while True:
        try:
            price=float(input(" - Price \"Decimal\" [1.0 - 1000.0]: "))
            if  1.0 <= float(price) <= 100.0:
                return price
            else:
                print("Price incorrect, Price \"Decimal\" [1.0 - 1000.0]: €\n")
        except ValueError:
                print("The price is incorrect, value \"Decimal\" [1.0 - 1000.0]: €\n")


def get_id():
    return  input("\nWrite the ID of item to select : ")


def get_field():
    id = int(get_id())
    print(f"\nChoose an option and enter a new number")
    print(f"1: new_name, 2: new_quantity,3: new_price")
    option = int(input("Enter the option: "))
    value = valida_valor(option)
    return id, option, value


def valida_valor(opt):
    value=""
    if  opt ==1: #new_name
        value=get_name()
    elif opt==2: #new_quentity
        value=get_cant()
    elif opt==3: #new_price
        value=get_price()
    else:
        print("Incorrect option")
    return value