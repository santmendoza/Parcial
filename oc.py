
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


script, conjunto1, conjunto2 = argv

c1=Validar(conjunto1)
c2=Validar(conjunto2)
c1.val_sintaxis(c1.conjunto1)
c2.val_sintaxis(c2.conjunto1)










