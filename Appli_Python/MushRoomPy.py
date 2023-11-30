import sys
from pathlib import Path
from PyQt6.QtWidgets import (
    QApplication,
    QPushButton,
    QLineEdit,
    QLabel,
    QVBoxLayout,
    QFileDialog,
    QProgressBar,
    QFrame,
    QComboBox,
)
import os
import json
from PyQt6.QtGui import QColor, QIcon
from DownloadThread import DownloadThread


class MushroomPyApp(QFrame):
    def __init__(self):
        """
        Initialise l'application MushroomPy.

        - Initialise les éléments de l'interface utilisateur.
        - Initialise les valeurs par défaut et les couleurs.
        """
        super().__init__()
        self.download_thread = None
        self.buttonDL = None
        self.btnCancel = None
        self.languageCombo = None
        self.languages = [
            "Français",
            "Anglais",
            "Espagnol",
            "Allemand",
        ]  # Langues disponibles
        self.currentLanguage = "Français"  # Langue actuelle
        self.backgroundColor = QColor(255, 255, 255)
        self.textButtonColor = QColor(13, 10, 11)
        self.bordureColor = QColor(0, 79, 45)
        self.buttonColor = QColor(220, 178, 83)
        self.destination = str(Path.home() / "Desktop")
        self.downloading = False
        self.initUI()

    def initUI(self):
        """
        Initialise l'interface utilisateur.

        - Définit la fenêtre et son apparence.
        - Ajoute des boutons, des champs et d'autres éléments.
        """
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

        # Menu déroulant du choix de langue
        self.languageCombo = QComboBox(self)
        self.languageCombo.addItems(self.languages)
        self.languageCombo.setCurrentText(self.currentLanguage)
        self.languageCombo.currentTextChanged.connect(self.changeLanguage)
        self.languageCombo.setStyleSheet(
            f"color: {self.textButtonColor.name()}; background-color: {self.backgroundColor.name()}; border: 2px solid {self.bordureColor.name()};"
        )

        # Disposition des éléments
        layout = QVBoxLayout(self)
        layout.addWidget(self.btnOpenJson)
        layout.addWidget(self.entry)
        layout.addWidget(self.btnChooseDir)
        layout.addWidget(self.labelMessage)
        layout.addWidget(self.labelResult)
        layout.addWidget(self.progressBar)
        layout.addWidget(self.btnCancel)
        layout.addWidget(self.languageCombo)

        self.progressBar.hide()
        self.btnCancel.hide()

    def changeLanguage(self, language):
        """
        Change la langue de l'application.

        Args:
            language (str): La nouvelle langue sélectionnée.

        - Met à jour les textes et les éléments de l'interface pour la nouvelle langue.
        """
        # Met à jour la langue actuelle
        self.currentLanguage = language
        # Met à jour les textes des boutons en fonction de la langue
        self.btnOpenJson.setText(self.getTranslation("Open JSON"))
        self.btnChooseDir.setText(self.getTranslation("Choose Destination Folder"))
        self.labelMessage.setText(
            self.getTranslation(
                'Instructions:\n\n1- Enter the desired name for your zip file.\n2- Click "OPEN JSON"\n3- Choose the destination folder'
            )
        )
        self.labelResult.setText("")
        self.btnCancel.setText(self.getTranslation("Cancel"))
        self.entry.setPlaceholderText(self.getTranslation("Name of the .zip file"))

    def getTranslation(self, text):
        """
        Traduit un texte en fonction de la langue actuelle.

        Args:
            text (str): Le texte à traduire.

        Returns:
            str: Le texte traduit.

        - Fonction de traduction en fonction de la langue sélectionnée.
        """
        if self.currentLanguage == "Français":
            if text == "Open JSON":
                return "Ouvrir JSON"
            elif text == "Choose Destination Folder":
                return "Choisissez le dossier de destination"
            elif (
                text
                == 'Instructions:\n\n1- Enter the desired name for your zip file.\n2- Click "OPEN JSON"\n3- Choose the destination folder'
            ):
                return 'Consignes d\'utilisation:\n\n1- Entrez le nom souhaité pour votre fichier zip.\n2- Cliquez sur "OUVRIR JSON"\n3- Choisissez le dossier de destination'
            elif text == "Cancel":
                return "Annuler"
            elif text == "Name of the .zip file":
                return "Nom du fichier .zip"
            else:
                return text
        elif self.currentLanguage == "Anglais":
            if text == "Open JSON":
                return "Open JSON"
            elif text == "Choose Destination Folder":
                return "Choose Destination Folder"
            elif (
                text
                == 'Instructions:\n\n1- Enter the desired name for your zip file.\n2- Click "OPEN JSON"\n3- Choose the destination folder'
            ):
                return 'Instructions:\n\n1- Enter the desired name for your zip file.\n2- Click "OPEN JSON"\n3- Choose the destination folder'
            elif text == "Cancel":
                return "Cancel"
            elif text == "Name of the .zip file":
                return "Name of the .zip file"
            else:
                return text
        elif self.currentLanguage == "Espagnol":
            if text == "Open JSON":
                return "Abrir JSON"
            elif text == "Choose Destination Folder":
                return "Elegir carpeta de destino"
            elif (
                text
                == 'Instructions:\n\n1- Enter the desired name for your zip file.\n2- Click "OPEN JSON"\n3- Choose the destination folder'
            ):
                return 'Instrucciones:\n\n1- Ingrese el nombre deseado para su archivo zip.\n2- Haga clic en "ABRIR JSON"\n3- Elija la carpeta de destino'
            elif text == "Cancel":
                return "Cancelar"
            elif text == "Name of the .zip file":
                return "Nombre del archivo .zip"
            else:
                return text
        elif self.currentLanguage == "Allemand":
            if text == "Open JSON":
                return "JSON öffnen"
            elif text == "Choose Destination Folder":
                return "Zielordner auswählen"
            elif (
                text
                == 'Instructions:\n\n1- Enter the desired name for your zip file.\n2- Click "OPEN JSON"\n3- Choose the destination folder'
            ):
                return 'Anleitung:\n\n1- Geben Sie den gewünschten Namen für Ihre Zip-Datei ein.\n2- Klicken Sie auf "JSON ÖFFNEN"\n3- Wählen Sie den Zielordner aus'
            elif text == "Cancel":
                return "Abbrechen"
            elif text == "Name of the .zip file":
                return "Name der .zip-Datei"
            else:
                return text

    def openJson(self):
        """
        Ouvre un fichier JSON.

        - Affiche une boîte de dialogue pour sélectionner un fichier JSON.
        - Traite les données JSON chargées.
        """
        filepath, _ = QFileDialog.getOpenFileName(
            self, "Ouvrir un fichier JSON", "", "Fichiers JSON (*.json)"
        )
        if filepath:
            with open(filepath, "r", encoding="utf-8") as file:
                json_data = json.load(file)
                self.processJson(json_data)

    def removeDownloadButton(self):
        """
        Supprime le bouton de téléchargement.

        - Parcourt les éléments de l'interface pour trouver et supprimer le bouton de téléchargement.
        """
        for i in reversed(range(self.layout().count())):
            item = self.layout().itemAt(i)
            if item.widget() and item.widget().text() == "↓":
                item.widget().deleteLater()

    def cancelDownload(self):
        """
        Annule le téléchargement en cours.

        - Arrête le thread de téléchargement et met à jour l'interface.
        """
        if self.download_thread is not None and self.download_thread.isRunning():
            self.download_thread.stop()
            self.labelResult.setText("STOP.")
            self.progressBar.hide()

    def chooseDestination(self):
        """
        Choisi un dossier de destination.

        - Affiche une boîte de dialogue pour sélectionner un dossier de destination.
        - Met à jour le chemin de destination.
        """
        default_dir = str(Path.home() / "Desktop")  # Obtient le chemin vers le bureau
        directory = QFileDialog.getExistingDirectory(
            self, "Choisir le dossier de destination", default_dir
        )
        if directory:
            self.destination = directory

    def processJson(self, json_data):
        """
        Traite les données JSON chargées.

        Args:
            json_data (dict): Les données JSON chargées.

        - Affiche un bouton pour télécharger les images à partir des données JSON.
        """
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

        self.buttonDL = QPushButton("↓", self)
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
        """
        Vérifie si l'entrée est valide.

        Args:
            input_string (str): La chaîne à vérifier.

        Returns:
            bool: True si l'entrée est valide, sinon False.

        - Vérifie si la chaîne contient uniquement des caractères alphanumériques.
        """
        return input_string.isalnum()

    def downloadImages(self, json_data, zip_filename):
        """
        Télécharge les images à partir des données JSON.

        Args:
            json_data (dict): Les données JSON contenant les URL des images.
            zip_filename (str): Le nom du fichier .zip de sortie.

        - Démarre un thread pour télécharger les images.
        """
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
        """
        Met à jour la barre de progression.

        Args:
            value (int): La valeur de progression.

        - Met à jour la barre de progression avec la nouvelle valeur.
        """
        self.progressBar.setValue(value)

    def cancelDownload(self):
        """
        Annule le téléchargement en cours.

        - Arrête le thread de téléchargement et met à jour l'interface.
        """
        if self.download_thread is not None and self.download_thread.isRunning():
            self.download_thread.stop()
            self.labelResult.setText("STOP.")
            self.progressBar.hide()
            self.btnCancel.setEnabled(False)  # Désactiver le bouton "Annuler"


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MushroomPyApp()
    ex.show()
    sys.exit(app.exec())
