


def agregar_producto(productos):
    nombre= input("Nombre del producto")
    cantidad = int(input("Ingrese la cantidad de producto"))
    precio = int(input("Ingrese el precio del producto"))
    productos.append({
        'nombre':nombre,
        'cantidad':cantidad,
        'precio':precio
    })
    print("Productos Guardados ")
    print(productos)


def eliminar_producto(productos):
    nombre = input("ingrese el producto que desea eliminar : ").lower()
    for producto in productos:
        if producto['nombre'] == nombre:
            print("producto encontrado : ")
            print(f'nombre {producto['nombre']} Cantidad : {producto['cantidad']}')
            productos.remove(producto)
            print("producto eliminado ")
        

def actualizar_cant(productos):
    nombre = input("ingrese el producto a actualizar : ").lower()
    for producto in productos:
        if producto['nombre'] == nombre:
            print(f'nombre {producto['nombre']} Cantidad : {producto['cantidad']}')
            cantidad = int(input("ingrese la cantidad nueva : "))
            producto['cantidad']= cantidad
            print("producto actualizado ")
            
        

def Mostrar_invt(productos):
    for producto in productos:
            print(f"Nombre : {producto['nombre']} ")
            print(f"Cantidad : {producto['cantidad']} ")
            print(f"Precio  : {producto['precio']} ")
            print("############################")
        

def buscar_productos(productos):
    nombre = input("ingrese el nombre del producto que deseas buscar : ")
    for producto in productos:
        if producto['nombre']==nombre:
            print(f"Nombre : {producto['nombre']} ")
            print(f"Cantidad : {producto['cantidad']} ")
            print(f"Precio  : {producto['precio']} ")
            print("############################")