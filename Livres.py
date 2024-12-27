import json

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
    {"titre": "Catcher in the Rye", "auteur": "J.D. Salinger", "genre": "Roman", "date_publication": 1951},
    {"titre": "Brave New World", "auteur": "Aldous Huxley", "genre": "Dystopie", "date_publication": 1932},
    {"titre": "Les Mots", "auteur": "Jean-Paul Sartre", "genre": "Autobiographie", "date_publication": 1964},
    {"titre": "Voyage au centre de la Terre", "auteur": "Jules Verne", "genre": "Aventure", "date_publication": 1864},
    {"titre": "Vingt mille lieues sous les mers", "auteur": "Jules Verne", "genre": "Science-fiction", "date_publication": 1870},
    {"titre": "L'Odyssee", "auteur": "Homere", "genre": "Epopee", "date_publication": "VIIIe siecle av. J.-C."},
    {"titre": "Crime et Chatiment", "auteur": "Fiodor Dostoievski", "genre": "Roman", "date_publication": 1866},
    {"titre": "La Divine Comedie", "auteur": "Dante Alighieri", "genre": "Poesie", "date_publication": 1320},
    {"titre": "Les Souffrances du jeune Werther", "auteur": "Johann Wolfgang von Goethe", "genre": "Romantisme", "date_publication": 1774},
    {"titre": "Les Evangiles", "auteur": "Anonyme", "genre": "Religieux", "date_publication": "Ier siecle"},
    {"titre": "Le Livre de la jungle", "auteur": "Rudyard Kipling", "genre": "Conte", "date_publication": 1894},
    {"titre": "La Guerre des mondes", "auteur": "H.G. Wells", "genre": "Science-fiction", "date_publication": 1898},
    {"titre": "Les Hauts de Hurlevent", "auteur": "Emily Bronte", "genre": "Roman", "date_publication": 1847},
    {"titre": "L'Insoutenable legerete de l'etre", "auteur": "Milan Kundera", "genre": "Roman", "date_publication": 1984},
    {"titre": "La Nausee", "auteur": "Jean-Paul Sartre", "genre": "Philosophique", "date_publication": 1938},
    {"titre": "Le Paradoxe du chien", "auteur": "David Foster Wallace", "genre": "Essai", "date_publication": 1997},
    {"titre": "Le Nom de la rose", "auteur": "Umberto Eco", "genre": "Policier", "date_publication": 1980},
    {"titre": "Hunger Games", "auteur": "Suzanne Collins", "genre": "Dystopie", "date_publication": 2008},
    {"titre": "Les Miserables", "auteur": "Victor Hugo", "genre": "Roman historique", "date_publication": 1862},
    {"titre": "La Condition humaine", "auteur": "Andre Malraux", "genre": "Roman", "date_publication": 1933},
]
def sauvegarder_livres():
    with open("Livres.json", "w") as file:
        json.dump(livres, file)

def charger_livres() :
    global livres
    try :
        with open("livres.json", "r") as file :
            livres = json.load(file)
    except FileNotFoundError:
        livres = []


def ajouter_livre() :
    
    Titre = input("Entrez le titre du livre : ")
    Auteur = input("Entrez l'auteur du livre : ")
    Genre = input("Entrez le genre du livre : ")
    Date = input("Entrez la date de publication du livre : ")
    Livre = {"titre": Titre, "auteur": Auteur, "genre": Genre, "date_publication": Date}
    livres.append(Livre)
    sauvegarder_livres()
    for i in range(len(livres)) :
        if livres[i]["titre"] == Titre :
            print("Le livre est déjà dans la bibliothèque !")
            break
        else :
            print(f"Le livre {Titre} a été ajouté à la bibliothèque.")
            break

def afficher_livres() :
    
    print("Voici la liste des livres disponibles :")
    print("")
    for i in range(len(livres)) :
        print(f"Titre : {livres[i]['titre']}")
        print(f"Auteur : {livres[i]['auteur']}")
        print(f"Genre : {livres[i]["genre"]}")
        print(f"Date de publication : {livres[i]["date_publication"]}")
        print("")
        
        sauvegarder_livres()

def modifier_livre() :
    
    Titre = input("Entrez le titre du livre à modifier : ")
    for i in range(len(livres)) :
        if livres[i]["titre"] == Titre :
            print("Les informations acctuelles du livre sont :")
            print(f"Titre : {livres[i]['titre']}")
            print(f"Auteur : {livres[i]['auteur']}")
            print(f"Genre : {livres[i]["genre"]}")
            print(f"Date de publication : {livres[i]["date_publication"]}")
            print("")
            print("Quelle information voulez-vous modifier ?")
            print("1. Titre")
            print("2. Auteur")
            print("3. Genre")
            print("4. Date de Publication")
            print("")
            choix = input("Entrez le numéro de votre choix : ")
            if choix == "1" :
                Titre = input("Entrez le nouveau titre du livre : ")
                livres[i]['titre'] = Titre
                print("Le titre du livre à été modifier.")
                sauvegarder_livres()
            elif choix == "2" :
                Auteur = input("Entrez le nouveau  auteur du livre : ")
                livres[i]["auteur"] = Auteur
                print("L'auteur du livre à été modifier.")
                sauvegarder_livres()
            elif choix == "3" :
                Genre = input("Entrez le nouveau genre du livre : ")
                livres[i]["genre"] = Genre
                print("Le genre du livre à été modifier.")
                sauvegarder_livres()
            elif choix == "4" :
                Date = input("Entrez la nouvelle date de publication de livre : ")
                livres[i]["date_publication"] = Date
                print("La date de publication du livre à été modifier.")
                sauvegarder_livres()
            else :
                print("Choix invalide !")
            break

def supprimer_livre() :

    Titre = input("Entrez le titre du livre à supprimer : ")
    for i in range(len(livres)) :
        if livres[i]["titre"] == Titre :
            livres.pop(i)
            print("Le livre à été supprimé.")
            sauvegarder_livres()
            break

def rechercher_livre() :

    Titre = input("Entrez le titre du livre à rechercher : ")
    for i in range(len(livres)) :
        if livres[i]["titre"] == Titre :

            print(f"Titre : {livres[i]["titre"]}")
            print(f"Auteur : {livres[i]["auteur"]}")
            print(f"Genre : {livres[i]["genre"]}")
            print(f"Date de publication : {livres[i]["date_publication"]}")
            print("")
            break
        else :
            print("Le livre n'est pas dans la bibliothéque.")
            break

def menu() :

    while True :
        print("\n Bienvenu dans la bibliothéque !")
        print("\n voici Les différentes options :")
        print("")
        print("1. Ajouter un livre")
        print("2. Afficher les livres")
        print("3. Modifier un livre")
        print("4. Supprimer un livre")
        print("5. Rechercher un livre")
        print("6. Quitter")
        print("")
        choix = input("Entrez le numéro de votre choix : ")
        if choix == "1" :
            ajouter_livre()
        elif choix == "2" :
            afficher_livres()
        elif choix == "3" :
            modifier_livre()
        elif choix == "4" :
            supprimer_livre()
        elif choix == "5" :
            rechercher_livre()
        elif choix == "6" :
            print("Merci d'avoir utilisé la bibliothéque !")
            exit()
        else :
            print("Choix invalide !")
            menu()

if __name__ == "__main__" :

    charger_livres()
    menu()



