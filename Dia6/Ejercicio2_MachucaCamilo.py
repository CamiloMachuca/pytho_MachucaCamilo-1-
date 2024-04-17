#--------------------------------
#-------- DIA 6 PYTHON--------
#--------------------------------
def funcion_numeros(numeros, target): #se crea la funcion para encontrar los dos numeros 
    lugar=[]
    contador=(0)
    for i in range(len(numeros) - 1):# bucle para buscar los dos numeros que sumados me den igual a returt
        
        

        for j in range(i + 1, len(numeros)): # se verifica si la suma de numeros[i] y numeros[j] es igual a returt
            
            
            if numeros[i] + numeros[j] == target:# Retornar los dos números que al sumarlos son iguales a returt
                
               
                return (numeros[i], numeros[j]) # Si no se encuentran números que al sumarlos den igual a target se reinicia el siclo hasta encontrarlo
contador=(0)



def main(): # se define a main para que se ejecute en primera instancia ya que de alli sale los valores para la funcion
    
    lista = input()# se le pide la lista de numeros al usuario
    
    numeros = list(map(int,lista.strip().split(","))) #se pasan los numeros dados por el usuario a una lista y se separan las cadenas en donde estan las comas con split

    target = int(input())#se le pide al usuario el numero que quiere que encuentre la pareja a sumar y que sea igual a target

    
    suma = funcion_numeros(numeros, target)# se busca los dos números que sumen igual a starget

    if suma:# se muestra el resultado
        print(f" {suma[0]}, {suma[1]}")
        
   


if __name__ == "__main__":# se ejecuta la función main si este es el módulo principal a realizarse
    main()


#Desarrollado por Camilo Machuca Vega TI 1090397640















    








