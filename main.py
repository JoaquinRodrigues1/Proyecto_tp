from funciones import ordenar_matriz_burbujeo, mostrar_matriz

#encabezado columnas
encabezados = ["Producto", "Stock", "Precio"]
matriz = []

#carga de datos
n = int(input("¿Cuántos productos querés cargar? "))

for i in range(n):
    print(f"\nProducto #{i + 1}")
    nombre = input("Nombre del producto: ")
    stock = int(input("Stock disponible: "))
    precio = float(input("Precio unitario ($): "))
    matriz.append([nombre, stock, precio])

#muestra la matriz original
print("\nMatriz original:")
mostrar_matriz(matriz, encabezados)

#selecciona la matriz a ordenar
print("\n¿Según qué columna querés ordenar?")
for i, titulo in enumerate(encabezados):
    print(f"{i} - {titulo}")

col = int(input("Número de columna: "))

#valida y ordena la mart
if 0 <= col < len(encabezados):
    ordenar_matriz_burbujeo(matriz, col)
    print(f"\nMatriz ordenada por '{encabezados[col]}':")
    mostrar_matriz(matriz, encabezados)
else:
    print("Columna inválida.")
