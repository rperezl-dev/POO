#class Sintaxis:
#    def useVariables(self):
#        edad,_peso = 50, 70.50
#        print(edad, _peso)

#ejer1 = Sintaxis()
#ejer1.useVariables()

class Sintaxis:
    instancia=0 #variables de clases(opcional)
    #__init__: metodo constructor que se ejecuta cuando se instancia la clase cuyo
    #objetivo es crear e inicializar los atributos de la clase,
    #self es un objeto que representa la clase creada
    def __init__(self, dato = 'Inicialización'):
        self.frase=dato #variables de instancia
        #Sintaxis.instancia = Sintaxis.instancia+1

    def usoVariables(self):
        edad,_peso = 50, 70.5
        nombres = 'Daniel Vera'
        Tipo_sexo = 'M'
        civil = True
        #tuplas = () son colecciones de datos de cualquier tipo-inmutables
        usuario=()
        usuario = ('dchiki', 1234, 'chiki@gmail.com', True)
        #usuario[3]= 'Milagro'
        #listas = [] colecciones mutables
        materias = []
        materias = ['Programacion Web', 'PHP', 'POO']
        materias[1] = 'Python'
        materias.append('Go')
        #diccionario = {} colecciones de objetos clave:valor - tipo json
        docente={'nombre': 'Daniel', 'edad':50, 'fac':'faci'}
        docente['carrera']='CS'
        #presentacion con format
        #print('''Mi nombre es {}, tengo {}
        #      años'''.format(nombres, edad))
        #print(usuario, materias, docente)
        #print(usuario, usuario[0], usuario[0:2], usuario[-1])
        #print(materias, materias[2:], materias[:3], materias[:], materias[-2:])
        print(docente, docente['nombre'])

ejer1 = Sintaxis() #Se crea un objeto que es una instancia de la clase y se ejecuta el constructor
ejer1.usoVariables()