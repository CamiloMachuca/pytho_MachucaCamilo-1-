import json

with open('large-file.json', encoding="utf-8") as openfile:
    miJSON= json.load(openfile)
print(miJSON)

crearEventos=[]
print(len(miJSON))

for i in miJSON:
    if (miJSON[i]['type']=='createEvent'):
        crearEventos.append(miJSON[i])

for q in crearEventos:
    print("Eventos de creacion")
    print("ID",q ['id'])
    print("typo",q ['Event'])

for q in range (5):
    print("Eventos de creacion")
    print("ID:", crearEventos[q]['id'])
    print("tipo",crearEventos[q] ['type'])
    print("Actor")
    print("ID:", crearEventos[q]['actor']['id'])

    print("evento",q+1,)


with open("eventos.json","w") as outfile:
    json.dump(crearEventos,outfile)


