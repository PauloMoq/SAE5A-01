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
import os
import json
from PyQt6.QtGui import QColor, QIcon
from DownloadThread import DownloadThread


class MushroomPyApp(QFrame):
    def __init__(self):
        super().__init__()
        self.download_thread = None
        self.buttonDL = None
        self.btnCancel = None  # Ajout du bouton d'annulation
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

        # Ajout du bouton d'annulation
        self.btnCancel = QPushButton("Annuler", self)
        self.btnCancel.clicked.connect(self.cancelDownload)
        self.btnCancel.setStyleSheet(
            f"background-color: {self.buttonColor.name()}; color: {self.textButtonColor.name()}; border: 2px solid {self.bordureColor.name()};"
        )
        self.btnCancel.hide()

        # Disposition des éléments
        layout = QVBoxLayout(self)
        layout.addWidget(self.btnOpenJson)
        layout.addWidget(self.entry)
        layout.addWidget(self.btnChooseDir)
        layout.addWidget(self.labelMessage)
        layout.addWidget(self.labelResult)
        layout.addWidget(self.progressBar)
        layout.addWidget(self.btnCancel)

        self.progressBar.hide()
        self.btnCancel.hide()

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

    def cancelDownload(self):
        if self.download_thread is not None and self.download_thread.isRunning():
            self.download_thread.stop()
            self.labelResult.setText("Téléchargement annulé.")
            self.progressBar.hide()

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
        self.buttonDL.setStyleSheet(
            f"background-color: {self.buttonColor.name()}; color: {self.textButtonColor.name()}; border: 2px solid {self.bordureColor.name()};"
        )
        layout = self.layout()
        layout.addWidget(self.buttonDL)

        self.btnCancel.setEnabled(False)  # Désactiver le bouton "Annuler"
        self.downloading = True  # Marquer comme étant en cours de téléchargement

        self.btnCancel.show()  # Montrer le bouton "Annuler

    def isValidInput(self, input_string):
        return input_string.isalnum()

    def downloadImages(self, json_data, zip_filename):
        if not self.isValidInput(self.entry.text()):
            self.labelResult.setText(
                "Nom invalide. Utilisez uniquement des caractères alphanumériques."
            )
            return

        self.labelResult.setText("Téléchargement en cours...")
        self.progressBar.show()
        self.progressBar.setValue(0)

        self.btnCancel.setEnabled(True)  # Activer le bouton "Annuler"

        self.download_thread = DownloadThread(
            json_data, self.destination, zip_filename, self.entry.text()
        )
        self.download_thread.progress_updated.connect(self.updateProgressBar)
        self.download_thread.start()

    def updateProgressBar(self, value):
        self.progressBar.setValue(value)

    def cancelDownload(self):
        if self.download_thread is not None and self.download_thread.isRunning():
            self.download_thread.stop()
            self.labelResult.setText("Téléchargement annulé.")
            self.progressBar.hide()
            self.btnCancel.setEnabled(False)  # Désactiver le bouton "Annuler"


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MushroomPyApp()
    ex.show()
    sys.exit(app.exec())
