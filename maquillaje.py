print ("hecho por: brenda estephany camacho hernandez")
productos = []

CONTRASENA = "controlZ" 

def pedir_contraseña():
    """Función que pide la contraseña y verifica si es correcta."""
    intentos = 0
    while intentos < 3:
        contrasena_ingresada = input("Introduce la contraseña: ")
        if contrasena_ingresada == CONTRASENA:
            print("Contraseña correcta. Accediendo al sistema...")
            return True
        else:
            intentos += 1
            print("Contraseña incorrecta. Intentos restantes:", 3 - intentos)
    print("Número máximo de intentos alcanzado. El programa se cerrará.")
    return False

def mostrar_menu():
    """Muestra las opciones del menú"""
    print("\n1. Altas (Insertar nuevo producto)")
    print("2. Bajas (Eliminar producto)")
    print("3. Consulta (Mostrar productos)")
    print("4. Modificación (Editar producto)")
    print("5. Salir")

def agregar_producto():
    """Agrega un nuevo producto a la lista de productos"""
    marca = input("Marca: ")
    tipo_producto = input("Tipo de Producto: ")
    tono_color = input("Tono/Color: ")
    presentacion = input("Presentación: ")
    cantidad = float(input("Cantidad: "))
    precio = float(input("Precio: "))
    fecha_expiracion = input("Fecha Expiración: ")
    stock = int(input("Stock: "))
    descripcion = input("Descripción: ")
    codigo_producto = input("Código Producto: ")

    producto = {
        "Marca": marca,
        "Tipo de Producto": tipo_producto,
        "Tono/Color": tono_color,
        "Presentación": presentacion,
        "Cantidad": cantidad,
        "Precio": precio,
        "Fecha Expiración": fecha_expiracion,
        "Stock": stock,
        "Descripción": descripcion,
        "Código Producto": codigo_producto
    }

    productos.append(producto)

def eliminar_producto():
    """Elimina un producto de la lista"""
    consultar_productos()
    if productos:
        codigo_producto = input("Código del producto a eliminar: ")
        producto_a_eliminar = None
        for producto in productos:
            if producto["Código Producto"] == codigo_producto:
                producto_a_eliminar = producto
                break
        if producto_a_eliminar:
            productos.remove(producto_a_eliminar)

def consultar_productos():
    """Muestra todos los productos registrados"""
    if productos:
        print("{:<15} {:<15} {:<10} {:<15} {:<10} {:<10} {:<20} {:<10} {:<20} {:<15}".format(
            "Marca", "Tipo Producto", "Tono/Color", "Presentación", "Cantidad", "Precio", 
            "Fecha Expiración", "Stock", "Descripción", "Código Producto"))
        for producto in productos:
            print("{:<15} {:<15} {:<10} {:<15} {:<10} {:<10} {:<20} {:<10} {:<20} {:<15}".format(
                producto["Marca"], producto["Tipo de Producto"], producto["Tono/Color"], 
                producto["Presentación"], producto["Cantidad"], producto["Precio"], 
                producto["Fecha Expiración"], producto["Stock"], producto["Descripción"], 
                producto["Código Producto"]))
    else:
        print("No hay productos disponibles.")

def modificar_producto():
    """Permite modificar un producto ya existente"""
    consultar_productos()
    if productos:
        codigo_producto = input("Código del producto a modificar: ")
        producto_a_modificar = None
        for producto in productos:
            if producto["Código Producto"] == codigo_producto:
                producto_a_modificar = producto
                break
        if producto_a_modificar:
            marca = input(f"Marca ({producto_a_modificar['Marca']}): ")
            tipo_producto = input(f"Tipo de Producto ({producto_a_modificar['Tipo de Producto']}): ")
            tono_color = input(f"Tono/Color ({producto_a_modificar['Tono/Color']}): ")
            presentacion = input(f"Presentación ({producto_a_modificar['Presentación']}): ")
            cantidad = input(f"Cantidad ({producto_a_modificar['Cantidad']}): ")
            precio = input(f"Precio ({producto_a_modificar['Precio']}): ")
            fecha_expiracion = input(f"Fecha Expiración ({producto_a_modificar['Fecha Expiración']}): ")
            stock = input(f"Stock ({producto_a_modificar['Stock']}): ")
            descripcion = input(f"Descripción ({producto_a_modificar['Descripción']}): ")

            producto_a_modificar["Marca"] = marca if marca else producto_a_modificar["Marca"]
            producto_a_modificar["Tipo de Producto"] = tipo_producto if tipo_producto else producto_a_modificar["Tipo de Producto"]
            producto_a_modificar["Tono/Color"] = tono_color if tono_color else producto_a_modificar["Tono/Color"]
            producto_a_modificar["Presentación"] = presentacion if presentacion else producto_a_modificar["Presentación"]
            producto_a_modificar["Cantidad"] = float(cantidad) if cantidad else producto_a_modificar["Cantidad"]
            producto_a_modificar["Precio"] = float(precio) if precio else producto_a_modificar["Precio"]
            producto_a_modificar["Fecha Expiración"] = fecha_expiracion if fecha_expiracion else producto_a_modificar["Fecha Expiración"]
            producto_a_modificar["Stock"] = int(stock) if stock else producto_a_modificar["Stock"]
            producto_a_modificar["Descripción"] = descripcion if descripcion else producto_a_modificar["Descripción"]

def main():
    """Función principal que maneja la ejecución del programa"""
    if not pedir_contraseña():
        return 

    while True:
        mostrar_menu()
        try:
            opcion = int(input("Selecciona una opción (1-5): "))
        except ValueError:
            continue

        if opcion == 1:
            agregar_producto()
        elif opcion == 2:
            eliminar_producto()
        elif opcion == 3:
            consultar_productos()
        elif opcion == 4:
            modificar_producto()
        elif opcion == 5:
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    main()