class Usuario:

    def __init__(
        self,
        identificacion,
        nombre,
        correo
    ):

        self.identificacion = identificacion
        self.nombre = nombre
        self.correo = correo

    @property
    def identificacion(self):
        return self._identificacion

    @identificacion.setter
    def identificacion(self, valor):

        if not str(valor).strip():
            raise ValueError(
                "La identificación es obligatoria."
            )

        self._identificacion = str(valor).strip()

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, valor):

        if not valor.strip():
            raise ValueError(
                "El nombre es obligatorio."
            )

        self._nombre = valor.strip()

    @property
    def correo(self):
        return self._correo

    @correo.setter
    def correo(self, valor):

        if not valor.strip():
            raise ValueError(
                "El correo es obligatorio."
            )

        self._correo = valor.strip()

    def mostrar_informacion(self):

        return (
            f"Identificación: {self.identificacion}\n"
            f"Nombre: {self.nombre}\n"
            f"Correo: {self.correo}"
        )

    def to_dict(self):

        return {
            "identificacion": self.identificacion,
            "nombre": self.nombre,
            "correo": self.correo
        }

    def __str__(self):

        return (
            f"{self.nombre} - "
            f"{self.identificacion}"
        )
    