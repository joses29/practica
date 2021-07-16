class Logica:
    def __init__(self,lista=None):
        self.__lista=lista

    @property
    def lista(self):
        return self._lista
    @lista.setter
    def lista(self,value):
        self.__lista=value
    
    def parImpar(self,numero):
        rec = numero%2
        if rec == 0:
            print("{} es par".format(numero))
        else:
            print("{} es Impar".format(numero))

    def perfecto(self,num):
        acu=0
        for contador in range(1,num):
            rec = num % contador
            if rec == 0:
                acu=acu+contador
        if acu == num:
            print("{} es perfecto".format(num))
        else:
            print("{} No es prefecto".format(num))


class Ejercicio(Logica):
    def __init__(self,lista,numeros):
        super().__init__(lista)
        self.dato=numeros 

    def sumar(self,n1,n2):
        return n1+n2

    def parImpar(self,numero):
        super().parImpar(numero)
        return numero%2

ejer = Ejercicio([1,3,5],20)
if ejer.parImpar(6) == 0:
    print("Par")
else:
    print("Impar")
print(ejer.lista)

#print(ejer.sumar(4,8))





 ent        pro                 sal
 num        obtener divisores   perf o no perfecto
  6          1 2 3=6
  8          1,2,4=7
  12         1,2,3,4,6

num    contador 
  12 % 1 = 0 
  si rec = 0

  12 % 2 = 0
  12 % 3 = 0
  12 % 4 = 0
  12 % 5 = 1
  12 % 6 = 0
  12 % 7 = 1
  12 % 8 = 1
  12 % 9 = 1
  12 % 10 = 1
  12 % 11 = 1