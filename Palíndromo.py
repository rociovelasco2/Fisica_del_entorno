class Pila:
    def __init__(self):
        self.pila = []
    def esVacia(self):
        return not self.pila
    def apilar(self, elemento):
        self.pila.append(elemento)
    def cima(self):
        if not self.esVacia():
            return self.pila[-1]
        else:
            print("Error. No se puede consultar la cima porque está vacía.")
    def desapilar(self):
        if not self.esVacia():
            return self.pila.pop()
        else:
            print("Error!. No se puede desapilar porque la pila está vacía")
        return None
    
def VerificarPalindromo(cadena):
    pila = Pila()
    longitud = len(cadena)
    for i in range(longitud // 2): #Apilamos la primera mitad de la palabra
        pila.apilar(cadena[i])
    if longitud % 2 == 0:
        inicio_segunda_mitad = longitud // 2
    else:
        inicio_segunda_mitad = longitud // 2 + 1

    for i in range(inicio_segunda_mitad, longitud): #Apilamos la segunda mitad de la palabra
        if pila.desapilar() != cadena[i]:
            return False

    return True #Si coinciden, es palindromo
      
cadena = input("Introduzca una palabra: ")

if VerificarPalindromo(cadena):
    print(f"{cadena} es un palíndromo.")
else:
    print(f"{cadena} no es un palíndromo.")      
      
            
    