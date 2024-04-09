#--------------------------------
#---- DIA 1 CHEAT SHEET PYTHON ------
#--------------------------------

#Imprimir hola mundo
print("Hola mundoooooooooooooo!!!")

#Datos primitivos

#Numero
numerito = 1 #nombreVariable = valor
print(numerito) #imprimir(variable)
print(type(numerito)) #imprimir(tipo(variable))

#Decimal
numeritoDecimal = 1.1
print(numeritoDecimal)
print(type(numeritoDecimal))

#Booleano
miBooleanito = True
print(miBooleanito)
print(type(miBooleanito))

#Cadena de texto
texto = "MI TIBU"
print(texto)
print(type(texto))

#Ingresa por teclado la infomarcion
# pedir que el usuario ingresara su nombre para asi saludarlo
print("Hola ¿cual es tu nombre?")
nombre=input()
print("mucho gusto,", nombre)


#Conversion de tipos de variable
# string
X= 10
X=str(X)
print(type(X))

#De string a flotante
x= "10"
x=float(X)
print(type(X))

#De flotante a entero
X= 10.0
X= int(X)
print(type(X))

#De entero a Booleano
X= 10
X=bool(X)
print(type(X))




#Bucles For y While
#Bucle for
for i in range(3):
    print(i)
    print("se completo el bucle for")

#while
contador=0
while contador<5:
    contador+=1
    print("se completo el bucle while")
   

#Funciones (4 Tipos)
#Funcion con parametro sin retorno
def suma(total):
    total=(1+1)
    print(total)
    
#Funcion con parametro y retorno
def suma(numero):
    return numero+numero
resultado= suma(20)
print(resultado)

#Funcion sin parametros con retorno
def saludo():
    return "¡hola!"
saludo= saludo()
print(saludo)


#Funcion sin parametros ni retorno
print("Final del programa")


#Desarrollado por Camilo Machuca Vega TI 1090397640