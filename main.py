#se traer funciones desde archivo funciones.py
import funciones as fn
#contruccion de lista vacia para almacenar datos 
productos = []
#menu 
while True:
    print('''
          1.- Añadir producto 
          2.- Eliminar producto 
          3.- actualizar Cantidad 
          4.- Mostrar inventario 
          5.- Buscar producto 
          6.- Salir
          ''')
    op=int(input("Selecciona una opcion : "))
    #validacion opcion seleccionada por el usuario 
    if op ==1:
        #llama a funcion agregar producto que esta almacenada en el archivo funciones.py
        fn.agregar_producto(productos)
    
    if op == 2:
        #llama a funcion Eliminar_producto que esta almacenada en el archivo funciones.py
        fn.eliminar_producto(productos)
    if op ==3:
        #llama a funcion actualizar_cant que esta almacenada en el archivo funciones.py
        fn.actualizar_cant(productos)
    if op ==4:
        #llama a funcion Mostrar_invt que esta almacenada en el archivo funciones.py
        fn.Mostrar_invt(productos)
    if op ==5:
        #llama a funcion buscar_productos que esta almacenada en el archivo funciones.py
        fn.buscar_productos(productos)
    if op ==6:
        break