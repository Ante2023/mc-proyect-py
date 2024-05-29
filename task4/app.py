from product import Product
from inventory import Inventory
from graphics import Graphics

import util  as menu

def init_app():
    
    inventory = Inventory()
    option = menu.show_menu()

    while True:
        if option == "1": # List product
            inventory.list_inventory()
        elif option == "2": # Create new Product
            name,cant,price=menu.form_nuevo_item()
            product = inventory.add_item(Product(name,cant,price))
            print(product)
        elif option == "3": #update
            inventory.update_item()
        elif option == "4": # Delete
            inventory.delete_item() 
        elif option == "5": #graphics
            Graphics().create_graphics(inventory.get_inventory())            
        elif option == "6": #exit
            return # exit()
        else:
           print("Incorrect Opción!!")
        option=menu.show_menu()
        
if __name__=='__main__':
    init_app()
