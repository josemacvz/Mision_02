# Autor: José Luis Macías Vázquez, A01655713, Grupo 03
# Descripcion: Entrega la cuenta más propina e IVA y el desgloce de cada cargo.

# Escribe tu programa después de esta línea.

subtotal = int(input("Digite el total de la cuenta: "))
propina = subtotal*1.13
iva = subtotal*1.16
totalAPagar = subtotal+(propina-subtotal)+(iva-subtotal)

print("Costo de su comida: $",subtotal)
print("Propina: $",propina-subtotal)
print("IVA: $",iva-subtotal)
print("Total a pagar: $",totalAPagar)


