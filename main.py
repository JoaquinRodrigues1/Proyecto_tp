from funciones import *

cantidad_productos = int(input("Ingrese la cantidad de productos a cargar: "))
lista_productos = generar_productos(cantidad_productos)
print()
cantidad_proveedores = int(input("Ingrese la cantidad de proveedores a cargar: "))
lista_proveedores = generar_proveedor(cantidad_proveedores)

clientes = []

#menu
    elegir_opcion = int(input("""\n
1. Cargar Cliente
2. Ver información segun ID de producto
3. Ver todos los productos
4. Ver todos los clientes
5. Salir
Elija una opción: """))

    if elegir_opcion == 1:
        cliente = generar_clientes(lista_productos)[0]
        clientes.append(cliente)

    elif elegir_opcion == 2:
        id_buscar = int(input("Digite el ID del producto: "))
        encontrado = False
        for i in lista_productos:
            if i[0] == id_buscar:
                print(f"ID: {i[0]}, Nombre: {i[1]}, Categoria: {i[2]}, Precio: {i[3]}, Stock: {i[4]}")
                encontrado = True
        if not encontrado:
            print("Producto no encontrado.")

    elif elegir_opcion == 3:
        print("\nListado de productos:")
        for i in lista_productos:
            print(f"ID: {i[0]}, Nombre: {i[1]}, Categoria: {i[2]}, Precio: {i[3]}, Stock: {i[4]}")

    elif elegir_opcion == 4:
        print("\nListado de clientes:")
        for c in clientes:
            print(f"Nombre: {c[0]} {c[1]}, DNI: {c[2]}, Teléfono: {c[3]}, Categoría: {c[4]}, Cantidad: {c[5]}")

    elif elegir_opcion == 5:
        print("Saliendo del sistema. . .")
        break

    else:
        print("Opción inválida Intente nuevamente.")
