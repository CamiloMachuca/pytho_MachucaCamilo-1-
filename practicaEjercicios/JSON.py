
import json

datos = {"nombre": "Camilo", "edad": 19, "ciudad": "Cucuta"} # se crea un diccionario

# se convierte el diccionario a Json 
json_datos = json.dumps(datos)
print(json_datos)

# se convierte Json a un diccionario
diccionario_Json= json.loads(json_datos)
print(diccionario_Json)

