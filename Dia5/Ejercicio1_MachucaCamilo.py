#--------------------------------
#-------- DIA 5 PYTHON--------
#--------------------------------

T=input("ingrese el numero de veces que se va a repetir el caso")# es la cantidad de veces que se va a repetir el caso
n=input("ingrese la cantidad de numeros que va a tener la lista")# n va a ser por el numero que lo va a dividir
numeros=input("ingrese los numeros de la lista separandolos con comas")# se le pide la lista al usuario
lista=[numeros]# se pasan los numeros que dio el usuario a una lista
pares=[]
menor= min(lista) 
mayor=max(lista)
contador=0
ai=menor 
aj= mayor 
I=0
for i in range(T):
    

    if lista>=ai:
        pares=[ai,lista]
        contador+=1
    if lista<=aj:
        pares=[aj,lista]
        contador+=1

    if 1<=lista:
        I=(lista)

    if lista:
        pares=[ai+aj]





#Desarrollado por Camilo Machuca Vega TI 1090397640







