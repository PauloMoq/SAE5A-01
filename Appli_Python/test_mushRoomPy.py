import unittest
from unittest.mock import patch
from PyQt6.QtTest import QTest
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication
from MushRoomPy import MushroomPyApp
from pathlib import Path


class TestMushroomPyApp(unittest.TestCase):
    def setUp(self):
        self.app = QApplication([])
        self.window = MushroomPyApp()

    def tearDown(self):
        self.window.close()

    def test_openJson(self):
        json_filepath = "./exemple_test.json"

        # Simule un clic sur le bouton et vérifie si le texte a changé
        with patch(
            "builtins.open", unittest.mock.mock_open(read_data='{"key": "value"}')
        ):
            QTest.mouseClick(self.window.btnOpenJson, Qt.MouseButton.LeftButton)
        self.assertEqual(
            self.window.labelResult.text(),
            "Nom invalide. Utilisez uniquement des caractères alphanumériques.",
        )

    def test_chooseDestination(self):
        # Vérifie si le chemin a changé
        QTest.mouseClick(self.window.btnChooseDir, Qt.MouseButton.LeftButton)
        self.assertNotEqual(self.window.destination, str(Path.home() / "Desktop"))

    def test_isValidInput(self):
        # Test avec un entrée invalide
        valid_input = "ValidInput123"
        self.assertTrue(self.window.isValidInput(valid_input))

        # Test avec une entrée valide
        invalid_input = "!@#$%^"
        self.assertFalse(self.window.isValidInput(invalid_input))


if __name__ == "__main__":
    unittest.main()
