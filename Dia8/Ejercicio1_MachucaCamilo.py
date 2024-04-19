#--------------------------------
#-------- DIA 8 PYTHON--------
#--------------------------------
print("=====Bienvenido al programa de suscripciones=====")
Año=50# se le da un valor a la variable año
buli=True
buliano=True
definir=True
Dinero=(0)
suscripcionesRegaladas=(0)
compra=(0)
compras_realizadas=[]
regaladas=[]
while definir:

    
    print("===MENU===")#se crea el menu de opciones
    print("(1)comprar suscripcion")
    print("(2)iniciar sesion")
    print("(3)regalar una suscripcion")
    print("(4)mostrar suscripciones compradas y regaladas")
    print("(5)cerrar programa")
    opcion= input("Ingrese la opcion que desees:")
    if opcion=="1":# comprar suscripcion
        
        while buliano:# se crea un bucle while para pedir al usuario que ingrese un año de acuerdo a las limitaciones dadas

         año=int(input("ingrese el año en el que quieres subscribirse:"))
         if 1990<año<2020:
            print("año valido")
            buliano= False
         else:
            print("Año no valido para subscribirse")

        nombreComprador=input("Ingresa tu nombre: ")# se pide el nombre del comprador
        print("Ingrese la cantidad de subscripciones a comprar")
        compra=int(input())# se le pide la cantidad de suscripciones a comprar y se almacena en la variable compra
        totalCompra= compra*Año
        
        if totalCompra<=Dinero:# se observa si el dinero alcanza para realizar la compra 
           
           print("se compro correctamente las suscripciones")
           Dinero=Dinero-totalCompra
           compras_realizadas.append((nombreComprador, compra))
           
        elif totalCompra> Dinero:
           print("Dinero insuficiente para realizar la suscripcion")
           

    elif opcion=="2":# se crea una cuenta o una sesion 
        nombre=input("ingresa tu nombre: ")
        Dinero=int(input("Ingrese el dinero que quieras ingresar a la cuenta: "))
        print("sesion realizada correctamente")

        
    elif opcion=="3":# se regala suscripciones
       NombreRegalo=input("Ingrese el nombre de la persona a la cual le vas a regalar la suscripcion: ")
       suscripcionesRegaladas=int(input("Ingrese la cantidad de suscripciones a regalar: "))
       regaladas.append((NombreRegalo, suscripcionesRegaladas))# se agregan los datos a una lista

       
       while buli:# se verifica el año que este dentro de las limitaciones 

         año_Regalo=int(input("ingrese el año en el que lo quieres subscribir: "))
         if 1990<año_Regalo<2020:
            print("año valido")
            print("compra de suscripcion realizada")
            buli= False
         else:
            print("Año no valido para subscribirse")

    elif opcion=="4":# se muestran las suscripciones compradas 
       print("Las suscripciones compradas:")
       for nombre, cantidad in compras_realizadas:
          print(f"{nombre} compro {cantidad} suscripciones")
          print()
       

       print("suscripciones regaladas:")
       for nombre, cantidad in regaladas:
          print(f"{nombre} recibio {regaladas} suscripciones")

       
      

    elif opcion=="5":# se finaliza el programa
       print("Gracias por utilizar este programa")
       definir=False

#Desarrollado por Camilo Machuca Vega TI 1090397640

        




        