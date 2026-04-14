# Retroalimentación GA2
# Jonathan Gabriel Morales Torres "10"
# Mercadito

barras = int(input("Introduce el número de filas vendidas que no son frescas: "))
precio = 3.49

descuento = 0.6
coste = barras * precio * (1 - descuento)
print("El coste de una fila fresca es " + str(precio) + "Q")
print("El descuento sobre una fila no fresca es " + str(descuento * 100) + "%")
print("El coste final a pagar es " + str(round(coste, 2)) + "Q")