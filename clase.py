# Autor: tuNombreCompleto, tuMatricula
# Descripcion: Texto que describe en pocas palabras el problema que estás resolviendo.

# Escribe tu programa después de esta línea.

mujeres = int(input("Escriba el número de mujeres inscritas: "))
hombres = int(input("Escriba el número de hombres inscritos: "))

totalDeAlumnosI = hombres+mujeres

porcentajeMujeres = (100*mujeres)/totalDeAlumnosI
porcentajeHombres =(100*hombres)/totalDeAlumnosI

print("Total de inscritos:  ",totalDeAlumnosI)
print("Porcentaje de mujeres:",porcentajeMujeres,"%")
print("Porcentaje de hombres:",porcentajeHombres,"%")


