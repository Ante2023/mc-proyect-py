class Product():

    def __init__(self,name,quantity,price,id=0) -> None:
        self.id = id
        self.name=name
        self.quantity=quantity
        self.price=price


    def __str__(self) -> str:
        product = f"Product: id:{self.id}, name:{self.name}, quantity {str(self.quantity)}, price :{str(self.price)}"
        return product