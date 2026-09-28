import os
import tkinter as tk
from tkinter import ttk, messagebox


class LoginView(ttk.Frame):

    def __init__(self, master, restaurante, archivo_servicio):
        super().__init__(master)

        self.master = master
        self.restaurante = restaurante
        self.archivo_servicio = archivo_servicio

        self.crear_interfaz()

    def crear_interfaz(self):

        self.master.title("AMALIA RESTAURANT - Inicio de sesión")
        self.master.geometry("450x500")
        self.master.resizable(False, False)

        contenedor = ttk.Frame(
            self,
            padding=30
        )

        contenedor.pack(
            fill="both",
            expand=True
        )

        # -----------------------------------------
        # LOGO DE AMALIA
        # -----------------------------------------

        base_dir = os.path.dirname(
            os.path.dirname(
                os.path.abspath(__file__)
            )
        )

        ruta_logo = os.path.join(
            base_dir,
            "assets",
            "logo_amalia.png"
        )

        try:
            self.logo = tk.PhotoImage(
                file=ruta_logo
            )

            etiqueta_logo = ttk.Label(
                contenedor,
                image=self.logo
            )

            etiqueta_logo.pack(
                pady=(5, 10)
            )

        except Exception as error:
            print("No se pudo cargar el logo:", error)

        # -----------------------------------------
        # TITULO
        # -----------------------------------------

        titulo = ttk.Label(
            contenedor,
            text="AMALIA RESTAURANT",
            font=("Arial", 20, "bold")
        )

        titulo.pack(
            pady=(5, 10)
        )

        # -----------------------------------------
        # SUBTITULO
        # -----------------------------------------

        subtitulo = ttk.Label(
            contenedor,
            text="Sistema de gestión",
            font=("Arial", 11)
        )

        subtitulo.pack(
            pady=(0, 20)
        )

        # -----------------------------------------
        # FORMULARIO
        # -----------------------------------------

        formulario = ttk.Frame(
            contenedor
        )

        formulario.pack()

        ttk.Label(
            formulario,
            text="Usuario:"
        ).grid(
            row=0,
            column=0,
            padx=8,
            pady=10,
            sticky="w"
        )

        self.usuario_entry = ttk.Entry(
            formulario,
            width=25
        )

        self.usuario_entry.grid(
            row=0,
            column=1,
            padx=8,
            pady=10
        )

        ttk.Label(
            formulario,
            text="Contraseña:"
        ).grid(
            row=1,
            column=0,
            padx=8,
            pady=10,
            sticky="w"
        )

        self.contrasena_entry = ttk.Entry(
            formulario,
            width=25,
            show="*"
        )

        self.contrasena_entry.grid(
            row=1,
            column=1,
            padx=8,
            pady=10
        )

        # -----------------------------------------
        # BOTON INGRESAR
        # -----------------------------------------

        boton_ingresar = ttk.Button(
            contenedor,
            text="Ingresar",
            command=self.iniciar_sesion
        )

        boton_ingresar.pack(
            pady=20
        )

        # -----------------------------------------
        # DATOS DE ACCESO
        # -----------------------------------------

        ttk.Label(
            contenedor,
            text="Usuario: admin | Contraseña: 1234"
        ).pack()

    # ---------------------------------------------
    # INICIAR SESION
    # ---------------------------------------------

    def iniciar_sesion(self):

        usuario = self.usuario_entry.get().strip()
        contrasena = self.contrasena_entry.get().strip()

        if usuario == "admin" and contrasena == "1234":

            self.destroy()

            from ui.main_view import MainView

            ventana_principal = MainView(
                self.master,
                self.restaurante,
                self.archivo_servicio
            )

            ventana_principal.pack(
                fill="both",
                expand=True
            )

        else:

            messagebox.showerror(
                "Error",
                "Usuario o contraseña incorrectos."
            )
            