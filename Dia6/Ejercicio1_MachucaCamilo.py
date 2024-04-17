#--------------------------------
#-------- DIA 6 PYTHON--------
#--------------------------------
#Programa para eliminar el numero repetido de una lista
lista=input()# se guarda la lista dada por el usuario en una variable llamada lista

for i in range(100):
    listaSinRepetir=(sorted(set(lista)))# se organiza la lista de menor a mayor y se eliminan los numeros repetidos

print(listaSinRepetir)#se le muestra al usuario


#Desarrollado por Camilo Machuca Vega TI 1090397640