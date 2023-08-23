fecha = input("Ingrese el día y la fecha: ")
fecha = fecha.split()

dia = fecha[0]
dia = dia[0:dia.find(",")]
dia = dia.lower()
aux = fecha[1]
dd = int(aux[0:aux.find("/")])
mm = int(aux[aux.find("/")+1:])

if (dia == "lunes") or (dia == "martes") or (dia == "miercoles") or (dia == "jueves") or (dia == "viernes"):
    if dd <= 31 and mm <= 12:
        if (dia == "lunes") or (dia == "martes") or (dia == "miercoles"):
            print("Ese día hubo examen")
            aprob = int(input("Ingrese la cantididad de alumnos aprobados: "))
            des_aprob = int(input("Ingrese la cantididad de alumnos desaprobados:"))
            alumnos = aprob + des_aprob
            porc_aprob = (aprob * 100) / alumnos
            print(f"El porcentaje de alumnos aprobados es del {porc_aprob}%")
        if (dia == "jueves"):
            asist = int(input("Ingrese el porcentaje de asistencia a las clases habladas"))
            if asist >= 50:
                    print("asistió la mayoría")
            else:
                    print("No asistió la mayoría")
        if (dia == "viernes") and (dd == 1 and ( mm == 1 or mm == 7)):
            print("Comienzo de nuevo ciclo")
            print()
            alumnos_ingr = int(input("Ingrese la cantidad de alumnos ingresantes: "))
            cost_arancel = int(input("Ingrese el costo del arancel por alumno: $"))
            ingresos = alumnos_ingr * cost_arancel
            print(f"El ingreso total será de ${ingresos}")
            
    else:
        print("La fecha ingresada no es válida")
else:
    print("El día ingresado no es válido")

print()
print("Fin del programa")