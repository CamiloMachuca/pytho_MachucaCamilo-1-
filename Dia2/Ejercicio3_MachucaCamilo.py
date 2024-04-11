#--------------------------------
#---- DIA 2 PYTHON
#--------------------------------
import random

randomNumero=random.randint(1,100)
intentos=0

print("Bienvenido al jueguito de adivinar el numero secreto en 10 intentos ")

while intentos <= 10:
    print(f"Intentos{intentos}")

    intentos= int(input())
    intentos+=1

    if intentos< randomNumero:
        print("El numero ingresado es muy bajo")
    elif intentos> randomNumero:
        print("El numero ingresado es muy alto")

    else:
        break

if intentos == randomNumero:
    print(f"FELICIDADES Adivinaste el numero el numero es {randomNumero}")
else:
    print(f"PERDISTEEE, el numero era {randomNumero}")

    #Desarrollado por Camilo Machuca Vega TI 1090397640