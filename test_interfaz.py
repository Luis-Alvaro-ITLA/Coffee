import unittest

from interfaz import InterfazConsola, crear_maquina


def ejecutar(maquina, respuestas):
    """Corre la interfaz con respuestas simuladas y devuelve todo lo que mostró."""
    entradas = iter(respuestas)
    salida = []
    InterfazConsola(maquina, entrada=lambda _="": next(entradas),
                    salida=salida.append).ejecutar()
    return "\n".join(salida)


class TestInterfazConsola(unittest.TestCase):
    def setUp(self):
        self.maquina = crear_maquina(vasos_por_tamano=10, cafe=100, azucar=30)

    def test_el_menu_muestra_los_tres_tamanos_con_sus_onzas(self):
        texto = ejecutar(self.maquina, ["4"])
        self.assertIn("Pequeño", texto)
        self.assertIn("3 Oz", texto)
        self.assertIn("Mediano", texto)
        self.assertIn("5 Oz", texto)
        self.assertIn("Grande", texto)
        self.assertIn("7 Oz", texto)

    def test_sirve_un_cafe_pequeno_con_azucar(self):
        texto = ejecutar(self.maquina, ["1", "2", "4"])
        self.assertIn("recoja su vaso", texto)
        self.assertEqual(97, self.maquina.get_cafetera().get_cantidad_cafe())
        self.assertEqual(28, self.maquina.get_azucarero().get_cantidad_azucar())
        self.assertEqual(9, self.maquina.get_vasos_pequeno().get_cantidad_vasos())

    def test_sirve_un_cafe_grande_sin_azucar(self):
        ejecutar(self.maquina, ["3", "0", "4"])
        self.assertEqual(93, self.maquina.get_cafetera().get_cantidad_cafe())
        self.assertEqual(30, self.maquina.get_azucarero().get_cantidad_azucar())

    def test_opcion_invalida_vuelve_a_mostrar_el_menu(self):
        texto = ejecutar(self.maquina, ["9", "4"])
        self.assertIn("Opción no válida", texto)

    def test_azucar_invalida_se_vuelve_a_pedir(self):
        ejecutar(self.maquina, ["1", "abc", "-1", "1", "4"])
        self.assertEqual(29, self.maquina.get_azucarero().get_cantidad_azucar())

    def test_mensaje_si_no_hay_vasos(self):
        self.maquina.get_vasos_pequeno().set_cantidad_vasos(0)
        texto = ejecutar(self.maquina, ["1", "1", "4"])
        self.assertIn("no hay vasos", texto)

    def test_mensaje_si_no_hay_cafe(self):
        self.maquina.get_cafetera().set_cantidad_de_cafe(2)
        texto = ejecutar(self.maquina, ["1", "1", "4"])
        self.assertIn("no hay café", texto)

    def test_mensaje_si_no_hay_azucar(self):
        self.maquina.get_azucarero().set_cantidad_de_azucar(1)
        texto = ejecutar(self.maquina, ["1", "3", "4"])
        self.assertIn("no hay azúcar", texto)

    def test_si_falla_no_se_consume_nada(self):
        self.maquina.get_azucarero().set_cantidad_de_azucar(1)
        ejecutar(self.maquina, ["1", "3", "4"])
        self.assertEqual(100, self.maquina.get_cafetera().get_cantidad_cafe())
        self.assertEqual(10, self.maquina.get_vasos_pequeno().get_cantidad_vasos())

    def test_mantenimiento_rellena_los_insumos(self):
        self.maquina.get_cafetera().set_cantidad_de_cafe(0)
        self.maquina.get_azucarero().set_cantidad_de_azucar(0)
        self.maquina.get_vasos_grande().set_cantidad_vasos(0)
        texto = ejecutar(self.maquina, ["5", "4"])
        self.assertIn("rellenad", texto)
        self.assertEqual(100, self.maquina.get_cafetera().get_cantidad_cafe())
        self.assertEqual(30, self.maquina.get_azucarero().get_cantidad_azucar())
        self.assertEqual(10, self.maquina.get_vasos_grande().get_cantidad_vasos())


if __name__ == "__main__":
    unittest.main()
