from Validar import Validar
import sys

class Operador():

    def __init__(self,conjunto,conjunto2):
        self.conjuto1=conjunto1
        

    def validar(self,conjunto)
        
        
        


    def op_conjuntos(self, conjunto1, conjunto2):

        p=conjunto1.replace('{','').replace('}','').replace(',',' ')
        y=conjunto2.replace('{','').replace('}','').replace(',',' ')
        #print(p)
        #print(y)
        x=p[1:len(p)]
        a=y[1:len(y)]
        #print(x)
        #print(a)

        lista1=x.split()
        lista2=a.split()

        #print(lista1)
        #print(lista2)
        papa = set(lista1)
        arroz= set(lista2)
        #print(papa)
        #print(arroz)

        print("***Union de conjuntos****")
        print (papa.union(arroz))
        print("==============================")

        # Diferencia entre conjuntos
        print("***Diferencia de conjuntos***")
        print (papa - arroz)
        print (arroz - papa)
        print("==============================")


    


