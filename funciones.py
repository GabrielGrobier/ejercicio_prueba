

#contruccion de funcion agregar productos, donde es una funcion con parametro
#que recibe la lista productos 
def agregar_producto(productos):
    #se solicita al usuario el nombre del producto
    nombre= input("Nombre del producto").lower()
    #se solicita al usuario la cantidad del producto escrito
    cantidad = int(input("Ingrese la cantidad de producto"))
    #se solicita el precio 
    precio = int(input("Ingrese el precio del producto"))
    #con la funcion append se guarda los elementos dentro de la lista en una estructura de
    #diccionario
    productos.append({
        'nombre':nombre,
        'cantidad':cantidad,
        'precio':precio
    })
    print("Productos Guardados ")
    print(productos)

#funcion eliminar producto 
def eliminar_producto(productos):
    #se solicita el nombre del producto a eliminar 
    nombre = input("ingrese el producto que desea eliminar : ").lower()
    #se recorre la lista y se guarda los valores de los indices en producto
    for producto in productos:
        #se comprueba que exista el valor dentro de la lista 
        if producto['nombre'] == nombre:
            print("producto encontrado : ")
            print(f'nombre {producto['nombre']} Cantidad : {producto['cantidad']}')
            #se elimina el valor encontrado 
            productos.remove(producto)
            print("producto eliminado ")
        
#actualizar cantidad 
def actualizar_cant(productos):
    #se solicita el nombre 
    nombre = input("ingrese el producto a actualizar : ").lower()
    #se ingresa y recorre la lista 
    for producto in productos:
        #si el nombre escrito por el usuario existe 
        if producto['nombre'] == nombre:
            print(f'nombre {producto['nombre']} Cantidad : {producto['cantidad']}')
            #se pide la cantidad a actualizar del producto encontrado 
            cantidad = int(input("ingrese la cantidad nueva : "))
            #se actualiza la cantidad 
            producto['cantidad']= cantidad
            print("producto actualizado ")
            
        
#mostrar productos 
def Mostrar_invt(productos):
    #con metodo for se recorre toda la lista y se muestra 
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