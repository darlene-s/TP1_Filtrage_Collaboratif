import math

# Dico personnes / critiques (Questions 1 a 4)
critiques = {
    "Lisa Rose": {"Lady": 2.5, "Snakes": 3.5, "Luck": 3.0, "Superman": 3.5, "Dupree": 2.5, "Night": 3.0},
    "Gene Seymour": {"Lady": 3.0, "Snakes": 3.5, "Luck": 1.5, "Superman": 5.0, "Dupree": 3.5, "Night": 3.0},
    "Michael Phillips": {"Lady": 2.5, "Snakes": 3.0, "Superman": 3.5, "Night": 4.0},
    "Claudia Puig": {"Snakes": 3.5, "Luck": 3.0, "Superman": 4.0, "Dupree": 2.5, "Night": 4.5},
    "Mick Lasalle": {"Lady": 3.0, "Snakes": 4.0, "Luck": 2.0, "Superman": 3.0, "Dupree": 2.0, "Night": 3.0},
    "Jack Matthews": {"Lady": 3.0, "Snakes": 4.0, "Superman": 5.0, "Dupree": 3.5, "Night": 3.0},
    "Toby": {"Snakes": 4.5, "Superman": 4.0, "Dupree": 1.0},
    "Anne": {"Lady": 1.5, "Luck": 4.0, "Dupree": 2.0},
}


def taux_cellules_vides(critiques):
    # Étape 1 : Calculer le nombre total de films dans le dictionnaire
    films = set()  # Crée un ensemble vide pour stocker les films uniques
    for personne in critiques:
        films.update(critiques[personne])  # Ajoute les films de chaque personne à l'ensemble

    nombre_total_films = len(films)  # Obtient le nombre total de films uniques

    # Étape 2 : Calculer le nombre total de personnes dans le dictionnaire
    nombre_total_personnes = len(critiques)  # Obtient le nombre total de personnes dans les critiques

    # Étape 3 : Calculer le nombre total de notes attendues
    total_valeurs_attendues = nombre_total_films * nombre_total_personnes
    # Chaque personne devrait fournir une note pour chaque film unique, donc c'est le produit des deux.

    # Étape 4 : Calculer le nombre total de notes effectives
    valeurs_effectives = sum(len(critiques[personne]) for personne in critiques)
    # Pour chaque personne, on compte combien de notes elle a données, puis on les additionne pour toutes les personnes.

    # Étape 5 : Calculer le taux de cellules vides en pourcentage
    taux = ((total_valeurs_attendues - valeurs_effectives) / total_valeurs_attendues) * 100
    # Le taux de cellules vides est la différence entre le nombre total de notes attendues et le nombres de notes effectif, divisée par le nombre de notes attendues,
    # puis multipliée par 100 pour obtenir un pourcentage.

    return taux  # Retourne le taux de cellules vides en pourcentage

def sim_distanceManhattan(person1, person2):
    # Étape 1 : Trouver les films communs (vus par les deux personnes) entre person1 et person2
    common_movies = [movie for movie in person1 if movie in person2]
    
    # Si aucune critique commune n'est trouvée, retourne 0 (distance minimale)
    if len(common_movies) == 0:
        return 0
    
    # Étape 2 : Calculer la distance de Manhattan entre les deux personnes pour les films communs
    manhattan_distance = sum(abs(person1[movie] - person2[movie]) for movie in common_movies)
    # Pour chaque film commun, calcule la valeur absolue de la différence entre les critiques de person1 et person2,
    # puis somme ces différences pour tous les films communs.

    return manhattan_distance  # Retourne la distance de Manhattan entre les deux personnes


def sim_distanceEuclidienne(person1, person2):
    # Étape 1 : Trouver les films communs (vus par les deux personnes) entre person1 et person2
    common_movies = [movie for movie in person1 if movie in person2]
    
    # Si aucune critique commune n'est trouvée, retourne 0 (distance minimale)
    if len(common_movies) == 0:
        return 0
    
    # Étape 2 : Calculer la distance euclidienne entre les deux personnes pour les films communs
    euclidean_distance = math.sqrt(sum((person1[movie] - person2[movie])**2 for movie in common_movies))
    # Pour chaque film commun, calcule le carré de la différence entre les critiques de person1 et person2,
    # puis additionne ces carrés pour tous les films communs. Ensuite, prend la racine carrée du résultat.

    return euclidean_distance  # Retourne la distance euclidienne entre les deux personnes

# Fonction ppv
def computeNearestNeighbor(person, Critiques):
    # Étape 1 : Vérifier si la personne existe dans le dictionnaire des critiques
    if person not in Critiques:
        return f"La personne '{person}' n'existe pas dans le dictionnaire des critiques"

    # Étape 2 : Créer une liste pour stocker les distances entre la personne et les autres personnes
    distances = []

    # Étape 3 : Parcourir toutes les personnes dans le dictionnaire des critiques
    for critique in Critiques:
        # Étape 4 : Exclut le cas où la personne se compare à elle-même 
        if critique != person:
            # Étape 5 :Calculer la distance de Manhattan entre la personne et la personne actuellement examinée
            distance = sim_distanceManhattan(Critiques[critique], Critiques[person])
            
            # Étape 6 : Ajouter la paire (distance, nom de la personne) à la liste des distances
            distances.append((distance, critique))

     # Étape 7 : Trier la liste des distances par ordre croissant de distance
    distances.sort()

    # Étape 8 : Retourner la liste triée des distances, ce qui donne les personnes les plus proches en premier
    return distances


def recommend(person, Critiques):
    # Etape 1 : Vérifier si la personne existe dans le dictionnaire des critiques
    if person not in Critiques:
        return f"La personne '{person}' n'existe pas dans le dictionnaire des critiques"

    # Etape 2 : Utiliser la fonction computeNearestNeighbor pour obtenir la critique la plus proche
    nearest_neighbor = computeNearestNeighbor(person, Critiques)[0]  # Prend la première critique la plus proche

    recommendations = []

    # Etape 3 : Parcourir les films et notes de la critique la plus proche
    for movie, rating in Critiques[nearest_neighbor[1]].items():
        # Etape 4 : Vérifier si le film n'a pas encore été noté par la personne choisie
        if movie not in Critiques[person]:
            recommendations.append((movie, rating))

    if recommendations:
        # Etape 5 : S'il y a des recommandations, les afficher avec le nom de la personne
        return f"Recommandations pour {person} : {recommendations}"
    else:
        # Etape 6 : Si aucune recommandation n'est disponible, indiquer qu'il n'y a pas de recommandations
        return []


def calculate_s_prime(a, personne, Critiques):
    # Étape 1 : Vérifier si la personne est une clé du dictionnaire
    if personne not in Critiques:
        return f"La personne '{personne}' n'existe pas dans le dictionnaire des critiques", [], None, None

    # Étape 2 : Obtient la liste des films disponibles dans le dictionnaire
    available_movies = set()
    for critique in Critiques:
        available_movies.update(Critiques[critique].keys())

    # Étape 3 : Vérifier si le film choisi appartient à la liste des films disponibles
    if a not in available_movies:
        return f"Le film '{a}' n'existe pas dans la liste des films disponibles", list(available_movies), None, None

    # Étape 4 : Vérifier si la personne a vu le film choisi en parametres
    if a in Critiques[personne]:
        message = f"Le film '{a}' a déjà été vu par '{personne}'"
        return message, [], None, None

    # Étape 5 : Liste des critiques ayant attribué une note au film choisi mais n'ayant pas encore vu le film choisi
    C_a = [critique for critique in Critiques if a in Critiques[critique] and a not in Critiques[personne]]

    # Initialiser des variables pour le calcul de s prime pour le film choisi
    total_a = 0
    s_a = 0

    # Étape 6 : Calcul de s prime pour le film choisi
    for critique in C_a:
        # Calcul de la similarité entre la personne actuelle et la critique de l'autre personne choisie selon Manhattan (peut etre modifie en choissant euclidienne)
        
        distance = 1 / (1 + sim_distanceManhattan(Critiques[critique], Critiques[personne]))
            
        # Ajout pondéré de la note du film choisi à total_a
        total_a += distance * Critiques[critique][a]
        
        # Accumulation des distances pour le calcul de s_a
        s_a += distance

    # Éviter une division par zéro
    if s_a == 0:
        return "s(a) = 0", C_a, s_a, total_a

    # Calcul de s prime pour le film choisi en utilisant les valeurs calculées précédemment
    s_prime_a = total_a / s_a

    # Retourne s prime pour le film choisi ainsi que d'autres informations utiles
    return s_prime_a, C_a, s_a, total_a


def bestRecommend(personne, Critiques):
    # Étape 1 : Vérifier si la personne est une clé du dictionnaire
    if personne not in Critiques:
        return f"La personne '{personne}' n'existe pas dans le dictionnaire des critiques"

    # Étape 2 : Obtient la liste des films disponibles dans le dictionnaire
    available_movies = set()
    for critique in Critiques:
        available_movies.update(Critiques[critique].keys())

    # Étape 3 : Liste des films non vus par la personne
    unwatched_movies = [movie for movie in available_movies if movie not in Critiques[personne]]

    # Étape 4 : Vérifier si la personne a vu tous les films disponibles
    if not unwatched_movies:
        return f"{personne} a vu tous les films disponibles."

    # Étape 5 : Initialisation des variables pour le meilleur film et la meilleure estimation de note
    best_movie = None
    best_s_prime = None

    # Étape 6 : Parcourir les films non vus par la personne
    for movie in unwatched_movies:
        # Calculer s_prime_a pour le film en cours
        result = calculate_s_prime(movie, personne, Critiques)
        
        # Ignorer les erreurs (cas où calculate_s_prime renvoie une chaîne de caractères)
        if isinstance(result, str):
            continue

        s_prime_a = result[0]
        
        # Mettre à jour le meilleur film et la meilleure estimation de note
        if best_movie is None or s_prime_a > best_s_prime:
            best_movie = movie
            best_s_prime = s_prime_a

    # Étape 7 : Si aucun film recommandable n'est trouvé, retourner un message approprié
    if best_movie is None:
        return []
    
    # Étape 8 : Retourner la meilleure recommandation et sa note associee
    return [best_movie, best_s_prime]


def calculate_s_seconde(a, personne, Critiques):
    # Étape 1 : Vérifier si la personne est une clé du dictionnaire
    if personne not in Critiques:
        return f"La personne '{personne}' n'existe pas dans le dictionnaire des critiques", [], None, None

    # Étape 2 : Obtient la liste des films disponibles dans le dictionnaire
    available_movies = set()
    for critique in Critiques:
        available_movies.update(Critiques[critique].keys())

    # Étape 3 : Vérifier si le film 'a' appartient à la liste des films disponibles
    if a not in available_movies:
        return f"Le film '{a}' n'existe pas dans la liste des films disponibles", list(available_movies), None, None

    # Étape 4 : Vérifier si la personne a vu le film 'a'
    if a in Critiques[personne]:
        message = f"Le film '{a}' a déjà été vu par '{personne}'"
        return message, [], None, None

    # Étape 5 : Liste des critiques ayant attribué une note au film 'a' mais n'ayant pas encore vu le film 'a'
    C_a = [critique for critique in Critiques if a in Critiques[critique] and a not in Critiques[personne]]

    # Initialiser des variables pour le calcul de s_seconde_a
    total_a = 0
    s_a = 0

    # Étape 6 : Calcul de s_seconde_a
    for critique in C_a:
        # Calcul de la distance modifiée (1 + distance de Manhattan) entre la personne et la critique en cours
        distance = (1 + sim_distanceManhattan(Critiques[critique], Critiques[personne]))
        
        # Ajout pondéré de la note du film 'a' à total_a
        total_a += distance * Critiques[critique][a]
        
        # Accumulation des distances modifiées pour le calcul de s_a
        s_a += distance

    # Étape 7 : Éviter une division par zéro
    if s_a == 0:
        return "s(a) = 0", C_a, s_a, total_a

    # Étape 8 : Calcul de s_seconde_a en utilisant les valeurs calculées précédemment
    s_seconde_a = total_a / s_a

    # Étape 9 : Retourner s_seconde_a ainsi que d'autres informations utiles
    return s_seconde_a, C_a, s_a, total_a


def otherBestRecommend(personne, Critiques):
    # Étape 1 : Vérifier si la personne est une clé du dictionnaire
    if personne not in Critiques:
        return f"La personne '{personne}' n'existe pas dans le dictionnaire des critiques"

    # Étape 2 : Obtient la liste des films disponibles dans le dictionnaire
    available_movies = set()
    for critique in Critiques:
        available_movies.update(Critiques[critique].keys())

    # Étape 3 : Liste des films non vus par la personne
    unwatched_movies = [movie for movie in available_movies if movie not in Critiques[personne]]

    # Étape 4 : Vérifier si la personne a vu tous les films disponibles
    if not unwatched_movies:
        return f"{personne} a vu tous les films disponibles."

    # Étape 5 : Initialisation des variables pour le meilleur film et la meilleure estimation de note (s_seconde)
    best_movie = None
    best_s_seconde = None

    # Étape 6 : Parcourir les films non vus par la personne
    for movie in unwatched_movies:
        # Calculer s_seconde_a pour le film en cours
        result = calculate_s_seconde(movie, personne, Critiques)
        
        # Ignorer les erreurs (cas où calculate_s_seconde renvoie une chaîne de caractères)
        if isinstance(result, str):
            continue

        s_seconde_a = result[0]
        
        # Mettre à jour le meilleur film et la meilleure estimation de note (s_seconde)
        if best_movie is None or s_seconde_a > best_s_seconde:
            best_movie = movie
            best_s_seconde = s_seconde_a

    # Étape 7 : Si aucun film recommandable n'est trouvé, retourner un message approprié
    if best_movie is None:
        return []

    # Étape 8 : Retourner le meilleur film recommandé et sa meilleure estimation de note (s_seconde)
    return [best_movie, best_s_seconde]


def pearson(person1, person2):
    
    #print("\nPEARSON\n")
    
    #print("person1 = ", person1)
    #print("person2 = ", person2)
    
    # Initialisation des variables de calcul
    sum_xy = 0  # Somme des produits des critiques
    sum_x = 0   # Somme des critiques de la première personne
    sum_y = 0   # Somme des critiques de la deuxième personne
    sum_x2 = 0  # Somme des carrés des critiques de la première personne
    sum_y2 = 0  # Somme des carrés des critiques de la deuxième personne
    n = 0       # Nombre de critiques communes entre les deux personnes

    # Parcourir les critiques de la première personne
    for key in person1:
        if key in person2:
            n += 1  # Incrémenter le nombre de critiques communes
            x = person1[key]
            y = person2[key]
            sum_xy += x * y     # Somme des produits des critiques
            sum_x += x         # Somme des critiques de la première personne
            sum_y += y         # Somme des critiques de la deuxième personne
            sum_x2 += x ** 2   # Somme des carrés des critiques de la première personne
            sum_y2 += y ** 2   # Somme des carrés des critiques de la deuxième personne
            
    #Si person1 et person2 n'ont pas vu de films en commun --> évite la division par 0       
    if (n==0):
        return 0
    
    # Calcul du dénominateur de la formule de Pearson
    denominator = math.sqrt(sum_x2 - (sum_x ** 2) / n) * math.sqrt(sum_y2 - (sum_y ** 2) / n)
    
    # Éviter une division par zéro si dénominateur nul
    if denominator == 0:
        return 0
    else:
        # Calcul du coefficient de Pearson
        #print("PEARSON = " , (sum_xy - (sum_x * sum_y) / n) / denominator)
        return (sum_xy - (sum_x * sum_y) / n) / denominator

#Recommandation pearson
def pearson_recommend(personne, critiques):
    # Étape 1 : Vérifier si la personne est une clé du dictionnaire
    if personne not in critiques:
        return f"La personne '{personne}' n'existe pas dans le dictionnaire des critiques"

    # Étape 2 : Obtient la liste des films disponibles dans le dictionnaire
    available_movies = set()
    for critique in critiques:
        available_movies.update(critiques[critique].keys())

    # Étape 3 : Liste des films non vus par la personne
    unwatched_movies = [movie for movie in available_movies if movie not in critiques[personne]]

    # Étape 4 : Vérifier si la personne a vu tous les films disponibles
    if not unwatched_movies:
        return f"{personne} a vu tous les films disponibles."

    # Étape 5 : Initialisation de la liste des recommandations
    recommendations = []

    # Étape 6 : Parcourir les films non vus par la personne
    for movie in unwatched_movies:
        similarity_scores = []

        # Parcourir les critiques pour calculer la similarité avec la personne
        for critique in critiques:
            if critique != personne and movie in critiques[critique]:
                similarity = pearson(critiques[personne], critiques[critique])
                similarity_scores.append((similarity, critique))

        # Trier les scores de similarité par ordre décroissant
        similarity_scores.sort(reverse=True)

        if similarity_scores:
            weighted_sum = 0
            total_similarity = 0

            # Calcul de la note prédite pour le film en cours
            for similarity, critic in similarity_scores:
                weighted_sum += similarity * critiques[critic][movie]
                total_similarity += abs(similarity)

            # Éviter une division par zéro
            if total_similarity > 0:
                predicted_rating = weighted_sum / total_similarity
                recommendations.append((movie, predicted_rating))

    # Trier les recommandations par ordre décroissant de note prédite
    recommendations.sort(key=lambda x: x[1], reverse=True)

    # Étape 7 : Si des recommandations sont disponibles, retourner la meilleure
    if recommendations:
        best_movie, best_s_prime = recommendations[0]
        return [best_movie, best_s_prime]
    else:
        # Étape 8 : Si aucune recommandation n'est disponible, retourner un message approprié
        return []

def cosinus(x, y):
    #print("\nCOSINUS")
    
    #Etape 0 : x et y sont les vecteurs taille n contenant les notes des films que x et y ont noté (out of range s'ils n'ont pas vu les mêmes films)
    film_x = list(x.keys())
    film_y = list(y.keys())
    
    xy_keys = list(set(film_x))
    
    if (film_x != film_y):
        xy_keys = list(set(film_x) & set(film_y))
    
        x = {key: value for key,value in x.items() if key in xy_keys}
        y = {key: value for key,value in y.items() if key in xy_keys}
        
        x = [value for value in x.values()]
        y = [value for value in y.values()]
    
    #print("X = ", x)
    #print("Y = ", y)
    
    # Étape 1 : Calcul du numérateur (somme des produits des composantes)
    numerator = sum(x[i] * y[i] for i in range(len(x)))

    # Étape 2 : Calcul du dénominateur pour le vecteur x (norme euclidienne)
    denominator_x = math.sqrt(sum(x[i] ** 2 for i in range(len(x))))

    # Étape 3 : Calcul du dénominateur pour le vecteur y (norme euclidienne)
    denominator_y = math.sqrt(sum(y[i] ** 2 for i in range(len(x))))

    # Étape 4 : Calcul du dénominateur total (produit des dénominateurs de x et y)
    denominator = denominator_x * denominator_y

    # Étape 5 : Éviter une division par zéro en cas de dénominateur nul
    if denominator == 0:
        return 0
    else:
        # Étape 6 : Calcul de la mesure de similarité cosinus
        # La similarité cosinus mesure l'angle entre les vecteurs x et y dans l'EV correspondant.
        # Plus la similarité est proche de 1, plus les vecteurs sont similaires dans la direction. -> les personnes sont proches
        # Plus la similarité est proche de 0, moins les vecteurs sont similaires. -> les personnes sont peu proches
        return numerator / denominator

    
def CosinusRecommend(person, Critiques):
    # Étape 1 : Vérifier si la personne est une clé du dictionnaire
    if person not in Critiques:
        return f"La personne '{person}' n'existe pas dans le dictionnaire des critiques"

    # Étape 2 : Obtient la liste des films disponibles dans le dictionnaire
    available_movies = set()
    for critique in Critiques:
        available_movies.update(Critiques[critique].keys())

    # Étape 3 : Liste des films non vus par la personne
    unwatched_movies = [movie for movie in available_movies if movie not in Critiques[person]]

    # Étape 4 : Vérifier si la personne a vu tous les films disponibles
    if not unwatched_movies:
        return f"{person} a vu tous les films disponibles."

    # Étape 5 : Initialisation de la liste des recommandations
    recommendations = []

    # Étape 6 : Parcourir les films non vus par la personne
    for movie in unwatched_movies:
        similarity_scores = []

        # Parcourir les critiques pour calculer la similarité avec la personne
        for critique in Critiques:
            if critique != person and movie in Critiques[critique]:
                # Calculer la similarité cosinus entre les critiques de la personne et de la critique en cours
                
                similarity = cosinus(Critiques[person], Critiques[critique])
                similarity_scores.append((similarity, critique))

        # Trier les scores de similarité par ordre décroissant
        similarity_scores.sort(reverse=True)

        if similarity_scores:
            weighted_sum = 0
            total_similarity = 0

            # Calcul de la note prédite pour le film en cours
            for similarity, critic in similarity_scores:
                weighted_sum += similarity * Critiques[critic][movie]
                total_similarity += similarity

            # Éviter une division par zéro
            if total_similarity > 0:
                predicted_rating = weighted_sum / total_similarity
                recommendations.append((movie, predicted_rating))

    # Trier les recommandations par ordre décroissant de note prédite
    recommendations.sort(key=lambda x: x[1], reverse=True)

    # Étape 7 : Si des recommandations sont disponibles, retourner la meilleure
    if recommendations:
        best_movie, best_s_prime = recommendations[0]
        return [best_movie, best_s_prime]
    else:
        # Étape 8 : Si aucune recommandation n'est disponible, retourner un message approprié
        return []

def sim_distanceTchebychev(person1, person2):
    # Étape 1 : Trouver les films communs (vus par les deux personnes) entre person1 et person2
    common_movies = [movie for movie in person1 if movie in person2]
    
    # Si aucune critique commune n'est trouvée, retourne 0 (distance minimale)
    if len(common_movies) == 0:
        return 0
    
    # Étape 2 : Calculer la distance de Manhattan entre les deux personnes pour les films communs
    manhattan_distance = max(abs(person1[movie] - person2[movie]) for movie in common_movies)
    # Pour chaque film commun, calcule la valeur absolue de la différence entre les critiques de person1 et person2,
    # puis somme ces différences pour tous les films communs.

    return manhattan_distance  # Retourne la distance de Manhattan entre les deux personnes

def print_message(result, personne_a_recommander):
    message = ""
    
    if (result == []):
        print("Aucun film à recommander à ", personne_a_recommander)
    else:
        print("Meilleur recommandation pour ", personne_a_recommander," est ", result[0], " ( score = ", result[1],")")
        print("D'après la similarité des notes que ", personne_a_recommander," a attribué avec celles des autres personnes ayant vu des films en commun, nous conseillons le film ", result[0])
        
import random

#génère un dictionnaire aléatoire des notes attribuées par les personnes des films tout en respectant le taux de cellule vide imposé (30 à 50%)
def random_dico(liste_film, liste_personne,personne_a_recommander):
    liste_note_possible = [0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5]
    dico_critiques = {}
    
    for personne in liste_personne:
        
        film_watched = random.sample(liste_film,random.randint(0,len(liste_film))) #Choisi aléatoirement les films que "personne" a vu
        dico_film_watched = {}
        
        for film in film_watched: #pour chaque film déjà vu par "personne"
            dico_film_watched[film] = random.choice(liste_note_possible)
        dico_critiques[personne] = dico_film_watched
    
    dico_critiques[personne_a_recommander] = random_dico_personne(liste_film)
    
    if (taux_cellules_vides(dico_critiques) > 30 and taux_cellules_vides(dico_critiques) > 50):
        dico_critiques = random_dico(liste_film, liste_personne, personne_a_recommander)
        
    return dico_critiques

#Génère les films vu par la personne que l'on cherche à recommander
def random_dico_personne(liste_film):
    liste_note_possible = [0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5]
    
    film_watched = random.sample(liste_film,random.randint(0,7)) #Choisi aléatoirement les films que "personne" a vu (personne a vu <= 50% des films)
    dico_film_watched = {}
    
    for film in film_watched: #pour chaque film déjà vu par "personne"
            dico_film_watched[film] = random.choice(liste_note_possible)
    return dico_film_watched

def calculate_s_prime_bis(a, personne, Critiques, choice):
    # Étape 1 : Vérifier si la personne est une clé du dictionnaire
    if personne not in Critiques:
        return f"La personne '{personne}' n'existe pas dans le dictionnaire des critiques", [], None, None

    # Étape 2 : Obtient la liste des films disponibles dans le dictionnaire
    available_movies = set()
    for critique in Critiques:
        available_movies.update(Critiques[critique].keys())

    # Étape 3 : Vérifier si le film choisi appartient à la liste des films disponibles
    if a not in available_movies:
        return f"Le film '{a}' n'existe pas dans la liste des films disponibles", list(available_movies), None, None

    # Étape 4 : Vérifier si la personne a vu le film choisi en parametres
    if a in Critiques[personne]:
        message = f"Le film '{a}' a déjà été vu par '{personne}'"
        return message, [], None, None

    # Étape 5 : Liste des critiques ayant attribué une note au film choisi mais n'ayant pas encore vu le film choisi
    C_a = [critique for critique in Critiques if a in Critiques[critique] and a not in Critiques[personne]]

    # Initialiser des variables pour le calcul de s prime pour le film choisi
    total_a = 0
    s_a = 0

    # Étape 6 : Calcul de s prime pour le film choisi
    for critique in C_a:
        # Calcul de la similarité entre la personne actuelle et la critique de l'autre personne choisie selon Manhattan (peut etre modifie en choissant euclidienne)
        
        if (choice == "1"):
            distance = 1 / (1 + sim_distanceEuclidienne(Critiques[critique], Critiques[personne]))
            
        elif(choice =="2"):
            distance = 1 / (1 + sim_distanceManhattan(Critiques[critique], Critiques[personne]))
            
        elif(choice =="5"):
            distance = 1 / (1 + sim_distanceTchebychev(Critiques[critique], Critiques[personne]))    
            
        # Ajout pondéré de la note du film choisi à total_a
        total_a += distance * Critiques[critique][a]
        
        # Accumulation des distances pour le calcul de s_a
        s_a += distance

    # Éviter une division par zéro
    if s_a == 0:
        return "s(a) = 0", C_a, s_a, total_a

    # Calcul de s prime pour le film choisi en utilisant les valeurs calculées précédemment
    s_prime_a = total_a / s_a

    # Retourne s prime pour le film choisi ainsi que d'autres informations utiles
    return s_prime_a, C_a, s_a, total_a

def bestRecommend_bis(personne, Critiques, choice):
    # Étape 1 : Vérifier si la personne est une clé du dictionnaire
    if personne not in Critiques:
        return f"La personne '{personne}' n'existe pas dans le dictionnaire des critiques"

    # Étape 2 : Obtient la liste des films disponibles dans le dictionnaire
    available_movies = set()
    for critique in Critiques:
        available_movies.update(Critiques[critique].keys())

    # Étape 3 : Liste des films non vus par la personne
    unwatched_movies = [movie for movie in available_movies if movie not in Critiques[personne]]

    # Étape 4 : Vérifier si la personne a vu tous les films disponibles
    if not unwatched_movies:
        return f"{personne} a vu tous les films disponibles."

    # Étape 5 : Initialisation des variables pour le meilleur film et la meilleure estimation de note
    best_movie = None
    best_s_prime = None

    # Étape 6 : Parcourir les films non vus par la personne
    for movie in unwatched_movies:
        # Calculer s_prime_a pour le film en cours
        result = calculate_s_prime_bis(movie, personne, Critiques, choice)
        
        # Ignorer les erreurs (cas où calculate_s_prime renvoie une chaîne de caractères)
        if isinstance(result, str):
            continue

        s_prime_a = result[0]
        
        # Mettre à jour le meilleur film et la meilleure estimation de note
        if best_movie is None or s_prime_a > best_s_prime:
            best_movie = movie
            best_s_prime = s_prime_a

    # Étape 7 : Si aucun film recommandable n'est trouvé, retourner un message approprié
    if best_movie is None:
        return []

    # Étape 8 : Retourner la meilleure recommandation et sa note associee
    return [best_movie, best_s_prime]

#Trouve le random dico approprié pour que chaque mesure renvoie un résultat différent
def recommend_movie(personne_a_recommander, liste_film, liste_personne):
    #print("\nDébut recommend different movie")
    
    dico_random = random_dico(liste_film, liste_personne,personne_a_recommander)
        
    #print(dico_random)
    
    set_film_result = set()
    
    x1 = bestRecommend_bis(personne_a_recommander, dico_random, "1")
    x2 = bestRecommend_bis(personne_a_recommander, dico_random, "2")
    x3 = CosinusRecommend(personne_a_recommander, dico_random)
    x4 = pearson_recommend(personne_a_recommander, dico_random)
    x5 = bestRecommend_bis(personne_a_recommander, dico_random, "5")
    
    #print("X1 = ", x1)
    #print("X2 = ", x2)
    #print("X3 = ", x3)
    #print("X4 = ", x4)
    #print("X5 = ", x5)
    
    
    if (len(x1)>0 and len(x2)>0 and len(x3)>0 and len(x4)>0 and len(x5)>0):
        set_film_result.add(x1[0])
        set_film_result.add(x2[0])
        set_film_result.add(x3[0])
        set_film_result.add(x4[0])
        set_film_result.add(x5[0])
        
    """    
    #print("ENSEMBLE = ", set_film_result)
    if (len(set_film_result) != 5):
        recommend_different_movie(personne_a_recommander, liste_film, liste_personne)
    else:
        print("Fin de l'algorithme DIFFERENT")
        print(dico_random, set_film_result)
        return (dico_random,set_film_result)
    """
    return [dico_random, set_film_result]


"""
#Trouve le random dico approprié pour que chaque mesure renvoie un résultat différent
def recommend_same_movie(personne_a_recommander, liste_film, liste_personne):
    #print("\nDébut recommend same movie")
    
    dico_random = random_dico(liste_film, liste_personne,personne_a_recommander)
    
    #print(dico_random)

    set_film_result = set()
    
    x1 = bestRecommend_bis(personne_a_recommander, dico_random, "1")
    x2 = bestRecommend_bis(personne_a_recommander, dico_random, "2")
    x3 = CosinusRecommend(personne_a_recommander, dico_random)
    x4 = pearson_recommend(personne_a_recommander, dico_random)
    x5 = bestRecommend_bis(personne_a_recommander, dico_random, "5")
    
    #print("X1 = ", x1)
    #print("X2 = ", x2)
    #print("X3 = ", x3)
    #print("X4 = ", x4)
    #print("X5 = ", x5)
    
    if (len(x1)>0 and len(x2)>0 and len(x3)>0 and len(x4)>0 and len(x5)>0):
        set_film_result.add(x1[0])
        set_film_result.add(x2[0])
        set_film_result.add(x3[0])
        set_film_result.add(x4[0])
        set_film_result.add(x5[0])
     
    #print("ENSEMBLE = ", set_film_result)
    if (len(set_film_result) != 1):
        recommend_same_movie(personne_a_recommander, liste_film, liste_personne)
    else:
        print("Fin de l'algorithme SAME")
        print(dico_random, set_film_result)
        return (dico_random,set_film_result)
    
    return [dico_random,set_film_result]
"""

# Affichage
#Partie 1 : Pourcentage de cellules vides du dictionnaire en parametre
taux = taux_cellules_vides(critiques)
print(f"Le taux de cellules vides dans le dictionnaire choisi (matrice d'evaluation) est de {taux:.2f}%.\n") #On obtient normalement 20,83% <=> 10/48 * 100 pour le dictionnaire critiques


# Partie 2(a) i : distance euclidienne / manhattan
person1 = "Lisa Rose"
person2 = "Gene Seymour"

if person1 not in critiques:
    print(f"La personne '{person1}' n'existe pas dans le dictionnaire des critiques.")
elif person2 not in critiques:
    print(f"La personne '{person2}' n'existe pas dans le dictionnaire des critiques.")
else:
    distance_manhattan = sim_distanceManhattan(critiques[person1], critiques[person2])
    distance_euclidienne = sim_distanceEuclidienne(critiques[person1], critiques[person2])
    print("Distance de Manhattan entre", person1, "et", person2, ":", distance_manhattan)
    print("Distance euclidienne entre", person1, "et", person2, ":", distance_euclidienne,"\n")

# Partie 2(a) ii : Ppv + Recommend
person_to_find = 'Lisa Rose'   # Remplacer par les autres personnes pour test
result = computeNearestNeighbor(person_to_find, critiques)

if isinstance(result, str):
    print(result)
else:
    print(f"Plus proches voisins de {person_to_find} :", result,"\n")
    
print("Recommandation ppv naive :")
person_to_recommend_for = 'Lisa Rose'  # Remplacer par les autres personnes pour test
result = recommend(person_to_recommend_for, critiques)

print_message(result, person_to_recommend_for)

print("\n")

# Partie 2(b) i : Global score
film_a = "Night"
personne = "Anne"
result = calculate_s_prime(film_a, personne, critiques)

if isinstance(result, str):
    print(result)
else:
    s_prime_a, C_a, s_a, total_a = result
    if isinstance(s_prime_a, str):
        print(s_prime_a)  # Afficher le message d'erreur
    else:
        print(f"Pour le film '{film_a}' non vu par '{personne}': \n")
      
        if C_a:
            print(f"C(a) = {C_a}")
            print(f"total(a) = {total_a:.8f}")
            print(f"s(a) = {s_a:.8f}")
        print(f"s'(a) = {s_prime_a:.4f}")
print("\n")

# Partie 2(b) ii : Best Recommand
print("Recommandation Best global score (poids distance inverse) :")
person_to_recommend_for = 'Anne'
result = bestRecommend(person_to_recommend_for, critiques)

print_message(result, person_to_recommend_for)
print("\n")  


# Utilisation de la fonction otherBestRecommend
print("Recommandation Other best global score :")
person_to_recommend_for = 'Anne'
result = otherBestRecommend(person_to_recommend_for, critiques)

print_message(result, person_to_recommend_for)
print("\n")

# Partie 3 : Pearson
print("Recommandation Pearson :")
person_to_recommend_for = 'Anne'  # Remplacer par les autres personnes pour test
result = pearson_recommend(person_to_recommend_for, critiques)
print_message(result, person_to_recommend_for)
print("\n")  

# Partie 4 : Cosinus
print("Recommandation Cosinus :")
person_to_recommend_for = 'Anne'  # Remplacer par les autres personnes pour test
result = CosinusRecommend(person_to_recommend_for, critiques)
print_message(result, person_to_recommend_for)

print("\n")

#Partie 5 et 6 : Initialisation de la liste des films et personnes
liste_film = ["Harry Potter", "Interstellar", "Barbie", "Spiderman", "Mon voisin Totoro", "Wall-E", "Mr. Bean", "Hunger games", "Labyrinthe", "Twilight", "Titanic", "Cendrillon", "Madagascar", "Tortue Ninja", "Shrek"]
liste_personne = ["Darlène", "Christian", "Skander", "Lucy", "William", "Lisa", "Haru", "Louisa", "Cédric", "Marine"]

personne_a_recommander = "Anne"

# Partie 5 : Recommandation unique pour 5 mesures différentes
result_same = recommend_movie(personne_a_recommander, liste_film, liste_personne)
nb_iteration_same = 0

while (len(result_same[1]) != 1):
    result_same = recommend_movie(personne_a_recommander, liste_film, liste_personne)
    nb_iteration_same += 1

dico_random_same = result_same[0]
set_film_same = result_same[1]

print("RESULTAT (films identiques) en ", nb_iteration_same, "itération(s) :", dico_random_same, "\n", set_film_same, "\n")
print("Taux de cellules vides du dictionnaire : ", round(taux_cellules_vides(dico_random_same),2),"%")

print("\n")

# Partie 6 : Recommandation différentes pour 5 mesures différentes
result_diff = recommend_movie(personne_a_recommander, liste_film, liste_personne)
nb_iteration_diff = 0

while (len(result_diff[1]) < 5):
    result_diff = recommend_movie(personne_a_recommander, liste_film, liste_personne)
    nb_iteration_diff += 1

dico_random_different = result_diff[0]
set_film_different = result_diff[1]

print("RESULTAT (films différents) en ", nb_iteration_diff, " itération(s) :\n", dico_random_different, "\n", set_film_different, "\n")
print("Taux de cellules vides du dictionnaire : ", round(taux_cellules_vides(dico_random_different),2),"%\n")

