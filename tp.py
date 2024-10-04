# Trabajo Practico "Programacion a la Par"

# Constantes

lista_productos = [
    ["Chupetin Sable de Luz", 50, 200],
    ["Agua La Fuerza", 35, 3200],
    ["Gomitas Holocubo", 25, 990],
    ["Barrita de Cereal Wookie", 48, 2500],
    ["Galletitas R2D2", 20, 15800]
]

continuar = "1"

# Funciones
def validar_opcion(opcion_elegida: str) -> int:
    while opcion_elegida.isdigit() == False:
        opcion_elegida = input("Error, ingrese una respuesta valida: ")
    
    opcion_elegida = int(opcion_elegida)
    while opcion_elegida < 1 or opcion_elegida > 4:
        opcion_elegida = validar_opcion(input("Error, ingrese la respuesta: "))
    return opcion_elegida

def agregarProducto(nombre: str, stock: int, precio: int) -> list:
    listaAgregado = []
    listaAgregado.append(nombre)
    listaAgregado.append(stock)
    listaAgregado.append(precio)
    return listaAgregado

def mostrarProductos(listaProductos):
    num = 0
    for i in range(len(listaProductos)):
        num += 1
        print(f"{num} Producto: {listaProductos[i][0]} / Stock: {listaProductos[i][1]} / Precio: {listaProductos[i][2]}") 
    return ""
    
def validar_producto(productoElegido: str) -> int:
    while productoElegido.isdigit() == False:
        productoElegido = input("Error, ingrese el Nro del producto: ")
    
    productoElegido = int(productoElegido)
    while productoElegido < 1 or productoElegido > len(lista_productos):
        productoElegido = validar_producto(input("Error, ingrese el Nro del producto: "))
    return productoElegido

def validar_stock(stockElegido: str, producto: int) -> int:
    stock_maximo = lista_productos[producto - 1][1]
    while stockElegido.isdigit() == False:
        stockElegido = input("Error, ingrese el stock: ")
    
    stockElegido = int(stockElegido)
    while stockElegido > stock_maximo:
        stockElegido = validar_stock(input("Error, no hay suficiente stock, vuelva aingresar el stock: "), producto)
    return stockElegido
 
def restar_stock(stock: int, producto: int) -> int:
    resta_stock = lista_productos[producto - 1][1] - stock
    return resta_stock

def validar_respuesta(respuesta: str) -> int:
    while respuesta.isdigit() == False:
        respuesta = input("Error, ingrese una respuesta valida: ")
    
    respuesta = int(respuesta)
    while respuesta < 1 or respuesta > 2:
        respuesta = validar_respuesta(input("Error, ingrese la respuesta: "))
    return respuesta

# Codigo
while continuar == "1":

    print("[1] Consultar Inventario")
    print("[2] Agregar producto al inventario")
    print("[3] Realizar Compra")
    print("[4] Terminar")
    opcion_elegida = input("Respuesta: ")
    opcion = validar_opcion(opcion_elegida)
    
    if opcion == 1:
        print(mostrarProductos(lista_productos))
        
    elif opcion == 2:
        nombre = input("Ingrese el nombre del producto: ")
        stock = int(input("Ingrese stock del producto: "))
        precio = int(input("Ingrese el precio del producto: "))
        listaAgregada = agregarProducto(nombre, stock, precio)
        print(f"Nuevo producto añadido al inventario: {nombre}")
        lista_productos.append(listaAgregada)
        print("El inventario actualizado es: ")
        mostrarProductos(lista_productos)
    
    elif opcion == 3:
        print("Lista de productos disponibles:")
        mostrarProductos(lista_productos)
        productoElegido = input("Seleccione el producto: ")
        producto = validar_producto(productoElegido)
        
        stockElegido = input("Ingrese el stock a comprar: ")
        stock = validar_stock(stockElegido, producto)
        
        stock_a_restar = restar_stock(stock, producto)
        lista_productos[producto - 1][1] = stock_a_restar
        mostrarProductos(lista_productos)
        print(f"El total a pagar es: {stock * lista_productos[producto - 1][2]}")
    
    elif opcion == 4:
        print("Hasta luego.")
        break
    else:
        print("No elegiste una opcion valida.")


    print("[1] Volver al Menu Principal [2] Terminar")
    seguir = input("Respuesta: ")
    respuesta = validar_respuesta(seguir)
    if respuesta == 1:
        continuar = "1"
    else:
        print("Hasta luego.")
        continuar = False

