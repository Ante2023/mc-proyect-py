class Friend:
    def __init__(self):
        self.formSetFriend()

    def formSetFriend(self):
        self.welcome()
        self.age = self.setAge()
        self.name = self.setOnlyTexto("what's your first name (Only one):\n")
        self.nationality = self.setOnlyTexto("where are your from:\n")
        self.height=self.setHeight()
        self.fanBC=self.setFansBarca()

#Solicite al sistema mostrar la informacion de Amigo
    def getInfoFriend(self):
        print(f"\nHi!, my name is \"{self.name.lower()}\" I am {self.age} years old, I am from {self.nationality}, I am {self.height}cm tall, and lastly it is {self.fanBC} that i am a Barca fan\nBye!!!")

#Solicite al usuario que ingrese su nombre o su nacionaliad, ambos texto
    def setOnlyTexto(self,msg):
        while True:
            name=input(msg)
            if name.isalpha():
                break
            else :
                print("You have tho enter alphabetical text\n")
        return name

#Solicite la edad del usuarios
    def setAge(self):
        while True:
            age=input("what's your age?, enter a value between 10 and 100:\n")
            if age.isdigit() and 10 <= int(age)<= 100:
                return age
            else:
                print("The age is incorrect, please enter a valid number\n")

#Solicite la altura del usuario en cm
    def setHeight(self):
        while True:
            try:
                height=float(input("what's your height in cm?. Use point for a range between 20.0 and 190.0 :\n"))
                if  20.0 <= float(height) <= 190.0:
                    return height
                else:
                    print("The height is incorrect, please enter a valid number inner 20cm and 190cm\n")
            except ValueError:
                    print("The height is incorrect, please enter a valid number inner 20cm and 190cm\n")

#Pregunte si es fanatico del FC Barcelona con una respuesta V o F usando una respuesta booleana
    def setFansBarca(self):
        while True:
            height=input("Are you fans to Barca? yes or si or not or no:\n").lower()
            if height =="yes" or  height =="si" or height =="not"or height =="si" :
                return height =="yes" or height =="si"
            else:
                print("Incorrect answer, the possible answer are: yes, not, si or no\n")
    
    def welcome(self):
        print(f"{'*'*77}\n * Wellcome to the friends regitry , answer the following questions please! *  \n{'*'*77}\n")

mxFriend = Friend()
mxFriend.getInfoFriend()

"""
SALIDA
Contruir unmensaje que incluya toda la información recopilada en un formato amistoso
EL mensaje debería decir  Mi nombre es :NOMBRE, tengo :EDAD de años , desde :NACIONALIDAD, soy >ALTURA cm de alto y definitivamnte es F/V que soy un fan de Barca
"""

"""Usar input() para recopilar todos los detalles necesarios"""
""""Convierta la edad en un entero y altura a flotante"""
"""Use una expresion booleana para convertir la declaración de verdad a un valor Booleano directamente """
"""Imprimir el resultado con todos los detalles recopilados"""