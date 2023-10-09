import tkinter as tk
from tkinterdnd2 import DND_FILES, TkinterDnD
from PIL import Image, ImageTk
import requests
from io import BytesIO
import json
import os
from tkinter import filedialog
from zipfile import ZipFile

def download_images(json_data, zip_filename):
    with ZipFile(zip_filename, 'w') as zipf:
        for item in json_data['rq_result']:
            url = item['lien_oeuvre']
            response = requests.get(url)
            image_data = response.content
            nomfic = item['auteur_oeuvre']+'_'+item['date_oeuvre']+'_'
            if item['support_oeuvre'] != "":
                nomfic += item['support_oeuvre']+'_'
            if item['zonegeo_oeuvre'] != "":
                nomfic += item['zonegeo_oeuvre']+'_'  
            nomfic += '.jpg'  
            filename = os.path.basename(nomfic)
            with open(filename, 'wb') as image_file:
                image_file.write(image_data)
            zipf.write(filename)
            os.remove(filename)

def open_json():
    filepath = filedialog.askopenfilename(filetypes=[("Fichiers JSON", "*.json")])
    if filepath:
        with open(filepath, 'r') as file:
            json_data = json.load(file)
            process_json(json_data)

def process_json(json_data):
    label_result.config(text="Fichier JSON chargé avec succès!")
    buttonDL = tk.Button(root, text="Télécharger les images", command=lambda: download_images(json_data, "test.zip"))
    buttonDL.pack()

def drop(event):
    filepath = event.data.strip()
    with open(filepath, 'r') as file:
        json_data = json.load(file)
    label_result.config(text="Fichier JSON chargé avec succès!")
    buttonDL = tk.Button(root, text="Télécharger les images", command=lambda: download_images(json_data, "test.zip"))
    buttonDL.pack()

root = TkinterDnD.Tk()
root.minsize(400, 300)
root.maxsize(1200, 900)
root.title("MushRoomPy")
root.eval('tk::PlaceWindow . center')
root.configure(bg="#FFFAFA")

# Ajout d'un bouton pour ouvrir le fichier JSON
button = tk.Button(root, text="Ouvrir JSON", command=open_json)
button.pack()

# Ajoute d'un scrollbar
scrollbar = tk.Scrollbar(root, bg="#004F2D", troughcolor="#FFCD00")

entry = tk.Entry(root, selectbackground="#004F2D", selectforeground="#FFCD00")

label = tk.Label(root, bg="#FFFAFA", text="Faites glisser le fichier JSON ici")
label.pack(pady=10)

label_result = tk.Label(root, bg="#FFFAFA", text="")
label_result.pack(pady=10)

root.drop_target_register(DND_FILES)
root.dnd_bind('<<Drop>>', drop)

root.mainloop()
