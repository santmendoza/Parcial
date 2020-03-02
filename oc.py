
from sys import argv

class Validar:

    def __init__(self,conjunto1):
        self.conjunto1 = conjunto1
        


    def val_sintaxis(self,conjunto):

        if conjunto.count(',,')==0 and conjunto.find(',')!=1 and conjunto.rfind(',')!=len(conjunto)-2  and conjunto.find('{')==0 and conjunto.rfind('}')==len(conjunto)-1 and conjunto.count('}')==1 and conjunto.count('{')==1:
        
            print("¡La sintaxis ingresada es la correcta!")
            
        else:
            print("error")
            exit()


class Operador(Validar):

    def __init__(self,conjunto,conjunto2):
        Validar.__init__ (self,conjunto)
        self.conjunto2=conjunto2

        
        


    def op_conjuntos(self, conjunto1, conjunto2):

        p=conjunto1.replace('{','').replace('}','').replace(',',' ')
        y=conjunto2.replace('{','').replace('}','').replace(',',' ')
        
        lista1=p.split()
        lista2=y.split()

       
        conjuntoa = set(lista1)
        conjuntob= set(lista2)
        

        print("***Union de conjuntos****")
        print (conjuntoa.union(conjuntob))
        print("==============================")

    
        print("***Diferencia de conjuntos***")
        print (conjuntoa - conjuntob)
        print("==============================")


objetoVacio = "#"
script, conjunto1, conjunto2 = argv

c1=Validar(conjunto1)
c2=Validar(conjunto2)
operacion=Operador(conjunto1,conjunto2)

c1.val_sintaxis(c1.conjunto1)
c2.val_sintaxis(c2.conjunto1)

operacion.op_conjuntos(conjunto1,conjunto2)















