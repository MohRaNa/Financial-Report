import unittest
import sys
import os
from datetime import datetime
from patterns.csv_utils import Ride
from patterns.web_report import create_content, create_file

# Agrega la ruta del directorio "src" para importar los módulos
sys.path.append(os.path.join(os.path.dirname(__file__), '../src'))

class TestWebReport(unittest.TestCase):
    def test_create_content(self):
        # Datos de ejemplo
        sample_data = [
            Ride(
                error="",
                taxi_id=1,
                pick_up_time=datetime(2023, 10, 25, 12, 0, 0),
                drop_of_time=datetime(2023, 10, 25, 13, 0, 0),
                passenger_count=2,
                trip_distance=5.0,
                tolls_amount=10.0
            ),
            Ride(
                error="",
                taxi_id=2,
                pick_up_time=datetime(2023, 10, 25, 13, 0, 0),
                drop_of_time=datetime(2023, 10, 25, 14, 0, 0),
                passenger_count=3,
                trip_distance=7.0,
                tolls_amount=12.0
            ),
        ]

        content = create_content(sample_data)
        self.assertTrue(content, "No se creó el contenido HTML correctamente")

    def test_create_file(self):
        sample_content = "Se creo "  
        create_file(sample_content)

        self.assertTrue(os.path.exists("financial-report.html"), "El archivo HTML no se creó")

if __name__ == '__main__':
    unittest.main()
