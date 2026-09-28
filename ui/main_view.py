import os
import tkinter as tk
from tkinter import ttk, messagebox

from modelos.producto import Producto


class MainView(ttk.Frame):

    def __init__(
        self,
        master,
        restaurante,
        archivo_servicio
    ):

        super().__init__(master)

        self.master = master
        self.restaurante = restaurante
        self.archivo_servicio = archivo_servicio

        self.master.title(
            "AMALIA RESTAURANT - Sistema de gestión"
        )

        self.master.geometry(
            "1050x700"
        )

        self.master.resizable(
            True,
            True
        )

        self.crear_interfaz()

    # --------------------------------------------------
    # VENTANA PRINCIPAL
    # --------------------------------------------------

    def crear_interfaz(self):

        encabezado = ttk.Frame(
            self,
            padding=15
        )

        encabezado.pack(
            fill="x"
        )

        ruta_logo = os.path.join(
            os.path.dirname(
                os.path.dirname(__file__)
            ),
            "assets",
            "logo_amalia.png"
        )

        if os.path.exists(
            ruta_logo
        ):

            self.logo = tk.PhotoImage(
                file=ruta_logo
            )

            self.logo = self.logo.subsample(
                4,
                4
            )

            ttk.Label(
                encabezado,
                image=self.logo
            ).pack(
                side="left",
                padx=(0, 10)
            )

        ttk.Label(
            encabezado,
            text="AMALIA RESTAURANT",
            font=("Arial", 20, "bold")
        ).pack(
            side="left"
        )

        ttk.Label(
            encabezado,
            text="Sistema de gestión"
        ).pack(
            side="right"
        )

        self.notebook = ttk.Notebook(
            self
        )

        self.notebook.pack(
            fill="both",
            expand=True,
            padx=15,
            pady=10
        )

        self.productos_frame = ttk.Frame(
            self.notebook,
            padding=15
        )

        self.usuarios_frame = ttk.Frame(
            self.notebook,
            padding=15
        )

        self.ventas_frame = ttk.Frame(
            self.notebook,
            padding=15
        )

        self.notebook.add(
            self.productos_frame,
            text="Productos"
        )

        self.notebook.add(
            self.usuarios_frame,
            text="Usuarios"
        )

        self.notebook.add(
            self.ventas_frame,
            text="Ventas"
        )

        self.crear_seccion_productos()

        self.crear_seccion_usuarios()

        self.crear_seccion_ventas()

    # --------------------------------------------------
    # PRODUCTOS
    # --------------------------------------------------

    def crear_seccion_productos(self):

        ttk.Label(
            self.productos_frame,
            text="Gestión de Productos",
            font=("Arial", 16, "bold")
        ).pack(
            anchor="w",
            pady=(0, 12)
        )

        formulario = ttk.LabelFrame(
            self.productos_frame,
            text="Información del producto",
            padding=12
        )

        formulario.pack(
            fill="x"
        )

        ttk.Label(
            formulario,
            text="Código:"
        ).grid(
            row=0,
            column=0,
            padx=8,
            pady=8,
            sticky="w"
        )

        self.codigo_entry = ttk.Entry(
            formulario,
            width=20
        )

        self.codigo_entry.grid(
            row=0,
            column=1,
            padx=8,
            pady=8
        )

        ttk.Label(
            formulario,
            text="Nombre:"
        ).grid(
            row=0,
            column=2,
            padx=8,
            pady=8,
            sticky="w"
        )

        self.nombre_entry = ttk.Entry(
            formulario,
            width=30
        )

        self.nombre_entry.grid(
            row=0,
            column=3,
            padx=8,
            pady=8
        )

        ttk.Label(
            formulario,
            text="Precio:"
        ).grid(
            row=1,
            column=0,
            padx=8,
            pady=8,
            sticky="w"
        )

        self.precio_entry = ttk.Entry(
            formulario,
            width=20
        )

        self.precio_entry.grid(
            row=1,
            column=1,
            padx=8,
            pady=8
        )

        ttk.Label(
            formulario,
            text="Stock:"
        ).grid(
            row=1,
            column=2,
            padx=8,
            pady=8,
            sticky="w"
        )

        self.stock_entry = ttk.Entry(
            formulario,
            width=30
        )

        self.stock_entry.grid(
            row=1,
            column=3,
            padx=8,
            pady=8
        )

        self.disponible_var = tk.BooleanVar(
            value=True
        )

        ttk.Checkbutton(
            formulario,
            text="Producto disponible",
            variable=self.disponible_var
        ).grid(
            row=2,
            column=0,
            columnspan=2,
            padx=8,
            pady=8,
            sticky="w"
        )

        botones = ttk.Frame(
            self.productos_frame,
            padding=(0, 10)
        )

        botones.pack(
            fill="x"
        )

        ttk.Button(
            botones,
            text="Registrar",
            command=self.registrar_producto
        ).pack(
            side="left",
            padx=4
        )

        ttk.Button(
            botones,
            text="Consultar",
            command=self.consultar_producto
        ).pack(
            side="left",
            padx=4
        )

        ttk.Button(
            botones,
            text="Actualizar",
            command=self.actualizar_producto
        ).pack(
            side="left",
            padx=4
        )

        ttk.Button(
            botones,
            text="Eliminar",
            command=self.eliminar_producto
        ).pack(
            side="left",
            padx=4
        )

        ttk.Button(
            botones,
            text="Cargar todos",
            command=self.cargar_productos
        ).pack(
            side="left",
            padx=4
        )

        ttk.Button(
            botones,
            text="Limpiar",
            command=self.limpiar_formulario
        ).pack(
            side="left",
            padx=4
        )

        tabla_frame = ttk.LabelFrame(
            self.productos_frame,
            text="Productos registrados",
            padding=10
        )

        tabla_frame.pack(
            fill="both",
            expand=True
        )

        columnas = (
            "codigo",
            "nombre",
            "precio",
            "stock",
            "disponible"
        )

        self.productos_tree = ttk.Treeview(
            tabla_frame,
            columns=columnas,
            show="headings",
            height=12
        )

        self.productos_tree.heading(
            "codigo",
            text="Código"
        )

        self.productos_tree.heading(
            "nombre",
            text="Nombre"
        )

        self.productos_tree.heading(
            "precio",
            text="Precio"
        )

        self.productos_tree.heading(
            "stock",
            text="Stock"
        )

        self.productos_tree.heading(
            "disponible",
            text="Disponible"
        )

        self.productos_tree.column(
            "codigo",
            width=80,
            anchor="center"
        )

        self.productos_tree.column(
            "nombre",
            width=250
        )

        self.productos_tree.column(
            "precio",
            width=100,
            anchor="center"
        )

        self.productos_tree.column(
            "stock",
            width=100,
            anchor="center"
        )

        self.productos_tree.column(
            "disponible",
            width=120,
            anchor="center"
        )

        self.productos_tree.pack(
            fill="both",
            expand=True
        )

        self.cargar_productos()

    # --------------------------------------------------
    # DATOS PRODUCTO
    # --------------------------------------------------

    def obtener_datos_producto(self):

        codigo = int(
            self.codigo_entry.get().strip()
        )

        nombre = (
            self.nombre_entry.get().strip()
        )

        precio = float(
            self.precio_entry.get().strip()
        )

        stock = int(
            self.stock_entry.get().strip()
        )

        disponible = (
            self.disponible_var.get()
        )

        return (
            codigo,
            nombre,
            precio,
            stock,
            disponible
        )

    # --------------------------------------------------
    # REGISTRAR PRODUCTO
    # --------------------------------------------------

    def registrar_producto(self):

        try:

            (
                codigo,
                nombre,
                precio,
                stock,
                disponible
            ) = self.obtener_datos_producto()

            producto = Producto(
                codigo,
                nombre,
                precio,
                stock,
                disponible
            )

            self.restaurante.agregar_producto(
                producto
            )

            self.archivo_servicio.guardar_productos(
                self.restaurante.productos
            )

            self.cargar_productos()

            self.limpiar_formulario()

            messagebox.showinfo(
                "Registro",
                "Producto registrado correctamente."
            )

        except ValueError as error:

            messagebox.showerror(
                "Error",
                str(error)
            )

        except Exception as error:

            messagebox.showerror(
                "Error",
                f"No se pudo registrar el producto:\n{error}"
            )

    # --------------------------------------------------
    # CONSULTAR PRODUCTO
    # --------------------------------------------------

    def consultar_producto(self):

        try:

            codigo = int(
                self.codigo_entry.get().strip()
            )

            producto = self.restaurante.buscar_producto(
                codigo
            )

            if producto is None:

                messagebox.showwarning(
                    "Consulta",
                    "No se encontró un producto con ese código."
                )

                return

            self.nombre_entry.delete(
                0,
                tk.END
            )

            self.nombre_entry.insert(
                0,
                producto.nombre
            )

            self.precio_entry.delete(
                0,
                tk.END
            )

            self.precio_entry.insert(
                0,
                str(producto.precio)
            )

            self.stock_entry.delete(
                0,
                tk.END
            )

            self.stock_entry.insert(
                0,
                str(producto.stock)
            )

            self.disponible_var.set(
                producto.disponible
            )

        except ValueError:

            messagebox.showerror(
                "Error",
                "Ingrese un código numérico válido."
            )

    # --------------------------------------------------
    # ACTUALIZAR PRODUCTO
    # --------------------------------------------------

    def actualizar_producto(self):

        try:

            (
                codigo,
                nombre,
                precio,
                stock,
                disponible
            ) = self.obtener_datos_producto()

            producto = self.restaurante.buscar_producto(
                codigo
            )

            if producto is None:

                messagebox.showwarning(
                    "Actualizar",
                    "No existe un producto con ese código."
                )

                return

            self.restaurante.actualizar_producto(
                codigo,
                nombre,
                precio,
                stock,
                disponible
            )

            self.archivo_servicio.guardar_productos(
                self.restaurante.productos
            )

            self.cargar_productos()

            messagebox.showinfo(
                "Actualizar",
                "Producto actualizado correctamente."
            )

        except ValueError as error:

            messagebox.showerror(
                "Error",
                str(error)
            )

    # --------------------------------------------------
    # ELIMINAR PRODUCTO
    # --------------------------------------------------

    def eliminar_producto(self):

        try:

            codigo = int(
                self.codigo_entry.get().strip()
            )

            producto = self.restaurante.buscar_producto(
                codigo
            )

            if producto is None:

                messagebox.showwarning(
                    "Eliminar",
                    "No existe un producto con ese código."
                )

                return

            confirmar = messagebox.askyesno(
                "Confirmar",
                f"¿Desea eliminar el producto {producto.nombre}?"
            )

            if not confirmar:
                return

            self.restaurante.eliminar_producto(
                codigo
            )

            self.archivo_servicio.guardar_productos(
                self.restaurante.productos
            )

            self.cargar_productos()

            self.limpiar_formulario()

            messagebox.showinfo(
                "Eliminar",
                "Producto eliminado correctamente."
            )

        except ValueError as error:

            messagebox.showerror(
                "Error",
                str(error)
            )

    # --------------------------------------------------
    # CARGAR PRODUCTOS
    # --------------------------------------------------

    def cargar_productos(self):

        for item in self.productos_tree.get_children():

            self.productos_tree.delete(
                item
            )

        productos = (
            self.restaurante.listar_productos()
        )

        for producto in productos:

            disponible = (
                "Sí"
                if producto.disponible
                else "No"
            )

            self.productos_tree.insert(
                "",
                tk.END,
                values=(
                    producto.codigo,
                    producto.nombre,
                    f"{producto.precio:.2f}",
                    producto.stock,
                    disponible
                )
            )

    # --------------------------------------------------
    # LIMPIAR PRODUCTO
    # --------------------------------------------------

    def limpiar_formulario(self):

        self.codigo_entry.delete(
            0,
            tk.END
        )

        self.nombre_entry.delete(
            0,
            tk.END
        )

        self.precio_entry.delete(
            0,
            tk.END
        )

        self.stock_entry.delete(
            0,
            tk.END
        )

        self.disponible_var.set(
            True
        )

    # --------------------------------------------------
    # USUARIOS
    # --------------------------------------------------

    def crear_seccion_usuarios(self):

        ttk.Label(
            self.usuarios_frame,
            text="Consulta de Usuarios",
            font=("Arial", 16, "bold")
        ).pack(
            anchor="w",
            pady=(0, 12)
        )

        ttk.Label(
            self.usuarios_frame,
            text="Usuarios registrados en el sistema"
        ).pack(
            anchor="w",
            pady=(0, 10)
        )

        tabla_frame = ttk.LabelFrame(
            self.usuarios_frame,
            text="Información de usuarios",
            padding=10
        )

        tabla_frame.pack(
            fill="both",
            expand=True
        )

        columnas = (
            "identificacion",
            "nombre",
            "correo"
        )

        self.usuarios_tree = ttk.Treeview(
            tabla_frame,
            columns=columnas,
            show="headings"
        )

        self.usuarios_tree.heading(
            "identificacion",
            text="Identificación"
        )

        self.usuarios_tree.heading(
            "nombre",
            text="Nombre"
        )

        self.usuarios_tree.heading(
            "correo",
            text="Correo"
        )

        self.usuarios_tree.column(
            "identificacion",
            width=150,
            anchor="center"
        )

        self.usuarios_tree.column(
            "nombre",
            width=300
        )

        self.usuarios_tree.column(
            "correo",
            width=350
        )

        self.usuarios_tree.pack(
            fill="both",
            expand=True
        )

        ttk.Button(
            self.usuarios_frame,
            text="Consultar usuarios",
            command=self.cargar_usuarios
        ).pack(
            pady=10
        )

        self.cargar_usuarios()

    # --------------------------------------------------
    # CARGAR USUARIOS
    # --------------------------------------------------

    def cargar_usuarios(self):

        for item in self.usuarios_tree.get_children():

            self.usuarios_tree.delete(
                item
            )

        usuarios = (
            self.restaurante.listar_usuarios()
        )

        for usuario in usuarios:

            self.usuarios_tree.insert(
                "",
                tk.END,
                values=(
                    usuario.identificacion,
                    usuario.nombre,
                    usuario.correo
                )
            )

    # --------------------------------------------------
    # VENTAS
    # --------------------------------------------------

    def crear_seccion_ventas(self):

        ttk.Label(
            self.ventas_frame,
            text="Gestión de Ventas",
            font=("Arial", 16, "bold")
        ).pack(
            anchor="w",
            pady=(0, 12)
        )

        formulario = ttk.LabelFrame(
            self.ventas_frame,
            text="Registrar venta",
            padding=15
        )

        formulario.pack(
            fill="x"
        )

        ttk.Label(
            formulario,
            text="Usuario:"
        ).grid(
            row=0,
            column=0,
            padx=8,
            pady=8,
            sticky="w"
        )

        self.usuario_venta_combo = ttk.Combobox(
            formulario,
            width=35,
            state="readonly"
        )

        self.usuario_venta_combo.grid(
            row=0,
            column=1,
            padx=8,
            pady=8
        )

        ttk.Label(
            formulario,
            text="Producto:"
        ).grid(
            row=1,
            column=0,
            padx=8,
            pady=8,
            sticky="w"
        )

        self.producto_venta_combo = ttk.Combobox(
            formulario,
            width=35,
            state="readonly"
        )

        self.producto_venta_combo.grid(
            row=1,
            column=1,
            padx=8,
            pady=8
        )

        ttk.Label(
            formulario,
            text="Cantidad:"
        ).grid(
            row=2,
            column=0,
            padx=8,
            pady=8,
            sticky="w"
        )

        self.cantidad_venta_spinbox = ttk.Spinbox(
            formulario,
            from_=1,
            to=100,
            width=10
        )

        self.cantidad_venta_spinbox.set(
            1
        )

        self.cantidad_venta_spinbox.grid(
            row=2,
            column=1,
            padx=8,
            pady=8,
            sticky="w"
        )

        self.cargar_opciones_venta()

        botones = ttk.Frame(
            self.ventas_frame,
            padding=(0, 10)
        )

        botones.pack(
            fill="x"
        )

        ruta_icono = os.path.join(
            os.path.dirname(
                os.path.dirname(__file__)
            ),
            "assets",
            "icono_amalia.png"
        )

        if os.path.exists(
            ruta_icono
        ):

            self.icono = tk.PhotoImage(
                file=ruta_icono
            )

            self.icono = self.icono.subsample(
                4,
                4
            )

            ttk.Button(
                botones,
                text="Registrar venta",
                image=self.icono,
                compound="left",
                command=self.registrar_venta
            ).pack(
                side="left",
                padx=4
            )

        else:

            ttk.Button(
                botones,
                text="Registrar venta",
                command=self.registrar_venta
            ).pack(
                side="left",
                padx=4
            )

        ttk.Button(
            botones,
            text="Cargar ventas",
            command=self.cargar_ventas
        ).pack(
            side="left",
            padx=4
        )

        ttk.Button(
            botones,
            text="Limpiar",
            command=self.limpiar_venta
        ).pack(
            side="left",
            padx=4
        )

        tabla_frame = ttk.LabelFrame(
            self.ventas_frame,
            text="Ventas registradas",
            padding=10
        )

        tabla_frame.pack(
            fill="both",
            expand=True
        )

        columnas = (
            "usuario",
            "producto",
            "cantidad",
            "fecha"
        )

        self.ventas_tree = ttk.Treeview(
            tabla_frame,
            columns=columnas,
            show="headings"
        )

        self.ventas_tree.heading(
            "usuario",
            text="Usuario"
        )

        self.ventas_tree.heading(
            "producto",
            text="Producto"
        )

        self.ventas_tree.heading(
            "cantidad",
            text="Cantidad"
        )

        self.ventas_tree.heading(
            "fecha",
            text="Fecha"
        )

        self.ventas_tree.column(
            "usuario",
            width=250
        )

        self.ventas_tree.column(
            "producto",
            width=250
        )

        self.ventas_tree.column(
            "cantidad",
            width=100,
            anchor="center"
        )

        self.ventas_tree.column(
            "fecha",
            width=180,
            anchor="center"
        )

        self.ventas_tree.pack(
            fill="both",
            expand=True
        )

        self.cargar_ventas()

    # --------------------------------------------------
    # OPCIONES DE VENTA
    # --------------------------------------------------

    def cargar_opciones_venta(self):

        usuarios = (
            self.restaurante.listar_usuarios()
        )

        opciones_usuarios = []

        for usuario in usuarios:

            texto = (
                f"{usuario.identificacion} - "
                f"{usuario.nombre}"
            )

            opciones_usuarios.append(
                texto
            )

        self.usuario_venta_combo["values"] = (
            opciones_usuarios
        )

        productos = (
            self.restaurante.listar_productos()
        )

        opciones_productos = []

        for producto in productos:

            if producto.disponible:

                texto = (
                    f"{producto.codigo} - "
                    f"{producto.nombre}"
                )

                opciones_productos.append(
                    texto
                )

        self.producto_venta_combo["values"] = (
            opciones_productos
        )

    # --------------------------------------------------
    # REGISTRAR VENTA
    # --------------------------------------------------

    def registrar_venta(self):

        try:

            usuario_seleccionado = (
                self.usuario_venta_combo.get()
            )

            producto_seleccionado = (
                self.producto_venta_combo.get()
            )

            if not usuario_seleccionado:

                messagebox.showwarning(
                    "Venta",
                    "Debe seleccionar un usuario."
                )

                return

            if not producto_seleccionado:

                messagebox.showwarning(
                    "Venta",
                    "Debe seleccionar un producto."
                )

                return

            usuario_id = (
                usuario_seleccionado.split(
                    " - ",
                    1
                )[0]
            )

            producto_codigo = int(
                producto_seleccionado.split(
                    " - ",
                    1
                )[0]
            )

            cantidad = int(
                self.cantidad_venta_spinbox.get()
            )

            venta = self.restaurante.registrar_venta(
                usuario_id,
                producto_codigo,
                cantidad,
                self.archivo_servicio
            )

            self.cargar_productos()

            self.cargar_opciones_venta()

            self.cargar_ventas()

            self.limpiar_venta()

            messagebox.showinfo(
                "Venta",
                "Venta registrada correctamente.\n\n"
                f"Fecha: {venta.fecha}"
            )

        except ValueError as error:

            messagebox.showerror(
                "Error",
                str(error)
            )

        except Exception as error:

            messagebox.showerror(
                "Error",
                f"No se pudo registrar la venta:\n{error}"
            )

    # --------------------------------------------------
    # MOSTRAR VENTAS
    # --------------------------------------------------

    def cargar_ventas(self):

        if not hasattr(
            self,
            "ventas_tree"
        ):
            return

        for item in self.ventas_tree.get_children():

            self.ventas_tree.delete(
                item
            )

        ventas = (
            self.restaurante.listar_ventas()
        )

        for venta in ventas:

            usuario = (
                self.restaurante.buscar_usuario(
                    venta.usuario_id
                )
            )

            producto = (
                self.restaurante.buscar_producto(
                    venta.producto_codigo
                )
            )

            nombre_usuario = (
                usuario.nombre
                if usuario is not None
                else venta.usuario_id
            )

            nombre_producto = (
                producto.nombre
                if producto is not None
                else str(venta.producto_codigo)
            )

            self.ventas_tree.insert(
                "",
                tk.END,
                values=(
                    nombre_usuario,
                    nombre_producto,
                    venta.cantidad,
                    venta.fecha
                )
            )

    # --------------------------------------------------
    # LIMPIAR VENTA
    # --------------------------------------------------

    def limpiar_venta(self):

        self.usuario_venta_combo.set(
            ""
        )

        self.producto_venta_combo.set(
            ""
        )

        self.cantidad_venta_spinbox.set(
            1
        )
        