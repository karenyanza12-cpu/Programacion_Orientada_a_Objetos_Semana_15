class Restaurante:

    def __init__(self):

        self.productos = []
        self.usuarios = []
        self.ventas = []

        self.indice_productos = {}
        self.indice_usuarios = {}
        self.ventas_por_usuario = {}

    def reconstruir_indices(self):

        self.indice_productos = {
            producto.codigo: producto
            for producto in self.productos
        }

        self.indice_usuarios = {
            usuario.identificacion: usuario
            for usuario in self.usuarios
        }

        self.ventas_por_usuario = {}

        for venta in self.ventas:

            if venta.usuario_id not in self.ventas_por_usuario:

                self.ventas_por_usuario[
                    venta.usuario_id
                ] = []

            self.ventas_por_usuario[
                venta.usuario_id
            ].append(venta)

    # ---------------- PRODUCTOS ----------------

    def agregar_producto(
        self,
        producto
    ):

        if producto.codigo in self.indice_productos:

            raise ValueError(
                "Ya existe un producto con ese código."
            )

        self.productos.append(
            producto
        )

        self.indice_productos[
            producto.codigo
        ] = producto

    def listar_productos(self):

        return self.productos

    def buscar_producto(
        self,
        codigo
    ):

        return self.indice_productos.get(
            int(codigo)
        )

    def actualizar_producto(
        self,
        codigo,
        nombre,
        precio,
        stock,
        disponible
    ):

        producto = self.buscar_producto(
            codigo
        )

        if producto is None:

            raise ValueError(
                "No se encontró el producto."
            )

        producto.nombre = nombre
        producto.precio = precio
        producto.stock = stock
        producto.disponible = disponible

        return producto

    def eliminar_producto(
        self,
        codigo
    ):

        producto = self.buscar_producto(
            codigo
        )

        if producto is None:

            raise ValueError(
                "No se encontró el producto."
            )

        self.productos.remove(
            producto
        )

        del self.indice_productos[
            int(codigo)
        ]

    # ---------------- USUARIOS ----------------

    def agregar_usuario(
        self,
        usuario
    ):

        if usuario.identificacion in self.indice_usuarios:

            raise ValueError(
                "Ya existe ese usuario."
            )

        self.usuarios.append(
            usuario
        )

        self.indice_usuarios[
            usuario.identificacion
        ] = usuario

    def listar_usuarios(self):

        return self.usuarios

    def buscar_usuario(
        self,
        identificacion
    ):

        return self.indice_usuarios.get(
            str(identificacion)
        )

    # ---------------- VENTAS ----------------

    def agregar_venta(
        self,
        venta
    ):

        self.ventas.append(
            venta
        )

        if venta.usuario_id not in self.ventas_por_usuario:

            self.ventas_por_usuario[
                venta.usuario_id
            ] = []

        self.ventas_por_usuario[
            venta.usuario_id
        ].append(venta)

    def listar_ventas(self):

        return self.ventas

    def consultar_ventas_usuario(
        self,
        identificacion
    ):

        return self.ventas_por_usuario.get(
            str(identificacion),
            []
        )