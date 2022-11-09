es1={"Codigo":1,"Nombre":"Juan", "Apellido":"Aguirre", "Notas":{"Taller":5.0,"Quiz":4.5,"Parcial":4.2}}
es2={"Codigo":2,"Nombre":"Maria", "Apellido":"Socorro", "Notas":{"Taller":4.7,"Quiz":3.9,"Parcial":4.2}}
es3={"Codigo":3,"Nombre":"Jesus", "Apellido":"Zabate", "Notas":{"Taller":3.2,"Quiz":4.8,"Parcial":4.2}}
es4={}

bucle=0
while bucle==0:
    opcion= int(input("----------------------------\nPara ingresar a la informacion oprima el número asignados\n0, Estudiante nuevo\n1, Informacion completa del estudiante 1\n"
                  "2, Informacion completa del estudiante 2\n3, Informacion completa del estudiante 3\n4, Agregar un nuevo estudiante\n"
                  "5, Modificar informacion de un estudiante\n6, Promedios, mayor y menor."
                  "\n9, Salir\nIngrese la opcion que desea aqui: "))

    if opcion == 0:
        print("----------------------------")
        print("Estudiante",es4)
        print("----------------------------")

    elif opcion == 1:
        print("----------------------------")
        print("Estudiante\n",es1)
        print("----------------------------")

    elif opcion == 2:
        print("----------------------------")
        print("Estudiante\n",es2)
        print("----------------------------")

    elif opcion == 3:
        print("----------------------------")
        print("Estudiante\n",es3)
        print("----------------------------")

    elif opcion == 4:
        print("----------------------------")
        es4["Codigo"]=4
        es4["Nombre"]=str(input("Ingrese el nombre del estudiante: "))
        es4["Apellido"]=str(input("Ingrese el apellido del estudiante: "))
        print("Asignacion de notas")
        es4["Notas"]={"Taller":float(input("Ingrese nota de Taller: ")),"Quiz":float(input("Ingrese la nota del Quiz: ")),
                  "Parcial":float(input("Ingrese nota del Parcial"))}
        print("----------------------------")
        print("Estudiante Añadido\n",es4)
        print("----------------------------")

    elif opcion == 5:
        print("----------------------------")
        print("Seleccione el estudiante al cual quiere modificar la informacion")
        modificar= int(input("0, Estudiante 0 \n1, Estudiante 1 \n2, Estudiante 2 \n3, Estudiante 3"
                             "\nIngrese la opcion que desea aqui: "))

        if modificar == 0:
                print("----------------------------")
                print("INICIO DE MODIFICACION")
                es4["Codigo"]=4
                es4["Nombre"]=str(input("Ingrese el nombre del estudiante: "))
                es4["Apellido"]=str(input("Ingrese el apellido del estudiante: "))
                print("Asignacion de notas")
                es4["Notas"]={"Taller":float(input("Ingrese nota de Taller: ")),"Quiz":float(input("Ingrese la nota del Quiz: ")),
                  "Parcial":float(input("Ingrese nota del Parcial"))}
                print("----------------------------")

        elif modificar == 1:
                print("----------------------------")
                print("INICIO DE MODIFICACION")
                es1["Codigo"]=1
                es1["Nombre"]=str(input("Ingrese el nombre del estudiante: "))
                es1["Apellido"]=str(input("Ingrese el apellido del estudiante: "))
                print("Asignacion de notas")
                es1["Notas"]={"Taller":float(input("Ingrese nota de Taller: ")),"Quiz":float(input("Ingrese la nota del Quiz: ")),
                  "Parcial":float(input("Ingrese nota del Parcial"))}
                print("----------------------------")

        elif modificar == 2:
                print("----------------------------")
                print("INICIO DE MODIFICACION")
                es2["Codigo"]=2
                es2["Nombre"]=str(input("Ingrese el nombre del estudiante: "))
                es2["Apellido"]=str(input("Ingrese el apellido del estudiante: "))
                print("Asignacion de notas")
                es2["Notas"]={"Taller":float(input("Ingrese nota de Taller: ")),"Quiz":float(input("Ingrese la nota del Quiz: ")),
                  "Parcial":float(input("Ingrese nota del Parcial"))}
                print("----------------------------")

        elif modificar == 3:
                print("----------------------------")
                print("INICIO DE MODIFICACION")
                es2["Codigo"]=3
                es2["Nombre"]=str(input("Ingrese el nombre del estudiante: "))
                es2["Apellido"]=str(input("Ingrese el apellido del estudiante: "))
                print("Asignacion de notas")
                es2["Notas"]={"Taller":float(input("Ingrese nota de Taller: ")),"Quiz":float(input("Ingrese la nota del Quiz: ")),
                              "Parcial":float(input("Ingrese nota del Parcial"))}
                print("----------------------------")

    elif opcion == 6:
        print("----------------------------")
        promedio = sum(es4["Notas"].values())/3
        print(es4)
        print("Tiene un promedio de: ",promedio)
        print("----------------------------")
        promedio1 = sum(es1["Notas"].values())/3
        print(es1)
        print("Tiene un promedio de: ",promedio1)
        print("----------------------------")
        promedio2 = sum(es2["Notas"].values())/3
        print(es2)
        print("Tiene un promedio de: ",promedio2)
        print("----------------------------")
        promedio3 = sum(es3["Notas"].values())/3
        print(es3)
        print("Tiene un promedio de: ",promedio3)
        print("----------------------------")
        print("----------------------------")
        print("Promedios del mayor al menor")
        lista_promedios=[promedio,promedio2,promedio3,promedio1]
        lista_promedios.sort()
        primero=lista_promedios[0]
        ultimo=lista_promedios[len(lista_promedios) - 1]
        print("El mejor promedio es: ",ultimo)
        print("El menor promedio es: ",primero)
        print("----------------------------")

    elif opcion == 9:
        print("Gracias por usarnos\nHasta pronto")
        break
    
