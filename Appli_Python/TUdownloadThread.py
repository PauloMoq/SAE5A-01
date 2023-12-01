import unittest
import tempfile
import shutil
import os
from unittest.mock import patch, MagicMock
from PyQt6.QtCore import Qt
from DownloadThread import (
    DownloadThread,
)


class TestDownloadThread(unittest.TestCase):
    def setUp(self):
        self.json_data = {
            "rq_user": "Utilisateur1",
            "rq_nboeuvre": "1",
            "rq_arg": {
                "date_debut": "2022-01-01",
                "date_fin": "2022-12-31",
                "zone_geo": "Paris",
                "support": "Toile",
            },
            "rq_result": [
                {
                    "date_oeuvre": "2022-06-15",
                    "auteur_oeuvre": "",
                    "support_oeuvre": "Toile",
                    "zonegeo_oeuvre": "Paris",
                    "lien_oeuvre": "https://via.placeholder.com/300",
                }
            ],
        }
        self.destination = tempfile.mkdtemp()
        self.zip_filename = os.path.join(self.destination, "test_archive.zip")
        self.entry_text = "test_archive"
        self.download_thread = DownloadThread(
            self.json_data, self.destination, self.zip_filename, self.entry_text
        )

    def tearDown(self):
        shutil.rmtree(self.destination)

    def test_run_method(self):
        # Mocking requests.get to simulate successful image download
        with patch("requests.get") as mock_get:
            mock_response = MagicMock()
            mock_response.content = b"Simulated image content"
            mock_get.return_value = mock_response

            # Run the thread
            self.download_thread.run()

            # Check if the zip file is created
            self.assertTrue(os.path.exists(self.zip_filename))

            # Check if files are removed after creating the zip archive
            self.assertFalse(
                os.path.exists(os.path.join(self.destination, "downloaded_file.jpg"))
            )

    def test_stop_method(self):
        # Run the thread
        self.download_thread.start()

        # Stop the thread
        self.download_thread.stop()

        # Wait for the thread to finish
        self.download_thread.wait()

        # Check if the thread has stopped
        self.assertFalse(self.download_thread.isRunning())


if __name__ == "__main__":
    unittest.main()
