huespedes={101:'Juan Valdes', 105:'Paquita la del Barrio', 202: 'Mariana Pajon'} 



print (huespedes) # Imprime las claves y los valores.
print (huespedes.items()) #Se convierte en una lista.

print (huespedes.keys()) # Imprime solo las claves.
for key in huespedes:
    print (key) # Imprime las claves una bajo la otra.

print (huespedes.values()) # Imprime solo los valores.
for key in huespedes:
    print (huespedes[key]) # Imprime los valores uno bajo el otro.
print()

for habitacion in huespedes:
    print (habitacion,':',huespedes[habitacion])
print() #Hace que las claves cambien a "Habitacion" y los valores a "huspedes" imprimiendo una simulacion de habitacion para su respectivo huesped.

for habitacion,huesped in huespedes.items():
    print (habitacion,':',huespedes[key]) #Imprime en todos las claves un mismo valor.
    
for indice, key in enumerate(huespedes):
    print (indice+1,key,huespedes[key])
print() # Se suma 1 antes de las claves y los valores para crear una lista de 1 a 3 con la habitacion y huesped correspondiente

print (huespedes[105])
print (huespedes.get(105)) #Imprime el valor 105 (Paquita la del Barrio)
    
print ('====================================')

huespedes[102]='Fanny Lu'
huespedes[107]='Don Omar'
huespedes.setdefault('109','Luis Miguel') #Se añadio nuevas claves y valores al diccionario.

for huesped in huespedes.items():
    print (habitacion,':',huesped)
print() #Imprime los nuevos huspedes y diccionarios como si estuvieran registrados en un mismo "recibo" pero con su diferencia de clave y valor siguen.

registroshoy={201:'Vicente Fernandez',301:'Pepe Guardiola'}
huespedes.update(registroshoy)
for habitacion, huesped in huespedes.items():
    print (habitacion,':',huesped)
print() #Imprime nuevas claves y valores.

print ('====================================')

huespedes[107]='Ricky Martin'
print (huespedes)
#Añade una nueva clave y valor dentro de los existenten en orden de menor a mayor utilizando el numero designado en la clave.
print ('====================================')

del huespedes[102]
huespedes.pop(202)
print(huespedes)
# ¿Imprime las claves impares?
print ('====================================')

copia1=huespedes.copy()
print ('copia1: ',copia1)
copia2={}
copia2.update(huespedes)
print ("copia2: ",copia2)
# Crea dos copias de la lista de impares.
print ('====================================')

lista=[2,5,7,1]
diccio=dict.fromkeys(lista,"xxx")
print(diccio)
# Crea 4 claves con su respectivo valor.
print ('====================================')

inventario={"plata": (500,2500), 'cartera' : ["Cedula","Moneda","Boletas"],'mecato':'Detodito','dias':1}
print (inventario)
inventario["cartera"].sort() #Imprime la seccion de "cartera" en orden alfabetico

print(inventario)
print(inventario.get("plata")[0]) #Imprime la clave.
