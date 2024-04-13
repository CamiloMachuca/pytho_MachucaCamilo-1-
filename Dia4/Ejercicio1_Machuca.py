#--------------------------------
#-------- DIA 4 PYTHON--------
#--------------------------------
#Se le da la vienvenida al usuario 
print("Bienvenido usuario")
print("Este es un programita de cambio de $")

c10=(0)# se crea una variable que va a representar los 10c la cual va a ser igual a cero y va cambiando su valor de acuerdo a su uso 

c5=(0)# se crea una variable que va a representar los 5c la cual va a ser igual a cero y va cambiando su valor de acuerdo a su uso 

c1=(0)# se crea una variable que va a representar un 1c la cual va a ser igual a cero y va cambiando su valor de acuerdo a su uso 

print("Ingrese el dinero a cambiar")
cambio=int(input())# el cambio tiene que ser un numero entero para poder realizar un cambio

     
    
if cambio >= 10:#si cambio ingresado es mayor a 10 o igual se procede a ser lo siguiente 
    c10 = int(cambio/10);#se divide el dinero dado por el usuario y asi almacenar las veces que se necesito de 10c en un arreglo
    cambio=cambio%10# se procede a revisar si sobra algun residuo de la division para luego pasarlo a dividirlo en 5c o si no hay mas residuos se finaliza y se imprime la cantidad de veces que se divio en 10c

if cambio >= 5:# se divide el sobrante de la division anterior o en llegado caso el dinero a cambiar dado por el usuario para mirar cuantas veces se va a necesitar de 5c en esta ocasion 
    c5= int(cambio/ 5);# se divide y se procede a guardar las veces que se dividio el numero entre 5c en un arreglo
    cambi=cambio%5;# se procede a mirar si quedan residuos de la divicion 

if cambi >= 1:# si el residuo anterior es mayor o igual a 1c se procede a dividirlo hasta que sea igual a 0
    c1=int(cambi/1)# se realiza la divicion y se guarada las veces que fue necesario 1c en una variable
    

print("cambio de monedas de 10c es igual a:",str(c10),"en monedas de 5c es igual a:",str(c5)," en monedas de 1c es igual a:",str(c1));# se imprime el cambio que se le dara al usuario

print("Se finalizo el programa gracias por participar")

#Desarrollado por Camilo Machuca Vega TI 1090397640