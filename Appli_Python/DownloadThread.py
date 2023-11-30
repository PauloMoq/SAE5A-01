import requests
from zipfile import ZipFile
from PyQt6.QtCore import QThread, pyqtSignal
import os


class DownloadThread(QThread):
    """
    Thread de téléchargement d'images.

    Attributes:
        progress_updated (pyqtSignal): Signal émis lors de la mise à jour de la progression.

    Methods:
        __init__(self, json_data, destination, zip_filename, entry_text):
            Initialise le thread de téléchargement.

        run(self):
            Exécute le téléchargement des images.

        stop(self):
            Arrête le téléchargement en cours.
    """

    progress_updated = pyqtSignal(int)

    def __init__(self, json_data, destination, zip_filename, entry_text):
        """
        Initialise le thread de téléchargement.

        Args:
            json_data (dict): Les données JSON contenant les URL des images.
            destination (str): Le chemin du dossier de destination.
            zip_filename (str): Le nom du fichier .zip de sortie.
            entry_text (str): Le texte d'entrée pour le nom du fichier.
        """
        super().__init__()
        self.json_data = json_data
        self.destination = destination
        self.zip_filename = zip_filename
        self.entry_text = entry_text
        self.running = True

    def run(self):
        """
        Exécute le téléchargement des images.

        - Télécharge les images à partir des URLs fournies dans les données JSON.
        - Crée un fichier .zip contenant les images téléchargées.
        - Signale la progression via le signal 'progress_updated'.
        """
        total_images = len(self.json_data["rq_result"])
        progress_step = 100 / total_images

        # Liste pour stocker les noms des fichiers téléchargés
        downloaded_files = []

        for i, item in enumerate(self.json_data["rq_result"]):
            if not self.running:
                break

            url = item["lien_oeuvre"]
            try:
                response = requests.get(url)
                response.raise_for_status()
                image_data = response.content
            except requests.exceptions.RequestException as e:
                continue  # Ignore l'image si le lien n'est pas accessible

            nomfic = self.entry_text + "_"
            nomfic += item["auteur_oeuvre"] + "_" + item["date_oeuvre"] + "_"
            if item["support_oeuvre"] != "":
                nomfic += item["support_oeuvre"] + "_"
            if item["zonegeo_oeuvre"] != "":
                nomfic += item["zonegeo_oeuvre"] + "_"
            nomfic += ".jpg"

            # Vérifier si le fichier existe déjà, si oui, incrémenter le nom
            base_filename, file_extension = os.path.splitext(nomfic)
            counter = 1
            while os.path.exists(os.path.join(self.destination, nomfic)):
                nomfic = f"{base_filename}({counter}){file_extension}"
                counter += 1

            filename = os.path.join(self.destination, nomfic)
            with open(filename, "wb") as image_file:
                image_file.write(image_data)

            # Ajouter le nom du fichier à la liste des fichiers téléchargés
            downloaded_files.append(nomfic)

            self.progress_updated.emit(int((i + 1) * progress_step))

        # Créer l'archive ZIP après avoir téléchargé toutes les images
        with ZipFile(self.zip_filename, "w") as zipf:
            for downloaded_file in downloaded_files:
                file_path = os.path.join(self.destination, downloaded_file)
                zipf.write(file_path, os.path.basename(downloaded_file))

        # Supprimer les fichiers locaux après la création de l'archive ZIP
        for downloaded_file in downloaded_files:
            file_path = os.path.join(self.destination, downloaded_file)
            os.remove(file_path)

    def stop(self):
        """
        Arrête le téléchargement en cours.

        - Met fin à l'exécution du thread.
        """
        self.running = False
