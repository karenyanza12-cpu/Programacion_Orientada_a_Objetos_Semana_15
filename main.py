import os
import tkinter as tk

from modelos.producto import Producto
from modelos.usuario import Usuario
from modelos.venta import Venta

from servicios.archivo_servicio import ArchivoServicio
from servicios.restaurante_servicio import RestauranteServicio

from ui.login_view import LoginView


def cargar_datos(
    restaurante,
    archivo_servicio
):

    # Cargar productos

    datos_productos = (
        archivo_servicio.cargar_productos()
    )

    for datos in datos_productos:

        try:

            producto = Producto(
                datos["codigo"],
                datos["nombre"],
                datos["precio"],
                datos["stock"],
                datos["disponible"]
            )

            restaurante.agregar_producto(
                producto
            )

        except (
            ValueError,
            KeyError,
            TypeError
        ):

            print(
                "Se encontró un producto con datos incorrectos."
            )

    # Cargar usuarios

    datos_usuarios = (
        archivo_servicio.cargar_usuarios()
    )

    for datos in datos_usuarios:

        try:

            usuario = Usuario(
                datos["identificacion"],
                datos["nombre"],
                datos["correo"]
            )

            restaurante.agregar_usuario(
                usuario
            )

        except (
            ValueError,
            KeyError,
            TypeError
        ):

            print(
                "Se encontró un usuario con datos incorrectos."
            )

    # Cargar ventas

    datos_ventas = (
        archivo_servicio.cargar_ventas()
    )

    for datos in datos_ventas:

        try:

            venta = Venta(
                datos["usuario_id"],
                datos["producto_codigo"],
                datos["cantidad"],
                datos.get("fecha")
            )

            restaurante.agregar_venta(
                venta
            )

        except (
            ValueError,
            KeyError,
            TypeError
        ):

            print(
                "Se encontró una venta con datos incorrectos."
            )

    restaurante.reconstruir_indices()


def main():

    # Ubicación del proyecto

    base_dir = os.path.dirname(
        os.path.abspath(__file__)
    )

    datos_dir = os.path.join(
        base_dir,
        "datos"
    )

    os.makedirs(
        datos_dir,
        exist_ok=True
    )

    ruta_productos = os.path.join(
        datos_dir,
        "productos.json"
    )

    ruta_usuarios = os.path.join(
        datos_dir,
        "usuarios.json"
    )

    ruta_ventas = os.path.join(
        datos_dir,
        "ventas.json"
    )

    # Servicio de archivos

    archivo_servicio = ArchivoServicio(
        ruta_productos,
        ruta_usuarios,
        ruta_ventas
    )

    # Servicio principal

    restaurante = RestauranteServicio()

    # Cargar información

    cargar_datos(
        restaurante,
        archivo_servicio
    )

    # Crear ventana

    root = tk.Tk()

    login = LoginView(
        root,
        restaurante,
        archivo_servicio
    )

    login.pack(
        fill="both",
        expand=True
    )

    root.mainloop()


if __name__ == "__main__":

    main()
    