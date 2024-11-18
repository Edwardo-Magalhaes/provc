import unittest
from main import adicionar, subtrair

class TestCalculadora(unittest.TestCase):
    def test_adicionar(self):
        self.assertEqual(adicionar(2, 3), 5)
    
    def test_subtrair(self):
        self.assertEqual(subtrair(5, 3), 2)

if __name__ == '__main__':
    unittest.main()
