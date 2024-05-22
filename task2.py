class Food:
    foods=[]

    def createListFoots(self,foods):
        self.foods = foods

    def showListFoots(self):
        print(f"My favorites foots are: {self.foods}")
    
    def addFoot(self,food):
        self.foods.append(food)
    
    def deleteFoot(self,food):
        for f in self.foods:
            if f == food:
                self.foods.remove(f)
    
    def addFootByIndex(self,index,foot):
        self.foods.insert(index,foot)

    def printFoots(self):
        for v,k in enumerate(self.foods):
            print(v,k)

    def ordeListFoots(self):
        print(f"List unordered {self.foods}")
        self.foods.sort()
        print(f"List ordered {self.foods}")
        
myFoots = Food()

# Init List
alimentos_favoritos = ["pizza", "sushi", "chocolate", "pasta"]
myFoots.createListFoots(alimentos_favoritos)

# print foot list
myFoots.showListFoots()

# Add new food to foot lisd
myFoots.addFoot("tacos")
myFoots.showListFoots()

#delete "chocolate" of the list
myFoots.deleteFoot("chocolate")
myFoots.showListFoots()

# add foot by index in list
myFoots.addFootByIndex(1,"ice cream")
myFoots.showListFoots()

# print foots list and index 
myFoots.printFoots()

# print list ordered
myFoots.ordeListFoots()


