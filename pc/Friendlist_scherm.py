import customtkinter as ctk
from tkinter import *
import json

# Laden van de gegevens uit het JSON-bestand
with open("storage/myFriends.json", "r") as file:
    data = json.load(file)

# Functie om de online status van een vriend te controleren
def is_online(player):
    return player["response"]["players"][0]["personastate"] == 1

# Functie die wordt uitgevoerd bij het klikken op een item in de Listbox
def on_listbox_click(event):
    # krijg de geselecteerde index
    selected_index = listbox.curselection()

    # krijg de tekst op de geselecteerde index
    selected_text = listbox.get(selected_index)

    # Voer hier je gewenste acties uit
    print(f"Geklikt op: {selected_text}")

# Maak een hoofdvenster
root = ctk.CTk()
root.title("Steam Vrienden")

# Verander de achtergrondkleur naar donkerblauw
root.configure(bg="#001F3F")

# Stel de grootte van het venster in (bijv. 300x200 pixels)
root.geometry("300x200")

# Frame voor het uitlijnen aan de linkerkant
left_frame = Frame(root, bg="#001F3F")
left_frame.pack(side=LEFT, padx=10)

# Maak een Listbox voor de vriendenlijst
listbox = Listbox(
    left_frame,
    selectbackground="#242930",
    selectforeground="#ffffff",
    bg="#242930",
    fg="#ffffff",
    width=25,
    height=6,  # Verander de hoogte naar 4
    font=("Arial", 12),
)
listbox.pack(pady=10, side=LEFT)  # Plaats de Listbox aan de linkerkant

# Voeg de klikfunctie toe aan de Listbox
listbox.bind("<ButtonRelease-1>", on_listbox_click)

# Maak een scrollbar en verbind deze met de Listbox
scrollbar = Scrollbar(left_frame, command=listbox.yview)
scrollbar.pack(side=LEFT, fill=Y)  # Plaats de scrollbar aan de linkerkant
listbox.config(yscrollcommand=scrollbar.set)  # Synchroniseer de Listbox met de scrollbar

# Loop over elke vriend en voeg een item toe aan de Listbox
for friend in data["friendslist"]["friends"]:
    personaname = friend["response"]["players"][0]["personaname"]
    online_status = "Online" if is_online(friend) else "Offline"
    listbox.insert(END, f"{personaname} - {online_status}")

# Start de CustomTkinter event loop
root.mainloop()
