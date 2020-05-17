import random

class Persona:
    # __NOMBRE = ''
    # __EDAD = 0
    SEXO = 'H'
    DNI =0
    # __PESO = 0
    # __ALTURA = 0

# Constructor por defecto
    def __init__(self):
        self.__nombre = ''
        self.__edad = 0
        self.__dni = __generaDNI()
        self.__sexo = 'H'
        self.__peso = 0
        self.__altura = 0

# • Un constructor con el nombre, edad y sexo, el resto por defecto.
    def __init__(self, nombre, edad, sexo):
        self.__nombre = nombre
        self.__edad = edad
        self.__sexo = sexo
        self.__dni = __generaDNI()
        self.__peso = 0
        self.__altura = 0

# • Un constructor con todos los atributos como parámetro.
    def __init__(self, nombre='', edad=0, sexo=SEXO, peso=0, altura=0):
        self.__nombre = nombre
        self.__edad = edad
        self.__dni = __generaDNI()
        self.__sexo = sexo
        self.__peso = peso
        self.__altura = altura

# • Métodos set de cada parámetro, excepto de DNI.
    def setnombre(self, nombre):
        self.__nombre = nombre

    def setedad(self, edad):
        self.__edad = edad
    
    def setsexo(self, sexo):
        self.__sexo= sexo

    def setpeso(self, peso):
        self.__peso = peso
    
    def setaltura(self, altura):
        self.__altura = altura

# calcularIMC(): calculara si la persona esta en su peso ideal (peso en
# kg/(altura^2 en m)), si esta fórmula devuelve un valor menor que 20, la
# función devuelve un -1, si devuelve un número entre 20 y 25 (incluidos),
# significa que esta por debajo de su peso ideal la función devuelve un 0 y si
# devuelve un valor mayor que 25 significa que tiene sobrepeso, la función
# devuelve un 1. Te recomiendo que uses “constantes” para devolver estos
# valores.

    def calcularIMC(self, peso, altura):
        resultado = peso/(altura^2)

        if resultado<20:
            return -1
        elif 20<=resultado<=25:
            return 0
        elif resultado<25:
            return 1
        
# esMayorDeEdad(): indica si es mayor de edad, devuelve un booleano.
    def esMayorDeEdad(self,edad):
        if edad<18:
            return "Es menor de edad"
        else:
            return "Es mayor de edad"

# • comprobarSexo(char sexo): comprueba que el sexo introducido es correcto.
# Si no es correcto, sera H. No sera visible al exterior.
    def comprobarSexo(self, sexo):
        if sexo==self.__sexo:
            return "Es correcto"
        else:
            return self.setsexo('H')

# • toString(): devuelve toda la información del objeto como String en un
# formato elegido por usted.

    # def toString(self):
    #     return "Nombre",{}.
    def __str__(self):
        return """\
    Nombre: {}
    Edad: {}
    Sexo: {}
    DNI:{}
    Peso: {}
    Altura:{} """.format(self.__nombre, self.__edad, self.__sexo,self.__dni,self.__peso,self.__altura)


# • generaDNI(): genera un número aleatorio de 8 cifras. Este método sera
# invocado cuando se construya el objeto. Puedes dividir el método para que
# te sea más fácil. No será visible al exterior.

    def __generaDNI(self):
        dni = random.randint(9999999, 1000000000)