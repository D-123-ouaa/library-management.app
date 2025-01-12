import customtkinter as ctk
from tkinter import messagebox, simpledialog
import json
import random

livres = [
    {"titre": "1984", "auteur": "George Orwell", "genre": "Dystopie", "date_publication": 1949},
    {"titre": "Le Petit Prince", "auteur": "Antoine de Saint-Exupery", "genre": "Conte", "date_publication": 1943},
    {"titre": "Moby Dick", "auteur": "Herman Melville", "genre": "Aventure", "date_publication": 1851},
    {"titre": "Les Miserables", "auteur": "Victor Hugo", "genre": "Roman historique", "date_publication": 1862},
    {"titre": "Orgueil et Prejuges", "auteur": "Jane Austen", "genre": "Romance", "date_publication": 1813},
    {"titre": "Cien anos de soledad", "auteur": "Gabriel Garcia Marquez", "genre": "Realisme magique", "date_publication": 1967},
    {"titre": "Don Quichotte", "auteur": "Miguel de Cervantes", "genre": "Roman", "date_publication": 1605},
    {"titre": "Le Seigneur des Anneaux", "auteur": "J.R.R. Tolkien", "genre": "Fantasy", "date_publication": 1954},
    {"titre": "L'Alchimiste", "auteur": "Paulo Coelho", "genre": "Philosophique", "date_publication": 1988},
    {"titre": "La Peste", "auteur": "Albert Camus", "genre": "Existentialisme", "date_publication": 1947},
    {"titre": "La Metamorphose", "auteur": "Franz Kafka", "genre": "Existentialisme", "date_publication": 1915},
    {"titre": "Le Comte de Monte-Cristo", "auteur": "Alexandre Dumas", "genre": "Aventure", "date_publication": 1844},
    {"titre": "Anna Karenine", "auteur": "Leon Tolstoi", "genre": "Roman realiste", "date_publication": 1877},
    {"titre": "L'Etranger", "auteur": "Albert Camus", "genre": "Philosophique", "date_publication": 1942},
    {"titre": "Fahrenheit 451", "auteur": "Ray Bradbury", "genre": "Science-fiction", "date_publication": 1953},
    {"titre": "Les Fleurs du mal", "auteur": "Charles Baudelaire", "genre": "Poesie", "date_publication": 1857},
    {"titre": "Le Grand Gatsby", "auteur": "F. Scott Fitzgerald", "genre": "Roman", "date_publication": 1925},
    {"titre": "L'Attrape-coeurs", "auteur": "J.D. Salinger", "genre": "Roman", "date_publication": 1951},
    {"titre": "Dracula", "auteur": "Bram Stoker", "genre": "Horreur", "date_publication": 1897},
    {"titre": "Frankenstein", "auteur": "Mary Shelley", "genre": "Horreur", "date_publication": 1818},
    {"titre": "La Recherche du temps perdu", "auteur": "Marcel Proust", "genre": "Roman", "date_publication": 1913},
    {"titre": "Le Silence de la mer", "auteur": "Vercors", "genre": "Roman", "date_publication": 1942},
    {"titre": "Les Trois Mousquetaires", "auteur": "Alexandre Dumas", "genre": "Aventure", "date_publication": 1844},
    {"titre": "L'Ile au tresor", "auteur": "Robert Louis Stevenson", "genre": "Aventure", "date_publication": 1883},
    {"titre": "Le Vieil Homme et la Mer", "auteur": "Ernest Hemingway", "genre": "Roman", "date_publication": 1952},
    {"titre": "Le Parfum", "auteur": "Patrick Suskind", "genre": "Roman", "date_publication": 1985},
    {"titre": "La Route", "auteur": "Cormac McCarthy", "genre": "Post-apocalyptique", "date_publication": 2006},
    {"titre": "Les Aventuriers du NHL2987", "auteur": "Pierre Raufast", "genre": "Science-fiction", "date_publication": 2003},
    {"titre": "Les Raisins de la colere", "auteur": "John Steinbeck", "genre": "Roman", "date_publication": 1939},
    {"titre": "Catcher in the Rye", "auteur": "J.D. Salinger", "genre": "Roman", "date_publication": 1951}
]
questions_par_livre = {
    "1984": (
        ("Qui est l'auteur de 1984 ?", "George Orwell"),
        ("En quelle annee '1984' a-t-il ete publie ?", 1949),
        ("Quel est le genre de '1984' ?", "Dystopie"),
        ("Quel est le titre de l'oeuvre de George Orwell qui traite de la surveillance totale ?", "1984"),
        ("Dans quel pays se deroule l'histoire de '1984' ?", "Oceania")
    ),
    "Le Petit Prince": (
        ("Qui est l'auteur du Petit Prince ?", "Antoine de Saint-Exupery"),
        ("En quelle annee 'Le Petit Prince' a-t-il ete publie ?", 1943),
        ("Quel est le genre de 'Le Petit Prince' ?", "Conte"),
        ("Quel est le nom de la planete du Petit Prince ?", "B-612"),
        ("Le Petit Prince rencontre un pilote, quel est le metier de celui-ci ?", "Pilote d'avion")
    ),
    "Moby Dick": (
        ("Qui est l'auteur de Moby Dick ?", "Herman Melville"),
        ("Quel est le nom du capitaine dans Moby Dick ?", "Ahab"),
        ("Quel est le genre de Moby Dick ?", "Aventure"),
        ("En quelle annee 'Moby Dick' a-t-il ete publie ?", 1851),
        ("Quel est le nom du baleinier dans 'Moby Dick' ?", "Pequod")
    ),
    "Les Miserables": (
        ("Qui est l'auteur des Miserables ?", "Victor Hugo"),
        ("Quel est le genre de 'Les Miserables' ?", "Roman historique"),
        ("En quelle annee 'Les Miserables' a-t-il ete publie ?", 1862),
        ("Qui est le personnage principal de 'Les Miserables' ?", "Jean Valjean"),
        ("Dans quelle ville se passe une partie de l'histoire de 'Les Miserables' ?", "Paris")
    ),
    "Orgueil et Prejuges": (
        ("Qui est l'auteur de 'Orgueil et Prejuges' ?", "Jane Austen"),
        ("Quel est le genre de 'Orgueil et Prejuges' ?", "Romance"),
        ("En quelle annee 'Orgueil et Prejuges' a-t-il ete publie ?", 1813),
        ("Qui est le personnage principal feminin de 'Orgueil et Prejuges' ?", "Elizabeth Bennet"),
        ("Quel est le prenom du principal pretendant de Elizabeth Bennet ?", "Darcy")
    ),
    "Cien anos de soledad": (
        ("Qui est l'auteur de 'Cien anos de soledad' ?", "Gabriel Garcia Marquez"),
        ("Quel est le genre de 'Cien anos de soledad' ?", "Realisme magique"),
        ("En quelle annee 'Cien anos de soledad' a-t-il ete publie ?", 1967),
        ("Quel est le nom de la ville fictive dans 'Cien anos de soledad' ?", "Macondo"),
        ("Qui est le personnage principal de 'Cien anos de soledad' ?", "Jose Arcadio Buendia")
    ),
    "Don Quichotte": (
        ("Qui est l'auteur de Don Quichotte ?", "Miguel de Cervantes"),
        ("En quelle annee 'Don Quichotte' a-t-il ete publie ?", 1605),
        ("Quel est le genre de 'Don Quichotte' ?", "Roman"),
        ("Quel est le nom du cheval de Don Quichotte ?", "Rocinante"),
        ("Comment s'appelle le fidele ecuyer de Don Quichotte ?", "Sancho Panza")
    ),
    "Le Seigneur des Anneaux": (
        ("Qui est l'auteur du 'Seigneur des Anneaux' ?", "J.R.R. Tolkien"),
        ("Quel est le genre du 'Seigneur des Anneaux' ?", "Fantasy"),
        ("En quelle annee 'Le Seigneur des Anneaux' a-t-il ete publie ?", 1954),
        ("Qui est le porteur de l'anneau dans 'Le Seigneur des Anneaux' ?", "Frodon Sacquet"),
        ("Quel est le nom de la communaute qui accompagne Frodon ?", "La Communaute de l'Anneau")
    ),
    "L'Alchimiste": (
        ("Qui est l'auteur de 'L'Alchimiste' ?", "Paulo Coelho"),
        ("En quelle annee 'L'Alchimiste' a-t-il ete publie ?", 1988),
        ("Quel est le genre de 'L'Alchimiste' ?", "Philosophique"),
        ("Quel est le reve du personnage principal de 'L'Alchimiste' ?", "Trouver un tresor"),
        ("Quel est le nom du protagoniste dans 'L'Alchimiste' ?", "Santiago")
    ),
    "La Peste": (
        ("Qui est l'auteur de 'La Peste' ?", "Albert Camus"),
        ("Quel est le genre de 'La Peste' ?", "Existentialisme"),
        ("En quelle annee 'La Peste' a-t-il ete publie ?", 1947),
        ("Quel est le cadre principal de l'intrigue de 'La Peste' ?", "La ville d'Oran en Algerie"),
        ("Quel est le nom du medecin dans 'La Peste' ?", "Dr. Rieux")
    ),
    "La Metamorphose": (
        ("Qui est l'auteur de 'La Metamorphose' ?", "Franz Kafka"),
        ("En quelle annee 'La Metamorphose' a-t-il ete publie ?", 1915),
        ("Quel est le genre de 'La Metamorphose' ?", "Existentialisme"),
        ("Quel est l'animal dans lequel Gregor Samsa se transforme ?", "Un insecte"),
        ("Quel est le nom de la famille de Gregor Samsa dans 'La Metamorphose' ?", "La famille Samsa")
    ),
    "Le Comte de Monte-Cristo": (
        ("Qui est l'auteur du 'Comte de Monte-Cristo' ?", "Alexandre Dumas"),
        ("En quelle annee 'Le Comte de Monte-Cristo' a-t-il ete publie ?", 1844),
        ("Quel est le genre de 'Le Comte de Monte-Cristo' ?", "Aventure"),
        ("Quel est le vrai nom du protagoniste, le Comte de Monte-Cristo ?", "Edmond Dantes"),
        ("Quel est l'objectif principal d'Edmond Dantes dans 'Le Comte de Monte-Cristo' ?", "Se venger")
    ),
    "Anna Karenine": (
        ("Qui est l'auteur de 'Anna Karenine' ?", "Leon Tolstoi"),
        ("En quelle annee 'Anna Karenine' a-t-il ete publie ?", 1877),
        ("Quel est le genre de 'Anna Karenine' ?", "Roman realiste"),
        ("Quel est le dilemme de l'heroine Anna Karenine ?", "Son amour illegitime pour Vronski"),
        ("Quel est le prenom de l'epoux d'Anna Karenine ?", "Alexis Karenine")
    ),
    "L'Etranger": (
        ("Qui est l'auteur de 'L'Etranger' ?", "Albert Camus"),
        ("Quel est le genre de 'L'Etranger' ?", "Philosophique"),
        ("En quelle annee 'L'Etranger' a-t-il ete publie ?", 1942),
        ("Quel est le prenom du protagoniste de 'L'Etranger' ?", "Meursault"),
        ("Ou Meursault commet-il un meurtre dans 'L'Etranger' ?", "Sur une plage en Algerie")
    ),
    "Fahrenheit 451": (
        ("Qui est l'auteur de 'Fahrenheit 451' ?", "Ray Bradbury"),
        ("En quelle annee 'Fahrenheit 451' a-t-il ete publie ?", 1953),
        ("Quel est le genre de 'Fahrenheit 451' ?", "Science-fiction"),
        ("Quel est le role principal du personnage de Guy Montag ?", "Pompeur de livres"),
        ("Quel est le symbole de la resistance dans 'Fahrenheit 451' ?", "Les livres")
    ),
    "Les Fleurs du mal": (
        ("Qui est l'auteur des 'Fleurs du mal' ?", "Charles Baudelaire"),
        ("En quelle annee 'Les Fleurs du mal' a-t-il ete publie ?", 1857),
        ("Quel est le genre de 'Les Fleurs du mal' ?", "Poesie"),
        ("Quel est le theme principal de 'Les Fleurs du mal' ?", "La beaute et le mal"),
        ("Quel est le nom de la premiere section du recueil 'Les Fleurs du mal' ?", "Spleen et Ideal")
    ),
    "Le Grand Gatsby": (
        ("Qui est l'auteur de 'Le Grand Gatsby' ?", "F. Scott Fitzgerald"),
        ("En quelle annee 'Le Grand Gatsby' a-t-il ete publie ?", 1925),
        ("Quel est le genre de 'Le Grand Gatsby' ?", "Roman"),
        ("Quel est le nom du personnage principal de 'Le Grand Gatsby' ?", "Jay Gatsby"),
        ("Quel est le reve de Jay Gatsby dans 'Le Grand Gatsby' ?", "Revivre son amour avec Daisy")
    ),
    "L'Attrape-coeurs": (
        ("Qui est l'auteur de 'L'Attrape-coeurs' ?", "J.D. Salinger"),
        ("En quelle annee 'L'Attrape-coeurs' a-t-il ete publie ?", 1951),
        ("Quel est le genre de 'L'Attrape-coeurs' ?", "Roman"),
        ("Quel est le prenom du protagoniste de 'L'Attrape-coeurs' ?", "Holden Caulfield"),
        ("Pourquoi Holden Caulfield est-il un personnage solitaire ?", "Il se sent aliene de la societe")
    ),
    "Dracula": (
        ("Qui est l'auteur de 'Dracula' ?", "Bram Stoker"),
        ("En quelle annee 'Dracula' a-t-il ete publie ?", 1897),
        ("Quel est le genre de 'Dracula' ?", "Horreur"),
        ("Quel est le nom du comte dans 'Dracula' ?", "Comte Dracula"),
        ("Dans quel pays le Comte Dracula est-il originaire ?", "Transylvanie")
    ),
    "Frankenstein": (
        ("Qui est l'auteur de 'Frankenstein' ?", "Mary Shelley"),
        ("En quelle annee 'Frankenstein' a-t-il ete publie ?", 1818),
        ("Quel est le genre de 'Frankenstein' ?", "Horreur"),
        ("Qui est le createur de la creature dans 'Frankenstein' ?", "Victor Frankenstein"),
        ("Quel est le theme principal de 'Frankenstein' ?", "Les dangers de la science")
    ),
    "La Recherche du temps perdu": (
        ("Qui est l'auteur de 'La Recherche du temps perdu' ?", "Marcel Proust"),
        ("En quelle annee 'La Recherche du temps perdu' a-t-il ete publie ?", 1913),
        ("Quel est le genre de 'La Recherche du temps perdu' ?", "Roman"),
        ("Quel est le nom du narrateur de 'La Recherche du temps perdu' ?", "Le narrateur n'a pas de nom specifique"),
        ("Quel est l'objet symbolique cle dans 'La Recherche du temps perdu' ?", "La madeleine")
    ),
    "Le Silence de la mer": (
        ("Qui est l'auteur de 'Le Silence de la mer' ?", "Vercors"),
        ("En quelle annee 'Le Silence de la mer' a-t-il ete publie ?", 1942),
        ("Quel est le genre de 'Le Silence de la mer' ?", "Roman"),
        ("Quel est le theme principal de 'Le Silence de la mer' ?", "La resistance pendant la Seconde Guerre mondiale"),
        ("Dans quel contexte historique se deroule 'Le Silence de la mer' ?", "Pendant l'Occupation nazie en France")
    ),
    "Les Trois Mousquetaires": (
        ("Qui est l'auteur des 'Trois Mousquetaires' ?", "Alexandre Dumas"),
        ("En quelle annee 'Les Trois Mousquetaires' a-t-il ete publie ?", 1844),
        ("Quel est le genre de 'Les Trois Mousquetaires' ?", "Aventure"),
        ("Quels sont les noms des trois mousquetaires ?", "Athos, Porthos, Aramis"),
        ("Quel est le prenom du personnage principal des 'Trois Mousquetaires' ?", "D'Artagnan")
    ),
    "L'Ile au tresor": (
        ("Qui est l'auteur de 'L'Ile au tresor' ?", "Robert Louis Stevenson"),
        ("En quelle annee 'L'Ile au tresor' a-t-il ete publie ?", 1883),
        ("Quel est le genre de 'L'Ile au tresor' ?", "Aventure"),
        ("Quel est le nom du pirate principal dans 'L'Ile au tresor' ?", "Long John Silver"),
        ("Quel est le tresor recherche dans 'L'Ile au tresor' ?", "Un tresor cache sur une ile")
    ),
    "Le Vieil Homme et la Mer": (
        ("Qui est l'auteur de 'Le Vieil Homme et la Mer' ?", "Ernest Hemingway"),
        ("En quelle annee 'Le Vieil Homme et la Mer' a-t-il ete publie ?", 1952),
        ("Quel est le genre de 'Le Vieil Homme et la Mer' ?", "Roman"),
        ("Quel est le nom du vieil homme dans 'Le Vieil Homme et la Mer' ?", "Santiago"),
        ("Que peche le vieil homme dans 'Le Vieil Homme et la Mer' ?", "Un marlin geant")
    ),
    "Le Parfum": (
        ("Qui est l'auteur de 'Le Parfum' ?", "Patrick Suskind"),
        ("En quelle annee 'Le Parfum' a-t-il ete publie ?", 1985),
        ("Quel est le genre de 'Le Parfum' ?", "Roman"),
        ("Quel est le prenom du personnage principal dans 'Le Parfum' ?", "Jean-Baptiste Grenouille"),
        ("Quel est le talent particulier de Grenouille dans 'Le Parfum' ?", "Il a un odorat extremement developpe")
    ),
    "La Route": (
        ("Qui est l'auteur de 'La Route' ?", "Cormac McCarthy"),
        ("En quelle annee 'La Route' a-t-il ete publie ?", 2006),
        ("Quel est le genre de 'La Route' ?", "Post-apocalyptique"),
        ("Dans quel contexte se deroule 'La Route' ?", "Un monde post-apocalyptique"),
        ("Qui sont les deux personnages principaux dans 'La Route' ?", "Le pere et le fils")
    ),
    "Les Aventuriers du NHL2987": (
        ("Qui est l'auteur de 'Les Aventuriers du NHL2987' ?", "Pierre Raufast"),
        ("En quelle annee 'Les Aventuriers du NHL2987' a-t-il ete publie ?", 2003),
        ("Quel est le genre de 'Les Aventuriers du NHL2987' ?", "Science-fiction"),
        ("Quel est le nom du personnage principal de 'Les Aventuriers du NHL2987' ?", "Tomek"),
        ("Quel est l'objectif principal des aventuriers dans 'Les Aventuriers du NHL2987' ?", "Explorer l'univers")
    ),
    "Les Raisins de la colere": (
        ("Qui est l'auteur des 'Raisins de la colere' ?", "John Steinbeck"),
        ("En quelle annee 'Les Raisins de la colere' a-t-il ete publie ?", 1939),
        ("Quel est le genre de 'Les Raisins de la colere' ?", "Roman"),
        ("Quel est le theme principal des 'Les Raisins de la colere' ?", "La Grande Depression aux Etats-Unis"),
        ("Qui sont les personnages principaux des 'Les Raisins de la colere' ?", "Les Joad")
    ),
    "Catcher in the Rye": (
        ("Qui est l'auteur de 'Catcher in the Rye' ?", "J.D. Salinger"),
        ("En quelle annee 'Catcher in the Rye' a-t-il ete publie ?", 1951),
        ("Quel est le genre de 'Catcher in the Rye' ?", "Roman"),
        ("Quel est le prenom du personnage principal de 'Catcher in the Rye' ?", "Holden Caulfield"),
        ("Quel est le sujet de la rebellion de Holden Caulfield ?", "Son rejet des normes sociales")
    )
}
def sauvegarder_livres():
    with open("Livres.json", "w") as file:
        json.dump(livres, file,indent=4)

def charger_livres():
    global livres
    try:
        with open("Livres.json", "r") as file:
            livres = json.load(file)
    except FileNotFoundError:
        livres = []

def ajouter_livre():
    def sauvegarder():
        titre = entry_titre.get()
        auteur = entry_auteur.get()
        genre = entry_genre.get()
        date = entry_date.get()

        if titre and auteur and genre and date:
            livres.append({"titre": titre, "auteur": auteur, "genre": genre, "date_publication": date})
            sauvegarder_livres()
            messagebox.showinfo("Succès", f"Le livre '{titre}' a été ajouté.")
            popup.destroy()
        else:
            messagebox.showwarning("Attention", "Tous les champs doivent être remplis.")
    
    popup = ctk.CTkToplevel(root)
    popup.title("Ajouter un livre")
    popup.geometry("400x300")

    ctk.CTkLabel(popup, text="Titre").pack(pady=5)
    entry_titre = ctk.CTkEntry(popup, width=300)
    entry_titre.pack(pady=5)

    ctk.CTkLabel(popup, text="Auteur").pack(pady=5)
    entry_auteur = ctk.CTkEntry(popup, width=300)
    entry_auteur.pack(pady=5)

    ctk.CTkLabel(popup, text="Genre").pack(pady=5)
    entry_genre = ctk.CTkEntry(popup, width=300)
    entry_genre.pack(pady=5)

    ctk.CTkLabel(popup, text="Date de Publication").pack(pady=5)
    entry_date = ctk.CTkEntry(popup, width=300)
    entry_date.pack(pady=5)

    ctk.CTkButton(popup, text="Ajouter", command=sauvegarder).pack(pady=20)

def afficher_livres():
    if not livres:
        messagebox.showinfo("Info", "Aucun livre disponible.")
        return

    popup = ctk.CTkToplevel(root)
    popup.title("Liste des livres")
    popup.geometry("600x400")

    for livre in livres:
        ctk.CTkLabel(
            popup,
            text=f"Titre: {livre['titre']} \nAuteur: {livre['auteur']} \nGenre: {livre['genre']} \nDate: {livre['date_publication']}",
            anchor="w"
        ).pack(pady=2, fill="x")

def rechercher_livre():
    def rechercher():
        titre = entry_recherche.get()
        for livre in livres:
            if livre["titre"].lower() == titre.lower():
                messagebox.showinfo("Livre trouvé", f"Titre: {livre['titre']}\nAuteur: {livre['auteur']}\nGenre: {livre['genre']}\nDate: {livre['date_publication']}")
                popup.destroy()
                return
        messagebox.showwarning("Non trouvé", f"Aucun livre trouvé avec le titre '{titre}'.")
    
    popup = ctk.CTkToplevel(root)
    popup.title("Rechercher un livre")
    popup.geometry("400x200")

    ctk.CTkLabel(popup, text="Entrez le titre").pack(pady=10)
    entry_recherche = ctk.CTkEntry(popup, width=300)
    entry_recherche.pack(pady=5)

    ctk.CTkButton(popup, text="Rechercher", command=rechercher).pack(pady=20)

def supprimer_livre():
    def supprimer():
        titre = entry_supprimer.get()
        for livre in livres:
            if livre["titre"].lower() == titre.lower():
                livres.remove(livre)
                sauvegarder_livres()
                messagebox.showinfo("Succès", f"Le livre '{titre}' a été supprimé.")
                popup.destroy()
                return
        messagebox.showwarning("Non trouvé", f"Aucun livre trouvé avec le titre '{titre}'.")
    
    popup = ctk.CTkToplevel(root)
    popup.title("Supprimer un livre")
    popup.geometry("400x200")

    ctk.CTkLabel(popup, text="Entrez le titre").pack(pady=10)
    entry_supprimer = ctk.CTkEntry(popup, width=300)
    entry_supprimer.pack(pady=5)

    ctk.CTkButton(popup, text="Supprimer", command=supprimer).pack(pady=20)

def poser_questions(livre_titre):
    score = 0
    questions = list(questions_par_livre[livre_titre])
    random.shuffle(questions)

    for question, reponse_attendue in questions:
        reponse = simpledialog.askstring("Question", question)
        if reponse is None:  # Si l'utilisateur annule
            messagebox.showwarning("Quiz annulé", "Vous avez annulé le quiz.")
            return
        if reponse.strip().lower() == str(reponse_attendue).strip().lower():
            score += 1
            messagebox.showinfo("Bonne réponse", "Bonne réponse !")
        else:
            messagebox.showwarning("Mauvaise réponse", f"Mauvaise réponse. La bonne réponse était : {reponse_attendue}")
    
    messagebox.showinfo("Résultat", f"Votre score pour '{livre_titre}': {score} / {len(questions)}")

def afficher_quiz():
    quiz_fenetre = ctk.CTkToplevel()
    quiz_fenetre.title("Quiz")
    quiz_fenetre.geometry("400x300")

    def lancer_quiz():
        livre_choisi = livre_menu.get()
        if livre_choisi in questions_par_livre:
            poser_questions(livre_choisi)
        else:
            messagebox.showwarning("Erreur", "Veuillez choisir un livre valide.")

    ctk.CTkLabel(quiz_fenetre, text="Choisissez un livre :").pack(pady=10)
    livre_menu = ctk.CTkComboBox(quiz_fenetre, values=list(questions_par_livre.keys()))
    livre_menu.pack(pady=10)

    ctk.CTkButton(quiz_fenetre, text="Commencer le quiz", command=lancer_quiz).pack(pady=20)


ctk.set_appearance_mode("Light") 
ctk.set_default_color_theme("blue")  

root = ctk.CTk()
root.title("Gestion De Bibliothéque")
root.geometry("500x400")

ctk.CTkLabel(root, text="Gestion Des Livres", font=("Helvetica", 20)).pack(pady=20)

ctk.CTkButton(root, text="Ajouter un livre", command=ajouter_livre, width=200).pack(pady=10)
ctk.CTkButton(root, text="Afficher les livres", command=afficher_livres, width=200).pack(pady=10)
ctk.CTkButton(root, text="Rechercher un livre", command=rechercher_livre, width=200).pack(pady=10)
ctk.CTkButton(root, text="Supprimer un livre", command=supprimer_livre, width=200).pack(pady=10)
ctk.CTkButton(root, text="Passer au quiz", command=afficher_quiz, width=200).pack(pady=10)

ctk.CTkButton(root, text="Quitter", command=root.quit, width=200).pack(pady=20)

root.mainloop()
