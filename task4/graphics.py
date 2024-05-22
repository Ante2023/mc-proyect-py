import matplotlib.pyplot as plt


class Graphics():
    def create_graphics(self,inventory):
        if not len(inventory):
            print("Has no item to display !!!")
            return
        product_names = []
        quantities = []
        price=[]

        for product in inventory:
            product_names.append(product.name)
            quantities.append(product.quantity)
            price.append(product.price)

        plt.bar(product_names, quantities)
        plt.xlabel('Product')
        plt.ylabel('Quantity')
        plt.title('Inventory Levels')
        plt.show()

        plt.pie(quantities, labels=product_names,autopct='%.2f%%')
        plt.show()

        plt.hist(price)
        plt.show()

        plt.scatter(product_names,price)
        plt.plot(product_names, price)
        plt.show()