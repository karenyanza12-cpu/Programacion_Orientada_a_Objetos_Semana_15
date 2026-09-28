class Producto:

    def __init__(
        self,
        codigo,
        nombre,
        precio,
        stock,
        disponible=True
    ):

        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.stock = stock
        self.disponible = disponible

    @property
    def codigo(self):
        return self._codigo

    @codigo.setter
    def codigo(self, valor):

        if int(valor) <= 0:
            raise ValueError(
                "El código debe ser mayor que cero."
            )

        self._codigo = int(valor)

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, valor):

        if not valor.strip():
            raise ValueError(
                "El nombre no puede estar vacío."
            )

        self._nombre = valor.strip()

    @property
    def precio(self):
        return self._precio

    @precio.setter
    def precio(self, valor):

        valor = float(valor)

        if valor <= 0:
            raise ValueError(
                "El precio debe ser mayor que cero."
            )

        self._precio = valor

    @property
    def stock(self):
        return self._stock

    @stock.setter
    def stock(self, valor):

        valor = int(valor)

        if valor < 0:
            raise ValueError(
                "El stock no puede ser negativo."
            )

        self._stock = valor

    @property
    def disponible(self):
        return self._disponible

    @disponible.setter
    def disponible(self, valor):

        self._disponible = bool(valor)

    def vender_producto(self, cantidad):

        cantidad = int(cantidad)

        if cantidad <= 0:
            raise ValueError(
                "La cantidad debe ser mayor que cero."
            )

        if cantidad > self.stock:
            raise ValueError(
                "No hay suficiente stock."
            )

        self.stock -= cantidad

        if self.stock == 0:
            self.disponible = False

    def to_dict(self):

        return {
            "codigo": self.codigo,
            "nombre": self.nombre,
            "precio": self.precio,
            "stock": self.stock,
            "disponible": self.disponible
        }

    def __str__(self):

        return (
            f"{self.codigo} - {self.nombre} | "
            f"${self.precio:.2f} | Stock: {self.stock}"
        )
    