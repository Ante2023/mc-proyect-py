from product import Product
import util as menu

class Inventory():

    inventary =[]
    id=0

    def list_inventory(self):
        if not len(self.inventary):
            print("\nNo item to display !!!")
            return
        print("\nList of existing items")
        for i in self.inventary:
            print("[",i.id ,",", i.name,",", i.quantity,",", i.price,"]")

        print(f"Products quantity: {len(self.inventary)}")
    

    def add_item(self,item):
        per = Product(item.name,item.quantity,item.price,self.id)
        self.id+=1
        self.inventary.append(per)
        return per


    def update_item(self):
        if not len(self.inventary):
            print("\nNo items to update !!!")
            return
        
        self.list_inventory()
        id, option, value = menu.get_field()
        if option== 1:
            print("Name old -> ",self.inventary[id])
            self.inventary[id].name = value
            print("Name new -> ",self.inventary[id])
        elif option == 2:
            print("Name old -> ",self.inventary[id])
            self.inventary[id].quantity = value
            print("Name new -> ",self.inventary[id])
        elif option == 3:
            print("Name old -> ",self.inventary[id])
            self.inventary[id].price = value
            print("Name new -> ",self.inventary[id])
        self.list_inventory()


    def delete_item(self):
        if not len(self.inventary):
            print("\nNo items to delete !!!")
            return
        self.list_inventory()
        id = int(menu.get_id())
        try:
            print(self.inventary[id])
            delette = self.inventary.pop(id)
            print(f"the item {delette} was removed")
            self.list_inventory()
        except IndexError:
            print ("The element not exists")
        

    def get_inventory(self):
        return self.inventary


    