def generar_productos(cantidad_productos):
    lista = []
    for i in range(cantidad_productos):
        mini_lista = []
        id = int(input("Digite el ID del producto: "))
        nombre = input("Digite nombre del producto: ")
        categoria = input("Digite categoría del producto: ").lower()
        precio = int(input("Digite el precio del producto: "))
        stock = int(input("Digite el stock del producto: "))
        mini_lista.extend([id, nombre, categoria, precio, stock])
        lista.append(mini_lista)
    return lista

def generar_proveedor(cantidad_proveedores):
    lista = []
    for i in range(cantidad_proveedores):
        mini_lista = []
        nombre = input("Digite el nombre del proveedor: ")
        apellido = input("Digite el apellido del proveedor: ")
        telefono = input("Digite el número del proveedor: ")
        categoria = input("Digite la categoría de productos que comercializa: ")
        precio = int(input("Digite el precio por unidad: "))
        stock = int(input("Digite el stock disponible del proveedor: "))
        print()
        mini_lista.extend([nombre, apellido, telefono, categoria, precio, stock])
        lista.append(mini_lista)
    return lista

def verificar_stock_compra(cant_comprar, categoria, lista):
    booleano = True
    stock = 0
    for i in lista:
        if i[2].lower() == categoria.lower():
            if i[4] >= cant_comprar:
                booleano = True
            else:
                booleano = False
                stock = i[4]
    return booleano, stock

def generar_clientes(lista_productos):
    lista = []
    mini_lista = []
    nombre = input("Digite el nombre del cliente: ")
    apellido = input("Digite el apellido del cliente: ")
    dni = int(input("Digite el DNI del cliente: "))
    telefono = int(input("Digite el teléfono del cliente: "))
    categoria = input("Digite la categoría del producto: ")
    cantidad = int(input("Digite la cantidad a comprar: "))
    
    verificar, stock = verificar_stock_compra(cantidad, categoria, lista_productos)
    while not verificar:
        print(f"Cantidad no disponible, stock actual: {stock}")
        cantidad = int(input("Digite la cantidad a comprar: "))
        verificar, stock = verificar_stock_compra(cantidad, categoria, lista_productos)
    print()
    
    mini_lista.extend([nombre, apellido, dni, telefono, categoria, cantidad])
    lista.append(mini_lista)
    return lista
