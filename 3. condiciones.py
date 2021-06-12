class Condicion:
    contador = 0
    def __init__(self, num1 = 0, num2 = 1):
        self.numero1 = num1 #variables de instancia
        self.numero2 = num2 #variables de instancia
        #numero = num1 + num2
        self.numero3 = num1
    def usoIf(self):
        if self.numero1 == self.numero2:
            # if...elif...else...: permiten condicionar la ejecucion de uno o varios bloques
            # de sentencias al cumpliento de una o varias condiciones.
            print('número1: {}, número2: {} son iguales.'.format(self.numero1,self.numero2))
        elif self.numero1 == self.numero3:
            print('número1: {}, número3: {} son iguales.'.format(self.numero1, self.numero3))
        else:
            print('No son iguales.')

#usar clase
#cond1=Condicion()
#print(cond1,numero1)
#print(cond1,numero2)

cond2 = Condicion(10, 10)
cond2.usoIf()#llamada a uun metodo de la clase
print(cond2.numero1)#llamada a un atributo de la clase