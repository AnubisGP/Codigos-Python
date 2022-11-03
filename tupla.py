t = (23,'a',(2.5,3.7,'x'),["perrito","gatito"],'Pepe')
print (t)
print (len(t))

print ('=====================================')
print (t[0]) #Imprime la llave ubicado en [0] es decir= 23
print (t[3]) #Imprime la lalve en [3] es decir= "Perrito,"gatito"
print (t[1:3])#Imprime la llave [1]= "a" y su siguiente.
print (t[3][1])#Toma dentro de la llave [3] el valor [1] // ([0][1])

print ('====================================')
print (t[3])
t[3].append('lorito')
print (t)
#Agrega a la llave [3] la palabra 'lorito'
print ('====================================')
for elemento in t:
    print (elemento)
#Imprime las llaves como si fuera una lista.
print ('====================================')
for index in range(0,len(t)):
    print (t[index])
#Imprime la lista desde la lalve seleccionada, la 0
#Se puede imprimir desde la 1,2,3 etc para mostrar la lista desde esa llave en adelante.
print ('====================================')
if 'a' in t:
    print ("El elemento 'a' esta en la tupla")
#Define que "a" esta en la tupla, si se cambia este elemento el mensaje no se imprimira.
print ('====================================')
lista=list(t)
lista[1]='A'
print (lista)

tupla=tuple(lista)
print (tupla)
#Hace que la letra A se vuelva mayuscula.
print ('====================================')
l = [(1,1), (2,4), (3,9), (4,16), (5,25)]
for x, y in l:
    print (x, ':', y)
#Crea una lista numerica en la que colocara valores numericos en orden.
