#--------------------------------
#-------- DIA 3 PYTHON--------
#--------------------------------
#Se le da la vienvenida al usuario 
print("Bienvenido querido usuario")
#se da una explicacion del programa
print("Bueno la idea de este programa es que el usuario nos proporcione un numero y que el programa verifique si es un numero primo o no")
#se crea un arreglo donde se almacenan las opciones
arreglo=["1=verificar un numero", "2=Detener el programa", "3=Obtener informacion adicional"]
#Defino un boleano como verdadero 
booleano=True
#Inicio del siclo while en donde si booleano es verdadero seguir con el programa
while booleano==True:
    print("A continuacion se presenta el menu de opciones ")
    print(arreglo)# extraigo las opciones guardadas en el arreglo y las muestro al usuario
    n=input(print("Escriba la opcion a elegir por ejemplo si es la 1=uno, 2=dos, 3=tres en texto"))
    
    if n=="uno":#si n es igual a opcion uno entonces seguir a este programa
        print("Esta es la opcion para verificar un numero ingrese el numero")
        while True:#mientras que el bucle while sea verdadero ejecutar el siguiente programa
            numero= int(input())# defini la variable del usuario con el nombre: numero
            primo=True#defini primo como verdadero 

            for i in range(2, numero):#este bucle for va a ser el encargado de saber si el numero es primo o no
               if numero% i == 0:# si al dividirlo por los diferentes numeros hasta llegar al numero ingresado por el usuario la divicion no es exacta o en este caso el residuo no es cero entonces es un numero primo
                 primo= False# segun el resultado de la acterior divicion depende si primo es falso o verdadero
                 
               

            if primo:# si el resultado anterior es verdadero entonces el numero es primo porque el residuo de la divicion no es igual a cero
                print("El numero es primo")

            else:# A qui es todo lo contrario el residuo si es igual a cero entonces no es un numero primo
                print("El numero no es primo")
            break

    elif n=="dos":#Esta es la segunda opcion que puede elegir el usuario en la cual hay un mensaje de despedida
        print("Muchas gracias por aver participado en este programa")
        print("Hasta la proxima")
        booleano= False# cambie el valor de booleano a false para terminar el programa 

    else:# Esta es la tercera opcion en la cual hay una breve explicacion de los numeros primos
        print("Recuerda que Los números primos son aquellos que solo son divisibles entre ellos mismos y el 1, es decir, que si intentamos dividirlos por cualquier otro número, el resultado no es entero o igual a cero ")
        print("programa desarrollado por Camilo Machuca Vega")

print("")
print("segundo programa ")
print("Bienvenido al programita ")
print("en este programita podras crear una contraseña segun tus gustos y muy segura")
print("Para generar la contraseña se requiere que especifiques cuantas mayusculas,caracteres alfanumerico,sinbolos,minusculas quieres que tenga la contraseña")
mayusculas=["M","B","C","A","H","D","T","K","O","L"]#seccreo un arreglo que almacenara las mayusculas

caracteresAlfanumerico=[1,"a",3,"q",5,"b",7,"r",9,"t"]#se creo un arreglo que almacenara los caracteres

simbolos=["|","#","$","/","!","?","&","¡","#","/"]#se creo un arreglo que almacenara los simbolos
generador=[]# se creo un arreglo bacio para que me guardara la cantidad de letras mayusculas que queria el usuario
generadorC=[]# se creo un arreglo bacio para que me guardara la cantidad de caracteres que queria el usuario
generadorS=[]# se creo un arreglo bacio para que me guardara la cantidad de simbolos que queria el usuario
arregloo=["1=Añadir letras mayusculas, 2= añadir caracteres alfanumericos, 3=añadir simbolos"]
boole=True
while boole==True:
    print("A continuacion se presenta el menu de opciones ")
    print(arregloo)# extraigo las opciones guardadas en el arreglo y las muestro al usuario
    op=input(print("Escriba la opcion a elegir por ejemplo si es la 1=uno, 2=dos, 3=tres en texto"))

    if op=="uno":#si n es igual a opcion uno entonces seguir a este programa
        print("Esta es la opcion para añadir la cantidad de letras mayusculas que quiere que tenga la contraseña")
        print("Ingrese cuantas mayusculas quieres que tenga tu contraseña")

        M= int(input())# se recibe el valor dado por el usuario
        for i in range(M):# se realiza el conteo hasta la cantidad dada por el usuario
         print(mayusculas[i+1])
         generador= [mayusculas[i]]#se realiza el ingreso de la cantidad de letras que el usuario requiera a otro arreglo

    elif op=="dos":
        print("Esta es la opcion para añadir los caracteres alfanumericos")
        Caracteres= int(input())# se recibe el valor dado por el usuario
        for i in range(Caracteres):# se realiza el conteo hasta la cantidad dada por el usuario
         print(caracteresAlfanumerico[i+1])
        
         generadorC= [caracteresAlfanumerico[i]]#se realiza el ingreso de la cantidad de caracteres que el usuario requiera a otro arreglo

    else:
       print("Ingrese cuantos simbolos quiere que tenga la contraseña")
       simb=int(input())# se recibe el valor dado por el usuario
       for i in range(simb):# se realiza el conteo hasta la cantidad dada por el usuario
         print(simbolos[i+1])
        
         generadorS=[simbolos[i]]


         totalll=[(generador, generadorC,generadorS)]# se agrupan todos los criterios que el usuario quiere para su contraseña en un arreglo
    
         for i in range(1):
        
           print(totalll)  # se procede a mostrar la contraseña creada
            #se le pregunta al usuario si quiere repetir el programa
    print("quieres repetir el programa(si o no)")
    fin=input()

    if fin=="si":
        boole= True# si la respuesta es si se boole sigue siendo verdadero

    elif fin=="no":# si la respuesta es no se finaliza el programa ya que boole pasa a ser falso
        boole=False


#Desarrollado por Camilo Machuca Vega TI 1090397640

    
    




