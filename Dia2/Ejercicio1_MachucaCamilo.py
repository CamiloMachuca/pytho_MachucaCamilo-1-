#--------------------------------
#---- DIA 2 PYTHON
#--------------------------------
print("Este programa trata sobre realizar la serie de fibonacci  la cual consiste en una serie infinita de números naturales que empieza con un 0 y un 1 y continúa añadiendo números que son la suma de los dos anteriores hasta llegar en este caso al valor dado por el usuario  ")
while True:
    n = int(input("ingrese un numero entero el cual va a marcar el numero de veces que se va a repetir la serie fibonacci:"))
    a = 0
    b = 1
    c = 1
    while c <= n:
        if c % 2 == 1:
            print(a, end=",")
            a += b
        else:
            print(b, end=",")
            b += a 
        c += 1
    Repetir_programa = input("\n¿Quieres repetir el programa? (si o no): ")
    if Repetir_programa.lower() != "si":
        break
    
  #Desarrollado por Camilo Machuca Vega TI 1090397640