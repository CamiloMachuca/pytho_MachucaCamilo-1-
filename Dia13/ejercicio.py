#!/usr/bin/python
# -*- coding: utf-8 -*-
import json

buliano=True# se define una variable para un bucle while para asi poder cerrar el bucle 
variable=True# se define una variable para un bucle while para asi poder cerrar el bucle 
contador=0


def abrirArchivo():# se crea una funcion para abrir el Json 
    miJSON=[]
    with open('info.json','r') as openfile:
        miJSON= json.load(openfile)
    return miJSON

def guardarArchivo(miData):# se crea una funcion para guardar los cambios que le realizemos al Json
    with open("info.json","w") as outfile:
        json.dump(miData,outfile)

while variable==True:# se inicia el bucle principal

    print("################")# se le da el menu de opciones al usuario
    print("## PLATAFORMA DE GESTION ##")
    print("################")
    print("")
    print("Hola! Por favor escoge alguna de las opciones:\n1.Revisar estudiantes\n2.Modificar estudiante\n3.crear estudiante\n4.eliminar estudiante\n5.salir del programa")
    x=int(input("Cual opción escoges:"))# se pide al usuario que ingrese una opcion
    miInfo=[]# se crea una lista vacia en donde se van a guardar los datos y a trabajar con ellos
    if(x==1):
        
        miInfo=abrirArchivo()# se llaman a los datos que hay en el Json para asi previamente mostrarlos
        n=int(input("Ingrese el numero de la posicision del grupo el cual quieres observar los estudiantes (0,1): "))
        for i in miInfo[n]["estudiantes"]:
            
            print("################")# se imprimen los datos de los estudiantes
            print("ID:",i["id"])
            print("Nombre:",i["nombre"])
            print("Apellido:",i["apellido"])
            print("Edad",i["edad"])
            print("Fecha de Nacimiento (DD-MM-AAAA):",i["fechaNacimiento"])
            print("Cédula:",i["cedula"])
            print("E-mail:",i["email"])
            print("GitHub:",i["github"])
            print("################")
            print("")
            
    elif(x==2):
        m=int(input("Ingrese el numero del grupo del cual quieres modificar los estudiantes (0,1): "))
        miInfo=abrirArchivo()
        contador=0
        for i in miInfo[m]["estudiantes"]:# se muestran los datos de los estudiantes de un grupo predeterminado por el usuario
            contador = contador +1
            print("################")
            print(" ESTUDIANTE #",contador)
            print("ID:",i["id"])
            print("Nombre:",i["nombre"])
            print("Apellido:",i["apellido"])
            print("Edad",i["edad"])
            print("Fecha de Nacimiento (DD-MM-AAAA):",i["fechaNacimiento"])
            print("Cédula:",i["cedula"])
            print("E-mail:",i["email"])
            print("GitHub:",i["github"])
            print("################")
            print("")
        contador=0
        estudiante = int(input("Cual numero de identificacion vas a cambiar?"))# se pide el id para buscarlo y actualizar al estudiante con el mismo id
        while buliano==True:# se crea un bucle while para que el usuario puede elegir que dato quiere cambiar las veces que el requiera
            datoCambiar=int(input("Que te gustaría cambiar del estudiante:\n1.Apellido, \n2.Nombre, \n3.Edad, \n4.FechaNacimiento, \n5.Cedula, \n6.Email, \n7.Github, \n: "))
            if (datoCambiar==1):
                nuevoApellido = input("Ingresa el nuevo apellido:")
                miInfo[0]["estudiantes"][estudiante-1]["apellido"] = nuevoApellido
                guardarArchivo(miInfo)
                print("Cambio realizado!")
                
            elif (datoCambiar==2):
                nuevoNombre = input("Ingresa el nuevo nombre:")
                miInfo[0]["estudiantes"][estudiante-1]["nombre"] = nuevoNombre
                guardarArchivo(miInfo)
                print("Cambio realizado!")
            elif (datoCambiar==3):
                nuevoEdad = int(input("Ingresa el nuevo edad:"))
                miInfo[0]["estudiantes"][estudiante-1]["edad"] = nuevoEdad
                guardarArchivo(miInfo)
                print("Cambio realizado!")
            elif (datoCambiar==4):
                NuevofechaNacimiento =input("Ingresa la nueva fecha de nacimiento:")
                miInfo[0]["estudiantes"][estudiante-1]["fechaNacimiento"] = NuevofechaNacimiento
                guardarArchivo(miInfo)
                print("Cambio realizado!")
            elif (datoCambiar==5):
                NuevoCedula =input("Ingresa el nuevo numero de cedula:")
                miInfo[0]["estudiantes"][estudiante-1]["cedula"] = NuevoCedula
                guardarArchivo(miInfo)
                print("Cambio realizado!")
            elif (datoCambiar==6):
                NuevoEmail =input("Ingresa el nuevo Email:")
                miInfo[0]["estudiantes"][estudiante-1]["email"] = NuevoEmail
                guardarArchivo(miInfo)
                print("Cambio realizado!")
            elif (datoCambiar==7):
                NuevoGithub =input("Ingresa el nuevo Github :")
                miInfo[0]["estudiantes"][estudiante-1]["github"] = NuevoGithub
                guardarArchivo(miInfo)
                print("Cambio realizado!")
            opc=input("Te gustaria cambiar algo mas (si o no)")# se le da la opcion de cambiar otro dato 
            if opc=="no":
                buliano=False
    elif(x==3):

        miInfo=abrirArchivo()

        crearEstudiante={}# se crea un diccionario vacio para guardar los datos del nuevo estudiante
        crearEstudiante["id"]=len (miInfo[0]["estudiantes"])+1# se crea el id automaticamente ya que ese representa el lugar que tome el estudiante
        crearEstudiante["nombre"]=input("ingrese el nombre del estudiante: ")
        crearEstudiante["apellido"]=input("ingrese el apellido del estudiante: ")
        crearEstudiante["edad"]=int(input("Ingrese la edad del estudiante: "))
        crearEstudiante["fechaNacimiento"]=input("Ingrese la fecha de nacimiento: ")
        crearEstudiante["cedula"]=input("ingrese la cedula del estudiante: ")
        crearEstudiante["email"]= input("Ingrese el correo electronico: ")
        crearEstudiante["github"]=input("Ingrese el usuario de github: ")

        N=int(input("En que grupo quieres añadir al estudiante (0,1): "))# se le da la opcion al usuario para añadirlo a cualquier grupo que el quiera

        miInfo[N]["estudiantes"].append(crearEstudiante)# se añade el estudiante al grupo elegido por el usuario
        guardarArchivo(miInfo)# se guardan los datos al Json
        print("Se agrego correctamente el nuevo estudiante")
    elif(x==4):
        miInfo=abrirArchivo()# se llama a los datos del Json
        n=int(input("De que grupo desea eliminar un estudiante (0,1): "))
        for i in miInfo[n]["estudiantes"]:
            
            print("################")
            print("ID:",i["id"])
            print("Nombre:",i["nombre"])
            print("Apellido:",i["apellido"])
            print("Edad",i["edad"])
            print("Fecha de Nacimiento (DD-MM-AAAA):",i["fechaNacimiento"])
            print("Cédula:",i["cedula"])
            print("E-mail:",i["email"])
            print("GitHub:",i["github"])
            print("################")
            print("")
        id_eliminar =int(input("Ingrese el id del estudiante que quieres eliminar: "))# se pide que ingrese el id del estudiante a eliminar
        for i,estudiante in enumerate(miInfo[n]["estudiantes"]):# se busca la posicion del estudiante ya  que esta representa el id 
            if estudiante["id"]== id_eliminar:
                miInfo[n]["estudiantes"].pop(i)# se procede a eliminar al estudiante con el mismo id que ingrese el usuario utilizando la funcion pop
                guardarArchivo(miInfo)# se guardan los cambios en el Json
                print("Estudiante eliminado correctamente")
    elif(x==5):# se finaliza el programa
        print("=========Se finalizo el programa=========")
        variable=False

#Desarrollado por Camilo Machuca Vega TI 1090397640


    

