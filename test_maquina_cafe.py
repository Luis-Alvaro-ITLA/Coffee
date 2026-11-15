import unittest

from maquina_cafe import Vaso, Cafetera, Azucarero, MaquinaDeCafe


class TestVaso(unittest.TestCase):
    def test_deberia_devolver_verdadero_si_existen_vasos(self):
        vasos_pequenos = Vaso(2, 10)
        self.assertTrue(vasos_pequenos.has_vasos(1))

    def test_deberia_devolver_falso_si_no_existen_vasos(self):
        vasos_pequenos = Vaso(1, 10)
        self.assertFalse(vasos_pequenos.has_vasos(2))

    def test_deberia_restar_cantidad_de_vaso(self):
        vasos_pequenos = Vaso(5, 10)
        vasos_pequenos.give_vasos(1)
        self.assertEqual(4, vasos_pequenos.get_cantidad_vasos())


class TestCafetera(unittest.TestCase):
    def test_deberia_devolver_verdadero_si_existe_cafe(self):
        cafetera = Cafetera(10)
        self.assertTrue(cafetera.has_cafe(5))

    def test_deberia_devolver_falso_si_no_existe_cafe(self):
        cafetera = Cafetera(10)
        self.assertFalse(cafetera.has_cafe(11))

    def test_deberia_restar_cafe_a_la_cafetera(self):
        cafetera = Cafetera(10)
        cafetera.give_cafe(7)
        self.assertEqual(3, cafetera.get_cantidad_cafe())


class TestAzucarero(unittest.TestCase):
    def setUp(self):
        self.azucarero = Azucarero(10)

    def test_deberia_devolver_verdadero_si_hay_suficiente_azucar(self):
        self.assertTrue(self.azucarero.has_azucar(5))
        self.assertTrue(self.azucarero.has_azucar(10))

    def test_deberia_devolver_falso_porque_no_hay_suficiente_azucar(self):
        self.assertFalse(self.azucarero.has_azucar(15))

    def test_deberia_restar_azucar_al_azucarero(self):
        self.azucarero.give_azucar(5)
        self.assertEqual(5, self.azucarero.get_cantidad_azucar())
        self.azucarero.give_azucar(2)
        self.assertEqual(3, self.azucarero.get_cantidad_azucar())


class TestMaquinaDeCafe(unittest.TestCase):
    def setUp(self):
        self.cafetera = Cafetera(50)
        self.vasos_pequeno = Vaso(5, 10)
        self.vasos_mediano = Vaso(5, 20)
        self.vasos_grande = Vaso(5, 30)
        self.azucarero = Azucarero(20)

        self.maquina = MaquinaDeCafe()
        self.maquina.set_cafetera(self.cafetera)
        self.maquina.set_vasos_pequeno(self.vasos_pequeno)
        self.maquina.set_vasos_mediano(self.vasos_mediano)
        self.maquina.set_vasos_grande(self.vasos_grande)
        self.maquina.set_azucarero(self.azucarero)

    def test_deberia_devolver_un_vaso_pequeno(self):
        vaso = self.maquina.get_tipo_de_vaso("pequeno")
        self.assertIs(self.maquina.vasos_pequeno, vaso)

    def test_deberia_devolver_un_vaso_mediano(self):
        vaso = self.maquina.get_tipo_de_vaso("mediano")
        self.assertIs(self.maquina.vasos_mediano, vaso)

    def test_deberia_devolver_un_vaso_grande(self):
        vaso = self.maquina.get_tipo_de_vaso("grande")
        self.assertIs(self.maquina.vasos_grande, vaso)

    def test_deberia_devolver_no_hay_vasos(self):
        vaso = self.maquina.get_tipo_de_vaso("pequeno")
        resultado = self.maquina.get_vaso_de_cafe(vaso, 10, 2)
        self.assertEqual("No hay Vasos", resultado)

    def test_deberia_devolver_no_hay_cafe(self):
        self.maquina.set_cafetera(Cafetera(5))
        vaso = self.maquina.get_tipo_de_vaso("pequeno")
        resultado = self.maquina.get_vaso_de_cafe(vaso, 1, 2)
        self.assertEqual("No hay Cafe", resultado)

    def test_deberia_devolver_no_hay_azucar(self):
        self.maquina.set_azucarero(Azucarero(2))
        vaso = self.maquina.get_tipo_de_vaso("pequeno")
        resultado = self.maquina.get_vaso_de_cafe(vaso, 1, 3)
        self.assertEqual("No hay Azucar", resultado)

    def test_deberia_restar_cafe(self):
        vaso = self.maquina.get_tipo_de_vaso("pequeno")
        self.maquina.get_vaso_de_cafe(vaso, 1, 3)
        self.assertEqual(40, self.maquina.get_cafetera().get_cantidad_cafe())

    def test_deberia_restar_vaso(self):
        vaso = self.maquina.get_tipo_de_vaso("pequeno")
        self.maquina.get_vaso_de_cafe(vaso, 1, 3)
        self.assertEqual(4, self.maquina.get_vasos_pequeno().get_cantidad_vasos())

    def test_deberia_restar_azucar(self):
        vaso = self.maquina.get_tipo_de_vaso("pequeno")
        self.maquina.get_vaso_de_cafe(vaso, 1, 3)
        self.assertEqual(17, self.maquina.get_azucarero().get_cantidad_azucar())

    def test_deberia_devolver_felicitaciones(self):
        vaso = self.maquina.get_tipo_de_vaso("pequeno")
        resultado = self.maquina.get_vaso_de_cafe(vaso, 1, 3)
        self.assertEqual("Felicitaciones", resultado)


if __name__ == "__main__":
    unittest.main()
