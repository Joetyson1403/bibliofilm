import json
import os
import tkinter as tk
from tkinter import messagebox, simpledialog # Ajout de simpledialog

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
    
    # Tri de la liste
    # On met les films vus (True) en premier
    films.sort(key=lambda x: x.get("vu"), reverse=True)

    for f in films:
        etat = "[X]" if f.get("vu") else "[ ]"
        titre = f["titre"]
        note = f" | {f['note']}/5" if f.get("note") else ""
        listbox_films.insert(tk.END, f"{etat} {titre}{note}")

# --- Actions ---

def ouvrir_fenetre_ajouter():
    top = tk.Toplevel()
    top.title("Ajouter")
    top.geometry("300x150")

    # GRID
    tk.Label(top, text="Titre :").grid(row=0, column=0, padx=10, pady=10)
    e_titre = tk.Entry(top)
    e_titre.grid(row=0, column=1, padx=10, pady=10)

    tk.Label(top, text="Année :").grid(row=1, column=0, padx=10, pady=5)
    e_annee = tk.Entry(top)
    e_annee.grid(row=1, column=1, padx=10, pady=5)

    def valider():
        if e_titre.get():
            films.append({"titre": e_titre.get(), "annee": e_annee.get(), "vu": False, "note": None, "avis": ""})
            sauvegarder()
            rafraichir_liste()
            top.destroy()
        else:
            messagebox.showwarning("Erreur", "Titre requis")

    tk.Button(top, text="Sauver", command=valider).grid(row=2, column=0, columnspan=2, pady=10)

def action_details():
    idx = listbox_films.curselection()
    if idx:
        f = films[idx[0]]
        messagebox.showinfo("Détails", f"Titre: {f['titre']}\nAvis: {f['avis']}")

def action_noter():
    idx = listbox_films.curselection()
    if idx:
        f = films[idx[0]]
        f["vu"] = True
        n = simpledialog.askinteger("Note", "Note (1-5):", minvalue=1, maxvalue=5)
        if n: f["note"] = n
        a = simpledialog.askstring("Avis", "Avis:")
        if a: f["avis"] = a
        sauvegarder()
        rafraichir_liste()

def action_supprimer():
    idx = listbox_films.curselection()
    if idx and messagebox.askyesno("Confirmer", "Supprimer ?"):
        del films[idx[0]]
        sauvegarder()
        rafraichir_liste()

def lancer_interface():
    global listbox_films
    fenetre = tk.Tk()
    fenetre.title("BiblioFilm")
    fenetre.geometry("500x450")

    tk.Label(fenetre, text="BIBLIOFILM", font=("Comic Sans MS", 18, "bold"), bg="#222", fg="white").pack(fill="x")

    frame_liste = tk.Frame(fenetre)
    frame_liste.pack(fill="both", expand=True, padx=10, pady=10)

    listbox_films = tk.Listbox(frame_liste, font=("Comic Sans MS", 10))
    listbox_films.pack(side="left", fill="both", expand=True)

    scroll = tk.Scrollbar(frame_liste, command=listbox_films.yview)
    scroll.pack(side="right", fill="y")
    listbox_films.config(yscrollcommand=scroll.set)

    # Zone Boutons
    frame_btn = tk.Frame(fenetre)
    frame_btn.pack(pady=10)
    tk.Button(frame_btn, text="Ajouter", command=ouvrir_fenetre_ajouter).pack(side="left", padx=5)
    tk.Button(frame_btn, text="Détails", command=action_details).pack(side="left", padx=5)
    tk.Button(frame_btn, text="Noter/Avis", command=action_noter).pack(side="left", padx=5)
    tk.Button(frame_btn, text="Supprimer", command=action_supprimer).pack(side="left", padx=5)

    rafraichir_liste()
    fenetre.mainloop()

if __name__ == "__main__":
    charger()
    lancer_interface()