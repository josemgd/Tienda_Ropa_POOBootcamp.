class Producto:
    def __init__(self, nombre, precio):
        self._nombre = nombre
        self._precio = precio

    def obtener_info(self):
        return f'{self._nombre}: ${self._precio}'

class Camisa(Producto):
    def __init__(self, nombre, precio, talla):
        super().__init__(nombre, precio)
        self._talla = talla

    def obtener_info(self):
        return f'{super().obtener_info()}, Talla: {self._talla}'

class Pantalon(Producto):
    def __init__(self, nombre, precio, talla):
        super().__init__(nombre, precio)
        self._talla = talla

    def obtener_info(self):
        return f'{super().obtener_info()}, Talla: {self._talla}'

class Zapato(Producto):
    def __init__(self, nombre, precio, talla):
        super().__init__(nombre, precio)
        self._talla = talla

    def obtener_info(self):
        return f'{super().obtener_info()}, Talla: {self._talla}'

class Categoria:
    def __init__(self, nombre):
        self._nombre = nombre
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def mostrar_productos(self):
        for producto in self.productos:
            print(producto.obtener_info())

class Tienda:
    def __init__(self):
        self.categorias = []
        self.carrito = []

    def agregar_categoria(self, categoria):
        self.categorias.append(categoria)

    def mostrar_menu(self):
        print("\n--- Seleccione una de las opciones de la tienda---")
        while True:
            print("1. Ver categorias")
            print("2. Ver carrito")
            print("3. Procesar compra")
            print("4. Salir")
            opcion = input("Seleccione una opcion: ")
            print("-"*20)

            if opcion == "1":
                self.mostrar_categorias()
            elif opcion == "2":
                self.ver_carrito()
            elif opcion == "3":
                self.procesar_compra()
            elif opcion == "4":
                print("Gracias por su compra.")
                break
            else:
                print("Opcion no valida, intente de nuevo.")

    def mostrar_categorias(self):
        for i, categoria in enumerate(self.categorias):
            print(f"{i+1}. {categoria._nombre}")
        seleccion = int(input("Seleccione una categoria: ")) - 1
        if 0 <= seleccion < len(self.categorias):
            self.mostrar_productos_categoria(self.categorias[seleccion])
        else:
            print("Categoria no válida.")
            print("-"*20)

    def mostrar_productos_categoria(self, categoria):
        categoria.mostrar_productos()
        producto_seleccionado = int(input("Seleccione el numero del producto para agregar al carrito: ")) - 1
        if 0 <= producto_seleccionado < len(categoria.productos):
            self.carrito.append(categoria.productos[producto_seleccionado])
            print("Producto agregado al carrito.")
            print("-"*20)
        else:
            print("Selección no valida.")
            print("-"*20)

    def ver_carrito(self):
        if not self.carrito:
            print("El carrito esta vacio.")
            print("-"*20)
        else:
            print("\n--- Carrito ---")
            for producto in self.carrito:
                print(producto.obtener_info())
                print("-"*20)

    def procesar_compra(self):
        if not self.carrito:
            print("El carrito esta vacio, no se puede procesar la compra.")
            print("-"*20)
        else:
            print("\n--- Procesando su compra ---")
            total = sum(producto._precio for producto in self.carrito)
            print(f"El total de su compra es: ${total}")
            print("-"*20)
            self.carrito.clear()

camisas = Categoria("Camisas")
camisas.agregar_producto(Camisa("1. Camisa Amarilla", 120000, "M"))
camisas.agregar_producto(Camisa("2. Camisa Blanca", 120000, "M"))
camisas.agregar_producto(Camisa("3. Camisa Celeste", 130000, "L"))

pantalones = Categoria("Pantalones")
pantalones.agregar_producto(Pantalon("1. Pantalon tipo vaquero", 220000, "32"))
pantalones.agregar_producto(Pantalon("2. Pantalon elegante", 100000, "34"))

zapatos = Categoria("Zapatos")
zapatos.agregar_producto(Zapato("1. Zapato negro casual", 200000, "41 al 43"))
zapatos.agregar_producto(Zapato("2. Zapato blanco deportivo", 140000, "44 al 46"))
zapatos.agregar_producto(Zapato("3. Zapato elegante", 200000, "41 al 43"))

tienda = Tienda()
tienda.agregar_categoria(camisas)
tienda.agregar_categoria(pantalones)
tienda.agregar_categoria(zapatos)

tienda.mostrar_menu()