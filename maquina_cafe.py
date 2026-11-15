class Vaso:
    def __init__(self, cantidad_vasos: int, contenido: int):
        self._cantidad_vasos = cantidad_vasos
        self._contenido = contenido  # onzas de café que lleva cada vaso

    def set_cantidad_vasos(self, cantidad_vasos: int):
        self._cantidad_vasos = cantidad_vasos

    def get_cantidad_vasos(self) -> int:
        return self._cantidad_vasos

    def set_contenido(self, contenido: int):
        self._contenido = contenido

    def get_contenido(self) -> int:
        return self._contenido

    def has_vasos(self, cantidad_vasos: int) -> bool:
        return self._cantidad_vasos >= cantidad_vasos

    def give_vasos(self, cantidad_vasos: int):
        self._cantidad_vasos -= cantidad_vasos


class Cafetera:
    def __init__(self, cantidad_cafe: int):
        self._cantidad_cafe = cantidad_cafe

    def set_cantidad_de_cafe(self, cantidad_cafe: int):
        self._cantidad_cafe = cantidad_cafe

    def get_cantidad_cafe(self) -> int:
        return self._cantidad_cafe

    def has_cafe(self, cantidad_cafe: int) -> bool:
        return self._cantidad_cafe >= cantidad_cafe

    def give_cafe(self, cantidad_cafe: int):
        self._cantidad_cafe -= cantidad_cafe


class Azucarero:
    def __init__(self, cantidad_azucar: int):
        self._cantidad_azucar = cantidad_azucar

    def set_cantidad_de_azucar(self, cantidad_azucar: int):
        self._cantidad_azucar = cantidad_azucar

    def get_cantidad_azucar(self) -> int:
        return self._cantidad_azucar

    def has_azucar(self, cantidad_azucar: int) -> bool:
        return self._cantidad_azucar >= cantidad_azucar

    def give_azucar(self, cantidad_azucar: int):
        self._cantidad_azucar -= cantidad_azucar


class MaquinaDeCafe:
    def __init__(self):
        self.cafetera = None
        self.vasos_pequeno = None
        self.vasos_mediano = None
        self.vasos_grande = None
        self.azucarero = None

    # --- setters / getters -------------------------------------------------
    def set_cafetera(self, cafetera: Cafetera):
        self.cafetera = cafetera

    def get_cafetera(self) -> Cafetera:
        return self.cafetera

    def set_vasos_pequeno(self, vasos: Vaso):
        self.vasos_pequeno = vasos

    def get_vasos_pequeno(self) -> Vaso:
        return self.vasos_pequeno

    def set_vasos_mediano(self, vasos: Vaso):
        self.vasos_mediano = vasos

    def get_vasos_mediano(self) -> Vaso:
        return self.vasos_mediano

    def set_vasos_grande(self, vasos: Vaso):
        self.vasos_grande = vasos

    def get_vasos_grande(self) -> Vaso:
        return self.vasos_grande

    def set_azucarero(self, azucarero: Azucarero):
        self.azucarero = azucarero

    def get_azucarero(self) -> Azucarero:
        return self.azucarero

    # --- comportamiento ----------------------------------------------------
    def get_tipo_de_vaso(self, tipo_de_vaso: str) -> Vaso:
        tipos = {
            "pequeno": self.vasos_pequeno,
            "mediano": self.vasos_mediano,
            "grande": self.vasos_grande,
        }
        return tipos.get(tipo_de_vaso.lower())

    def get_vaso_de_cafe(self, vaso: Vaso, cantidad_de_vasos: int,
                         cantidad_de_azucar: int) -> str:
        cafe_necesario = vaso.get_contenido() * cantidad_de_vasos

        # Se valida todo antes de consumir cualquier recurso
        if not vaso.has_vasos(cantidad_de_vasos):
            return "No hay Vasos"
        if not self.cafetera.has_cafe(cafe_necesario):
            return "No hay Cafe"
        if not self.azucarero.has_azucar(cantidad_de_azucar):
            return "No hay Azucar"

        vaso.give_vasos(cantidad_de_vasos)
        self.cafetera.give_cafe(cafe_necesario)
        self.azucarero.give_azucar(cantidad_de_azucar)
        return "Felicitaciones"
