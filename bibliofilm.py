import json
import os
import tkinter as tk
from tkinter import messagebox

# --- GESTION DES DONNÉES ---
FICHIER = "films.json"
films = []

def charger():
    global films
    if os.path.exists(FICHIER):
        try:
            with open(FICHIER, "r", encoding="utf-8") as f:
                films = json.load(f)
        except:
            films = []
    else:
        films = []

def sauvegarder():
    try:
        with open(FICHIER, "w", encoding="utf-8") as f:
            json.dump(films, f, ensure_ascii=False, indent=2)
    except:
        messagebox.showerror("Erreur", "Impossible de sauvegarder")

# --- INTERFACE GRAPHIQUE ---
listbox_films = None

def rafraichir_liste():
    listbox_films.delete(0, tk.END)
    # Affichage simple sans tri
    for f in films:
        titre = f["titre"]
        note = f" | {f['note']}/5" if f.get("note") else ""
        listbox_films.insert(tk.END, f"{titre}{note}")

def lancer_interface():
    global listbox_films
    fenetre = tk.Tk()
    fenetre.title("BiblioFilm")
    fenetre.geometry("500x450")

    # Titre
    tk.Label(fenetre, text="BIBLIOFILM", font=("Comic Sans MS", 18, "bold"), bg="#222", fg="white").pack(fill="x")

    # Zone Liste + Scrollbar
    frame_liste = tk.Frame(fenetre)
    frame_liste.pack(fill="both", expand=True, padx=10, pady=10)

    listbox_films = tk.Listbox(frame_liste, font=("Comic Sans MS", 10))
    listbox_films.pack(side="left", fill="both", expand=True)

    scroll = tk.Scrollbar(frame_liste, command=listbox_films.yview)
    scroll.pack(side="right", fill="y")
    listbox_films.config(yscrollcommand=scroll.set)

    rafraichir_liste()
    fenetre.mainloop()

if __name__ == "__main__":
    charger()
    lancer_interface()