import unittest
from unittest.mock import patch
from io import StringIO
from PC3 import process_names

# Clase de prueba para automatizar los casos
class TestProcessNames(unittest.TestCase):

    @patch('builtins.input', side_effect=['John', '70', 'Jane', '85', ''])
    @patch('sys.stdout', new_callable=StringIO)
    def test_category(self, mock_stdout, mock_input):
        process_names()
        output = mock_stdout.getvalue().strip()
        expected_output = "Categoría -80: llave de 2\nCategoría +80: llave de 2"
        self.assertEqual(output.strip(), expected_output.strip())

    @patch('builtins.input', side_effect=['John', '85', ''])
    @patch('sys.stdout', new_callable=StringIO)
    def test_only_above_80(self, mock_stdout, mock_input):
        process_names()
        output = mock_stdout.getvalue().strip()
        expected_output = "Llave vacía\nCategoría +80: llave de 2"
        self.assertEqual(output.strip(), expected_output.strip())

    @patch('builtins.input', side_effect=['Jane', '65', ''])
    @patch('sys.stdout', new_callable=StringIO)
    def test_only_below_80(self, mock_stdout, mock_input):
        process_names()
        output = mock_stdout.getvalue().strip()
        expected_output = "Categoría -80: llave de 2\nLlave vacía"
        self.assertEqual(output.strip(), expected_output.strip())

    @patch('builtins.input', side_effect=[''])
    @patch('sys.stdout', new_callable=StringIO)
    def test_no_participants(self, mock_stdout, mock_input):
        process_names()
        output = mock_stdout.getvalue().strip()
        expected_output = "Llave vacía\nLlave vacía"
        self.assertEqual(output.strip(), expected_output.strip())
    @patch('builtins.input', side_effect=['Jane', '90', 'John', '85', 'Jack', '100', ''])
    @patch('sys.stdout', new_callable=StringIO)
    def test_only_below_80_2(self, mock_stdout, mock_input):
        process_names()
        output = mock_stdout.getvalue().strip()
        expected_output = "Llave vacía\nCategoría +80: llave de 4"
        self.assertEqual(output.strip(), expected_output.strip())

if __name__ == '__main__':
    unittest.main()