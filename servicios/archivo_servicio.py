import json
import os


class ArchivoServicio:

    def __init__(
        self,
        ruta_productos,
        ruta_usuarios,
        ruta_ventas
    ):

        self.ruta_productos = ruta_productos
        self.ruta_usuarios = ruta_usuarios
        self.ruta_ventas = ruta_ventas

    def _cargar_archivo(self, ruta):

        if not os.path.exists(ruta):
            return []

        try:

            with open(
                ruta,
                "r",
                encoding="utf-8"
            ) as archivo:

                datos = json.load(archivo)

                if isinstance(datos, list):
                    return datos

                return []

        except (
            json.JSONDecodeError,
            OSError
        ):

            return []

    def _guardar_archivo(
        self,
        ruta,
        datos
    ):

        carpeta = os.path.dirname(ruta)

        if carpeta:
            os.makedirs(
                carpeta,
                exist_ok=True
            )

        with open(
            ruta,
            "w",
            encoding="utf-8"
        ) as archivo:

            json.dump(
                datos,
                archivo,
                indent=4,
                ensure_ascii=False
            )

    # PRODUCTOS

    def cargar_productos(self):

        return self._cargar_archivo(
            self.ruta_productos
        )

    def guardar_productos(
        self,
        productos
    ):

        datos = [
            producto.to_dict()
            for producto in productos
        ]

        self._guardar_archivo(
            self.ruta_productos,
            datos
        )

    # USUARIOS

    def cargar_usuarios(self):

        return self._cargar_archivo(
            self.ruta_usuarios
        )

    def guardar_usuarios(
        self,
        usuarios
    ):

        datos = [
            usuario.to_dict()
            for usuario in usuarios
        ]

        self._guardar_archivo(
            self.ruta_usuarios,
            datos
        )

    # VENTAS

    def cargar_ventas(self):

        return self._cargar_archivo(
            self.ruta_ventas
        )

    def guardar_ventas(
        self,
        ventas
    ):

        datos = [
            venta.to_dict()
            for venta in ventas
        ]

        self._guardar_archivo(
            self.ruta_ventas,
            datos
        )
        