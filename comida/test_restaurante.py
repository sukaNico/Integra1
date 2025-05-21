import unittest
from unittest.mock import Mock, MagicMock
from restaurante import Restaurante
from menu import Plato


class TestRestauranteAgregarPlatoAPedido(unittest.TestCase):
        
    def test_agregar_plato_existente(self):

        self.menu_mock = MagicMock()
        self.restaurante = Restaurante(self.menu_mock)
        self.pedido_mock = MagicMock()

        plato = Plato("pasta carbonara", 28000)
        self.menu_mock.obtener_plato.return_value = plato
        
        resultado = self.restaurante.agregar_plato_a_pedido(self.pedido_mock, "pasta carbonara")
        
        self.assertTrue(resultado)
        self.menu_mock.obtener_plato.assert_called_once_with("pasta carbonara")
        self.pedido_mock.agregar_plato.assert_called_once_with(plato)
        

if __name__ == '__main__':
    unittest.main()