# 🎬 BiblioFilm

**BiblioFilm** est une application de gestion de vidéothèque personnelle développée en Python avec Tkinter pour le projet d'évaluation du module I-319. Elle permet de lister vos films, de suivre ceux que vous avez vus et d'enregistrer vos critiques et notes détaillées.

---

## ✨ Fonctionnalités

* **Gestion de Collection** : Ajoutez facilement des films (Titre + Année).
* **Suivi de Visionnage** :
    * Indicateur visuel clair : ✅ pour les films vus, ⭕ pour les films à voir.
    * Tri automatique : Les films vus apparaissent en haut de la liste.
* **Système de Notation** : Notez vos films de 1 à 5.
* **Critiques Détaillées** : Espace de texte défilant (scroll) permettant d'écrire des avis de n'importe quelle longueur.
* **Sauvegarde Automatique** : Toutes les données sont enregistrées localement dans un fichier `films.json`.
* **Ergonomie** :
    * Interface claire et centrée sur l'écran.

## 🛠️ Prérequis

* **Python 3.x** installé sur votre machine.
* Le module `tkinter` (inclus par défaut avec Python).

## 🚀 Installation et Lancement

1.  **Récupérer le projet** :
    Téléchargez le fichier `bibliofilm.py` (ou le nom que vous avez donné à votre script).

2.  **Lancer l'application** :
    Ouvrez un terminal (ou invite de commandes) dans le dossier du projet et exécutez :

    ```bash
    python bibliofilm.py
    ```

3.  **Premier démarrage** :
    Si le fichier `films.json` n'existe pas, l'application se lancera avec une liste vide (ou vous pouvez utiliser le fichier JSON d'exemple films.json).

## 📖 Guide d'utilisation

### 1. Ajouter un film
Cliquez sur le bouton **Ajouter**, renseignez le titre et l'année de sortie, puis validez. Le film s'ajoute avec l'état "Non vu" (⭕).

### 2. Noter un film / Marquer comme vu
Sélectionnez un film et cliquez sur le bouton **Noter/Avis**.

Une fenêtre s'ouvrira pour entrer votre note (1-5) et rédiger votre avis. L'icône passera alors à ✅.

### 3. Lire un avis
Cliquez simplement sur un film dans la liste. Les détails (Note + Avis complet) s'afficheront dans la zone en bas de la fenêtre.

### 4. Supprimer
Sélectionnez un film et cliquez sur **Supprimer**. Une confirmation vous sera demandée.

## 📚 Sources

* **Aide au code, tutoriel, questions, rédaction du readme** : Google Gemini

## 📂 Structure des données (films.json)

Les données sont stockées au format JSON standard. Vous pouvez modifier ce fichier manuellement ou le partager.

**Exemple de structure :**

```json
[
  {
    "titre": "Inception",
    "annee": "2010",
    "vu": true,
    "note": 5,
    "avis": "Un chef-d'œuvre absolu..."
  },
  {
    "titre": "Mickey 17",
    "annee": "2025",
    "vu": false,
    "note": null,
    "avis": ""
  }
]
