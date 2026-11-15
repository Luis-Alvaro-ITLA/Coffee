from maquina_cafe import Vaso, Cafetera, Azucarero, MaquinaDeCafe

TAMANOS = {
    "1": ("pequeno", "Pequeño", 3),
    "2": ("mediano", "Mediano", 5),
    "3": ("grande", "Grande", 7),
}

MENSAJES_ERROR = {
    "No hay Vasos": "Lo sentimos, no hay vasos de ese tamaño disponibles.",
    "No hay Cafe": "Lo sentimos, no hay café suficiente.",
    "No hay Azucar": "Lo sentimos, no hay azúcar suficiente.",
}

MENSAJE_EXITO = "¡Listo! Su café está servido. Por favor, recoja su vaso."


def crear_maquina(vasos_por_tamano=10, cafe=100, azucar=30):
    maquina = MaquinaDeCafe()
    maquina.set_cafetera(Cafetera(cafe))
    maquina.set_vasos_pequeno(Vaso(vasos_por_tamano, TAMANOS["1"][2]))
    maquina.set_vasos_mediano(Vaso(vasos_por_tamano, TAMANOS["2"][2]))
    maquina.set_vasos_grande(Vaso(vasos_por_tamano, TAMANOS["3"][2]))
    maquina.set_azucarero(Azucarero(azucar))

    # Capacidad máxima, usada por la opción de mantenimiento
    maquina.capacidad = {"vasos": vasos_por_tamano, "cafe": cafe, "azucar": azucar}
    return maquina


class InterfazConsola:
    def __init__(self, maquina, entrada=input, salida=print):
        self.maquina = maquina
        self.entrada = entrada
        self.salida = salida

    def ejecutar(self):
        self.salida("=== MÁQUINA DE CAFÉ ===")
        while True:
            self._mostrar_menu()
            opcion = self.entrada("Seleccione una opción: ").strip()
            if opcion in TAMANOS:
                self._servir_cafe(opcion)
            elif opcion == "4":
                self.salida("¡Hasta luego!")
                return
            elif opcion == "5":
                self._rellenar()
            else:
                self.salida("Opción no válida, intente de nuevo.")

    def _mostrar_menu(self):
        self.salida("\n1) Seleccione el tamaño de su vaso:")
        for clave, (_, nombre, onzas) in TAMANOS.items():
            self.salida(f"   {clave}. {nombre} ({onzas} Oz)")
        self.salida("   4. Salir")
        self.salida("   5. Mantenimiento (rellenar insumos)")

    def _pedir_azucar(self):
        while True:
            texto = self.entrada("2) Cucharadas de azúcar (0 si no desea): ").strip()
            if texto.isdigit():
                return int(texto)
            self.salida("Ingrese un número entero igual o mayor que 0.")

    def _servir_cafe(self, opcion):
        clave, nombre, _ = TAMANOS[opcion]
        cucharadas = self._pedir_azucar()
        vaso = self.maquina.get_tipo_de_vaso(clave)
        resultado = self.maquina.get_vaso_de_cafe(vaso, 1, cucharadas)
        if resultado == "Felicitaciones":
            self.salida(f"Preparando café {nombre.lower()} con {cucharadas} cucharada(s) de azúcar...")
            self.salida(f"3) {MENSAJE_EXITO}")
        else:
            self.salida(MENSAJES_ERROR[resultado])

    def _rellenar(self):
        cap = self.maquina.capacidad
        self.maquina.get_cafetera().set_cantidad_de_cafe(cap["cafe"])
        self.maquina.get_azucarero().set_cantidad_de_azucar(cap["azucar"])
        for vasos in (self.maquina.get_vasos_pequeno(),
                      self.maquina.get_vasos_mediano(),
                      self.maquina.get_vasos_grande()):
            vasos.set_cantidad_vasos(cap["vasos"])
        self.salida("Insumos rellenados correctamente.")
