#--------------------------------
#-------- DIA 9 PYTHON--------
#--------------------------------

productos=[]# creo una variable vacia

buliano=True
while buliano==True:
    print("====MENU====")# imprimo un menu de opciones para el usuario
    print("(1)Agregar  productos al carrito")
    print("(2) ver los productos del carrito")
    print("(3)Salir del programa")
    
    opcion=input("Ingrese la opcion deseada: ")

    if opcion=="1":# pido los requerimientos del producto
        nombre=input("Ingrese el nombre del producto: ")
        precio=input("Ingrese el precio del producto: ")
        cantidad=input("Ingrese la cantidad del producto: ")

        productoo={ "nombre":nombre,"precio": precio,"cantidad": cantidad,}# cree un diccionario para almacenar el producto dado por el usuario
        productos.append(productoo)# paso el producto a la lista
        print("Se agrego correctamente al carrito")

    elif opcion=="2":# muestro al usuario los productos que hay en el carrito
        print("Los productos que hay en el carrito son:")
        for i in productos:
            print(f"Nombre: {i["nombre"]}, precio: {i["precio"]}, Cantidad: {i ["cantidad"]}")# imprimo los productos que esten en la lista productos

    else:# opcion para cerrar el programa
        print("Gracias Hasta luego")
        buliano=False








#Desarrollado por Camilo Machuca Vega TI 1090397640


