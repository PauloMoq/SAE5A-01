import requests
from zipfile import ZipFile
from PyQt6.QtCore import Qt, QThread, pyqtSignal
import os


class DownloadThread(QThread):
    progress_updated = pyqtSignal(int)

    def __init__(self, json_data, destination, zip_filename, entry_text):
        super().__init__()
        self.json_data = json_data
        self.destination = destination
        self.zip_filename = zip_filename
        self.entry_text = entry_text
        self.running = True

    def run(self):
        total_images = len(self.json_data["rq_result"])
        progress_step = 100 / total_images

        with ZipFile(self.zip_filename, "w") as zipf:
            for i, item in enumerate(self.json_data["rq_result"]):
                if not self.running:
                    break

                url = item["lien_oeuvre"]
                response = requests.get(url)
                image_data = response.content
                nomfic = self.entry_text + "_"
                nomfic += item["auteur_oeuvre"] + "_" + item["date_oeuvre"] + "_"
                if item["support_oeuvre"] != "":
                    nomfic += item["support_oeuvre"] + "_"
                if item["zonegeo_oeuvre"] != "":
                    nomfic += item["zonegeo_oeuvre"] + "_"
                nomfic += ".jpg"
                filename = os.path.join(self.destination, os.path.basename(nomfic))
                with open(filename, "wb") as image_file:
                    image_file.write(image_data)
                zipf.write(filename, os.path.basename(nomfic))
                os.remove(filename)
                self.progress_updated.emit(int((i + 1) * progress_step))

    def stop(self):
        self.running = False
