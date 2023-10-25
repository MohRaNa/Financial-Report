import unittest
import sys
import os

# Agrega la ruta del directorio "src" para importar los módulos
sys.path.append(os.path.join(os.path.dirname(__file__), '../src'))

from patterns.web_report import create_content, create_file

class TestWebReport(unittest.TestCase):
    def test_create_content(self):
        # Asegúrate de que tienes datos de prueba o un conjunto de datos de muestra
        sample_data = [...]  # Inserta tus datos de muestra aquí
        content = create_content(sample_data)
        self.assertTrue(content, "No se creó el contenido HTML correctamente")

    def test_create_file(self):
        # Asegúrate de que tienes datos de prueba o un conjunto de datos de muestra
        sample_content = "HTML Content"  # Cambia esto por tu contenido de muestra
        create_file(sample_content)

        self.assertTrue(os.path.exists("financial-report.html"), "El archivo HTML no se creó")

if __name__ == '__main__':
    unittest.main()
