import funciones as fn
productos = []
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
    
    if op ==1:
        fn.agregar_producto(productos)
    if op == 2:
        fn.eliminar_producto(productos)
    if op ==3:
        fn.actualizar_cant(productos)
    if op ==4:
        fn.Mostrar_invt(productos)
    if op ==5:
        fn.buscar_productos(productos)
    if op ==6:
        break