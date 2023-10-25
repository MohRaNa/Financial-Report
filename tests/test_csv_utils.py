import unittest
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '../src'))

from patterns.csv_utils import parse_file

class TestCSVUtils(unittest.TestCase):
    def test_parse_file(self):
        # Cambia la ruta al archivo CSV si es necesario
        csv_file = "taxi-data.csv"
        rides = parse_file(csv_file)
        self.assertTrue(len(rides) > 0, "No se cargaron datos desde el archivo CSV")

if __name__ == '__main__':
    unittest.main()
