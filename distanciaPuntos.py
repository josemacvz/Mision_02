# Autor: José Luis Macías Vázquez, A01655713, Grupo 03
# Calcula la distancia entre dos puntos en una gráfica.

puntoUnoX = int(input("Digite X del puinto uno: "))
puntoUnoY = int(input("Digite Y del puinto uno: "))
puntoDosX = int(input("Digite X del puinto dos: "))
puntoDosY = int(input("Digite Y del puinto dos: "))

distancia =(((puntoDosX-puntoUnoX)**2)+ ((puntoDosY-puntoUnoY)**2))**0.5

print("Distancia: %.3f"% distancia)

