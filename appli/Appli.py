import sys
from pathlib import Path
from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QPushButton,
    QLineEdit,
    QLabel,
    QVBoxLayout,
    QWidget,
    QFileDialog,
    QProgressBar,
    QFrame,
)
import requests
from zipfile import ZipFile
import os
import json
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QColor, QIcon


class MushroomPyApp(QFrame):
    def __init__(self):
        super().__init__()
        self.buttonDL = None
        self.backgroundColor = QColor(255, 255, 255)
        self.textButtonColor = QColor(13, 10, 11)
        self.bordureColor = QColor(0, 79, 45)
        self.buttonColor = QColor(220, 178, 83)
        self.destination = str(Path.home() / "Desktop")
        self.downloading = (
            False  # Ajout de la variable pour suivre l'état du téléchargement
        )
        self.initUI()

    def initUI(self):
        # Définition de la fenêtre
        self.setWindowTitle("MushroomPy")
        self.setGeometry(100, 100, 400, 200)
        icon_path = "appli\icone.ico"
        icon = QIcon(icon_path)
        self.setWindowIcon(icon)
        self.setStyleSheet(f"background-color: {self.backgroundColor.name()};")
        # Bouton pour ouvrir le fichier JSON
        self.btnOpenJson = QPushButton("Ouvrir JSON", self)
        self.btnOpenJson.clicked.connect(self.openJson)
        self.btnOpenJson.setStyleSheet(
            f"background-color: {self.buttonColor.name()}; color: {self.textButtonColor.name()}; border: 2px solid {self.bordureColor.name()};"
        )
        # Champ d'entrée pour le nom du fichier zip
        self.entry = QLineEdit(self)
        self.entry.setPlaceholderText("Nom du fichier .zip")
        self.entry.setStyleSheet(f"color: {self.textButtonColor.name()};")

        # Bouton pour choisir le dossier de destination
        self.btnChooseDir = QPushButton("Choisir le dossier de destination", self)
        self.btnChooseDir.clicked.connect(self.chooseDestination)
        self.btnChooseDir.setStyleSheet(
            f"background-color: {self.buttonColor.name()}; color: {self.textButtonColor.name()}; border: 2px solid {self.bordureColor.name()};"
        )

        # Consignes d'utilisation
        self.labelMessage = QLabel(
            'Consignes d\'utilisation:\n\n1- Entrez le nom souhaité pour votre fichier zip.\n2- Cliquez sur "OUVRIR JSON"\n3- Choisissez le dossier de destination',
            self,
        )
        self.labelMessage.setStyleSheet(f"color: {self.textButtonColor.name()};")
        self.labelMessage.setWordWrap(True)

        # Label résultat
        self.labelResult = QLabel("", self)
        self.labelResult.setStyleSheet(f"color: {self.textButtonColor.name()};")

        # Barre de progression
        self.progressBar = QProgressBar(self)
        self.progressBar.setValue(0)

        # self.btnCancel = QPushButton("Annuler", self)
        # self.btnCancel.clicked.connect(self.cancelDownload)
        # self.btnCancel.setStyleSheet(
        #    f"background-color: {self.buttonColor.name()}; color: {self.textButtonColor.name()}; border: 2px solid {self.bordureColor.name()};"
        # )

        # Disposition des éléments
        layout = QVBoxLayout(self)
        layout.addWidget(self.btnOpenJson)
        layout.addWidget(self.entry)
        layout.addWidget(self.btnChooseDir)
        layout.addWidget(self.labelMessage)
        layout.addWidget(self.labelResult)
        layout.addWidget(self.progressBar)
        # layout.addWidget(self.btnCancel)

        self.progressBar.hide()
        # self.btnCancel.hide()

    def openJson(self):
        filepath, _ = QFileDialog.getOpenFileName(
            self, "Ouvrir un fichier JSON", "", "Fichiers JSON (*.json)"
        )
        if filepath:
            with open(filepath, "r") as file:
                json_data = json.load(file)
                self.processJson(json_data)

    def removeDownloadButton(self):
        # Trouve et retire le bouton de téléchargement
        for i in reversed(range(self.layout().count())):
            item = self.layout().itemAt(i)
            if item.widget() and item.widget().text() == "Télécharger les images":
                item.widget().deleteLater()

    # def cancelDownload(self):
    #    self.labelResult.setText("Téléchargement annulé.")
    #    self.progressBar.hide()  # Cacher la barre de progression
    #    self.btnCancel.setEnabled(False)  # Désactiver le bouton "Annuler"
    #    self.buttonDL.setEnabled(False)  # Désactiver le bouton de téléchargement
    #    self.downloading = False  # Marquer comme étant non en cours de téléchargement

    def chooseDestination(self):
        default_dir = str(Path.home() / "Desktop")  # Obtient le chemin vers le bureau
        directory = QFileDialog.getExistingDirectory(
            self, "Choisir le dossier de destination", default_dir
        )
        if directory:
            self.destination = directory

    def processJson(self, json_data):
        if not self.isValidInput(self.entry.text()):
            self.labelResult.setText(
                "Nom invalide. Utilisez uniquement des caractères alphanumériques."
            )
            return

        self.labelResult.setText("Fichier JSON chargé avec succès!")
        self.progressBar.show()
        self.progressBar.setValue(0)

        if self.buttonDL is not None:
            self.buttonDL.deleteLater()  # Supprime le bouton de téléchargement précédent

        self.buttonDL = QPushButton("Télécharger les images", self)
        self.buttonDL.clicked.connect(
            lambda: self.downloadImages(
                json_data, os.path.join(self.destination, self.entry.text() + ".zip")
            )
        )

        layout = self.layout()
        layout.addWidget(self.buttonDL)

        #    self.btnCancel.setEnabled(False)  # Désactiver le bouton "Annuler"
        self.downloading = True  # Marquer comme étant en cours de téléchargement

    #    self.btnCancel.show()  # Montrer le bouton "Annuler

    def isValidInput(self, input_string):
        return input_string.isalnum()

    def downloadImages(self, json_data, zip_filename):
        if not self.isValidInput(self.entry.text()):
            self.labelResult.setText(
                "Nom invalide. Utilisez uniquement des caractères alphanumériques."
            )
            return

        total_images = len(json_data["rq_result"])
        progress_step = 100 / total_images

        with ZipFile(zip_filename, "w") as zipf:
            for i, item in enumerate(json_data["rq_result"]):
                if not self.downloading:
                    break  # Si le téléchargement a été annulé, arrêtez le téléchargement

                url = item["lien_oeuvre"]
                response = requests.get(url)
                image_data = response.content
                nomfic = self.entry.text() + "_"
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
                self.progressBar.setValue(int((i + 1) * progress_step))
        # self.downloading = False  # Marquer comme étant non en cours de téléchargement
        # self.btnCancel.setEnabled(False)  # Désactiver le bouton "Annuler"
        # self.btnCancel.hide()  # Cacher le bouton "Annuler"


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MushroomPyApp()
    ex.show()
    sys.exit(app.exec())
