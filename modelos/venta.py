from datetime import datetime


class Venta:

    def __init__(
        self,
        usuario_id,
        producto_codigo,
        cantidad,
        fecha=None
    ):

        self.usuario_id = str(usuario_id)
        self.producto_codigo = int(producto_codigo)
        self.cantidad = int(cantidad)

        if not self.usuario_id.strip():
            raise ValueError(
                "Debe seleccionar un usuario."
            )

        if self.producto_codigo <= 0:
            raise ValueError(
                "El código del producto no es válido."
            )

        if self.cantidad <= 0:
            raise ValueError(
                "La cantidad debe ser mayor que cero."
            )

        if fecha is None or not str(fecha).strip():

            self.fecha = datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S"
            )

        else:

            self.fecha = str(fecha)

    def to_dict(self):

        return {
            "usuario_id": self.usuario_id,
            "producto_codigo": self.producto_codigo,
            "cantidad": self.cantidad,
            "fecha": self.fecha
        }

    def __str__(self):

        return (
            f"Usuario: {self.usuario_id} | "
            f"Producto: {self.producto_codigo} | "
            f"Cantidad: {self.cantidad} | "
            f"Fecha: {self.fecha}"
        )
    