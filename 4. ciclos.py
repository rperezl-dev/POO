class Ciclos:
    def __init__(self, num1 = 5):
        self.numero=num1 #variables de instancia

    def usoWhile(self):
        # ciclo repetitivo que se ejecuta por verdadero y sale por falso
        car = input('Ingrese una vocal: ')
        car=car.lower()
        while car not in('a','e','i','o','u'):
            car=input('Ingrese vocal: ').lower()
        print('¡Felicidades! el caracter: {} es una vocal'.format(car))
ciclo1 = Ciclos()
ciclo1.usoWhile()