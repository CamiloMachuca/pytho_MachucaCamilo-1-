#--------------------------------
#-------- DIA 8 PYTHON--------
#--------------------------------


frutas={}# se crea un diccionario vacio en el cual se va a agregar la lista de frutas
buliano=True
while buliano:
    nombre=input("Ingrese el nombre de la fruta: ")
    precio=int(input("Ingrese el precio de la fruta: "))
    cantidad=int(input("Ingrese la cantidad disponible de la fruta: "))
    frutas[nombre]={"precio":precio,"cantidad": cantidad}# se guardan los datos en el diccionario
    
    respuesta=input("Quieres ingresar otra fruta (si o no):")# se da la opcion de agregar mas frutas
    if respuesta=="no":
        buliano=False

fruta_max_cantidad = max(frutas.items(), key=lambda x: x[1]["cantidad"])#Se encuentra la fruta con la mayor cantidad disponible utilizando la función max(), pasando como argumento los elementos del diccionario frutas  
# se  utiliza una función lambda para seleccionar el valor de "cantidad" de cada fruta.
print()
print("La fruta con la mayor cantidad disponible es:", fruta_max_cantidad[0])
print("Cantidad disponible:", fruta_max_cantidad[1]["cantidad"])
print()
#Se ordenan las frutas en el diccionario frutas en orden decreciente según su valor total
frutas_ordenadas = sorted(frutas.items(), key=lambda x: x[1]["precio"] * x[1]["cantidad"], reverse=True)
# se muestra el contenido del diccionario frutas ordenado por valor total
print("se ordenaron las frutas de forma decreciente de acuerdo a su valor total:")
print()
for nombre, datos in frutas_ordenadas:
    print(f"{nombre}: Precio: {datos['precio']}, Cantidad: {datos['cantidad']}, Valor Total: {datos['precio'] * datos['cantidad']}")

#Desarrollado por Camilo Machuca Vega TI 1090397640








