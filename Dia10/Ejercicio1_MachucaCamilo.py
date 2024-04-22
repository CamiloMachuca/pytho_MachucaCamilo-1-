#--------------------------------
#-------- DIA 10 PYTHON--------
#--------------------------------

nums=[]# se crea una lista vacia para ingresar los numeros 
nums= input()
target=int(input())#se pide al usuario que agregue el numero target
contador=0# se crea un contador que va a iniciar desde cero
for i in range(len(nums)):# se crea un bucle for para encontrar al numero que es igual al numero ingresado por el usuario
    contador+=1

    if i==target:# se encuentra el numero y se imprime la posicion de ese numero 
       contador=contador-1
       print(contador-1)

#Desarrollado por Camilo Machuca Vega TI 1090397640






        
