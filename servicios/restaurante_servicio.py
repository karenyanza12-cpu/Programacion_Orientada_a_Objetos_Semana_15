from servicios.restaurante import Restaurante
from modelos.venta import Venta


class RestauranteServicio(Restaurante):

    def validar_login(
        self,
        usuario,
        contrasena
    ):

        return (
            usuario == "admin"
            and contrasena == "1234"
        )

    def registrar_venta(
        self,
        usuario_id,
        producto_codigo,
        cantidad,
        archivo_servicio
    ):

        usuario = self.buscar_usuario(
            usuario_id
        )

        if usuario is None:

            raise ValueError(
                "No existe el usuario seleccionado."
            )

        producto = self.buscar_producto(
            producto_codigo
        )

        if producto is None:

            raise ValueError(
                "No existe el producto seleccionado."
            )

        cantidad = int(cantidad)

        if cantidad <= 0:

            raise ValueError(
                "La cantidad debe ser mayor que cero."
            )

        if not producto.disponible:

            raise ValueError(
                "El producto no está disponible."
            )

        if cantidad > producto.stock:

            raise ValueError(
                "No hay suficiente stock."
            )

        venta = Venta(
            usuario.identificacion,
            producto.codigo,
            cantidad
        )

        producto.vender_producto(
            cantidad
        )

        self.agregar_venta(
            venta
        )

        archivo_servicio.guardar_productos(
            self.productos
        )

        archivo_servicio.guardar_ventas(
            self.ventas
        )

        return venta
    