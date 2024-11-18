import unittest
from main import adicionar, subtrair, multiplicar, dividir

class TestCalculadora(unittest.TestCase):
    def test_adicionar(self):
        self.assertEqual(adicionar(2, 3), 5)

    def test_subtrair(self):
        self.assertEqual(subtrair(10, 4), 6)

    def test_multiplicar(self):
        self.assertEqual(multiplicar(3, 3), 9)

    def test_dividir(self):
        self.assertEqual(dividir(8, 2), 4)
        with self.assertRaises(ValueError):
            dividir(10, 0)

if __name__ == "__main__":
    unittest.main()
