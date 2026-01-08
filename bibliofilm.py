# =========================================================
# Projet : Bibliofilm
# Module : I-319
# Description  : Gestionnaire de films avec interface graphique
#
# Auteurs :
#   - Taveeporn Matta
#   - Eyuel Worku
# Classe : SI-CA1a
# Date : 08.01.2026
# =========================================================

import json
import os
import tkinter as tk
from tkinter import messagebox, simpledialog

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
lbl_details_contenu = None 

def rafraichir_liste():
    listbox_films.delete(0, tk.END)
    # Tri : Vus en premier
    films.sort(key=lambda x: x.get("vu"), reverse=True)

    for f in films:
        etat = "[✅]" if f.get("vu") else "[   ]"
        titre = f["titre"]
        note = f" | {f['note']}/5" if f.get("note") else "" 
        listbox_films.insert(tk.END, f"{etat} {titre}{note}")

# --- ACTIONS ---

def ouvrir_fenetre_ajouter():
    top = tk.Toplevel()
    top.title("Ajouter")
    
    # Centrage de la fenêtre
    largeur = 300
    hauteur = 150
    ecran_l = top.winfo_screenwidth()
    ecran_h = top.winfo_screenheight()
    x = (ecran_l // 2) - (largeur // 2)
    y = (ecran_h // 2) - (hauteur // 2)
    top.geometry(f"{largeur}x{hauteur}+{x}+{y}")

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

    tk.Button(top, text="Ajouter", command=valider).grid(row=2, column=0, columnspan=2, pady=10)

def afficher_details_selection(event=None):
    # Fonction appelée automatiquement quand on clique sur la liste
    selection = listbox_films.curselection()
    if selection:
        index = selection[0]
        f = films[index]
        
        texte = f"Titre : {f['titre']} ({f['annee']})\n"
        texte += f"Note : {f['note']}/5\n"
        texte += f"Avis : {f['avis']}"
        
        lbl_details_contenu.config(text=texte, fg="black")
    else:
        lbl_details_contenu.config(text="", fg="black")

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
        # force la mise à jour de l'affichage des détails
        afficher_details_selection() 
    else:
        messagebox.showinfo("Info", "Sélectionnez un film d'abord")

def action_supprimer():
    idx = listbox_films.curselection()
    if idx and messagebox.askyesno("Confirmer", "Supprimer ?"):
        del films[idx[0]]
        sauvegarder()
        rafraichir_liste()
        lbl_details_contenu.config(text="") # vide la zone détails

def lancer_interface():
    global listbox_films, lbl_details_contenu
    
    fenetre = tk.Tk()
    fenetre.title("BiblioFilm")
    fenetre.geometry("600x600") 

    # En-tête
    tk.Label(fenetre, text="BIBLIOFILM", font=("Comic Sans MS", 18, "bold"), bg="#222", fg="white").pack(fill="x")

    # Liste
    frame_liste = tk.Frame(fenetre)
    frame_liste.pack(fill="both", expand=True, padx=10, pady=5)

    listbox_films = tk.Listbox(frame_liste, font=("Comic Sans MS", 10))
    listbox_films.pack(side="left", fill="both", expand=True)

    scroll = tk.Scrollbar(frame_liste, command=listbox_films.yview)
    scroll.pack(side="right", fill="y")
    listbox_films.config(yscrollcommand=scroll.set)

    # Quand on sélectionne une ligne (<<ListboxSelect>>), on lance afficher_details_selection
    listbox_films.bind('<<ListboxSelect>>', afficher_details_selection)

    # Zone Détails
    frame_details = tk.LabelFrame(fenetre, text="Détails du film", font=("Arial", 10, "bold"), padx=10, pady=10)
    frame_details.pack(fill="x", padx=10, pady=5)
    
    # permet de couper le texte s'il est trop long
    # justify="left" aligne le texte à gauche
    lbl_details_contenu = tk.Label(frame_details, text="Cliquez sur un film...", justify="left", wraplength=550)
    lbl_details_contenu.pack(anchor="w")

    # Boutons
    frame_btn = tk.Frame(fenetre)
    frame_btn.pack(pady=10)
    
    tk.Button(frame_btn, text="Ajouter", command=ouvrir_fenetre_ajouter).pack(side="left", padx=5)
    tk.Button(frame_btn, text="Noter/Avis", command=action_noter).pack(side="left", padx=5)
    tk.Button(frame_btn, text="Supprimer", command=action_supprimer).pack(side="left", padx=5)

    # Bouton Quitter (Place)
    btn_quit = tk.Button(fenetre, text="X", bg="red", fg="white", font=("Arial", 8, "bold"), command=fenetre.destroy)
    btn_quit.place(relx=1.0, x=-10, y=10, anchor="ne")

    rafraichir_liste()
    fenetre.mainloop()

if __name__ == "__main__":
    charger()
    lancer_interface()