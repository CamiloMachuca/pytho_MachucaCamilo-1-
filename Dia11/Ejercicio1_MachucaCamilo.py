#--------------------------------
#-------- DIA 11 PYTHON--------
#--------------------------------
import json


# se extrae el Json y se pasan a la variable datos
with open("C:/Users/USUARIO/Documents/large-file.json",encoding="utf-8") as file:
    datos = json.load(file)

    

buliano=True
while buliano==True:# se crea un bucle while para proceder con los siguientes puntos del menu
    print("===MENU===")#se crea el menu de opciones
    print("(1)revisar Eventos")
    print("(2)crear")
    print("(3)actualizar")
    print("(4)eliminar")
    print("(5)salir del programa")
    opcion= input("Ingrese la opcion deseada: ")


    if opcion=="1":
        if datos:
            print("=====Eventos=====")
            for i, evento in enumerate (datos, 1):# se imprimen todos los eventos que haigan en la variable datos
                print(f"{i}. {evento["type"]} -{evento["id"]}")# se imprimen con su llave-valor 
        else:
            print("No hay eventos para mostrar")

    elif opcion=="2":
        eve= input("Ingrese el nuevo evento: ") 
        id= input("Ingrese el id del evento: ")
        nuevo_evento={"type": eve, "id": id}# se crea un diccionario con los datos ingresados por el usuario 
        datos.append(nuevo_evento)# se ingresa ese diccionario a la variable datos
        print("Se guardo correctamente el evento")

    elif opcion=="3":
        print("=====Eventos=====")
        for i, evento in enumerate (datos, 1):
            print(f"{i}. {evento["type"]} -{evento["id"]}")# se muestran los eventos
        llave= input("ingrese el id del evento que quieres actualizar")# se pide el id del avento a actualizar
        busqueda=False# se define busqueda como False para asi luego serrar el bucle for
        for evento in datos:
            if evento["id"]== llave:# se busca el evento con el mismo id que el usuario ingrese
                busqueda=True# si se encuentra se finaliza el programa
                nuevo_event= input("Ingrese el nuevo evento ")
                nuevo_id= input("Ingrese el nuevo ID del evento")
                evento["type"]=nuevo_event# se le asigna la llave del valor dado anteriormente por el usuario
                evento["id"]=nuevo_id# se le asigna la llave del valor dado anteriormente por el usuario
                print("Evento actualizado correctamente")

    elif opcion=="4":
        print("=====Eventos=====")
        for i, evento in enumerate (datos, 1):
            print(f"{i}. {evento["type"]} -{evento["id"]}")
        id_eliminar=input("Ingrese el id del evento a eliminar: ")# se pide el id del evento a eliminar 
        for evento in datos:# se busca el evento en la variable datos con el mismo id que el usuario ingrese
            if evento ["id"]== id_eliminar:
                datos.remove(evento)# se procede a eliminar ese evento
                print("Evento eliminado correctamente")
                
    elif opcion=="5":# se elimina el programa
        print("#######################################")
        print(" Se finalizo el programa gracias por participar")
        print("#######################################")
        buliano= False






