import tkinter as tk
from tkinterdnd2 import DND_FILES, TkinterDnD
from PIL import Image, ImageTk
import requests
from io import BytesIO
import json

def drop(event):
    filepath = event.data.strip()
    with open(filepath, 'r') as file:
        json_data = json.load(file)

    label_result.config(text="Fichier JSON chargé avec succès!")
    for item in json_data['rq_result']:
        url = item['lien_oeuvre']
        response = requests.get(url)
        image_data = response.content
        image = Image.open(BytesIO(image_data))
        photo = ImageTk.PhotoImage(image)
        label = tk.Label(root, bd=2, relief="solid", bordercolor="#004F2D", image=photo)
        label.image = photo
        label.pack()

root = TkinterDnD.Tk()
root.minsize(400, 300)
root.maxsize(1200, 900)
root.title("A déterminer")
root.eval('tk::PlaceWindow . center')
root.configure(bg="#FFFAFA")

scrollbar = tk.Scrollbar(root, bg="#004F2D", troughcolor="#FFCD00")
entry = tk.Entry(root, selectbackground="#004F2D", selectforeground="#FFCD00")

label = tk.Label(root, bg="#FFFAFA", text="Faites glisser le fichier JSON ici")
label.pack(pady=10)

label_result = tk.Label(root, bg="#FFFAFA", text="")
label_result.pack(pady=10)

root.drop_target_register(DND_FILES)
root.dnd_bind('<<Drop>>', drop)

root.mainloop()
