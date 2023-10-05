import csv
import os

Folder = "CSV"

def search_object_group(nom_fichier, mot_recherche):
    Path = os.path.join(Folder, nom_fichier)
    
    # Ouvrez le fichier CSV en mode lecture
    with open(Path, mode='r', newline='') as file:
        # Créez un objet lecteur CSV
        lecteur_csv = csv.reader(file)

        # Parcourez chaque ligne du fichier
        for ligne in lecteur_csv:
            #print(ligne)
            # Vérifiez si le mot de recherche est présent dans la première colonne (colonne 0)
            premiere_partie = ligne[0].split(';')[0].strip() 
            # Obtenir la première partie jusqu'au premier point-virgule
            if premiere_partie == mot_recherche:
                deuxieme_partie = ligne[0].split(';')[1].strip()
                #print(mot_recherche + " " + deuxieme_partie)
                # Si le mot est trouvé, retournez le contenu de la deuxième colonne (colonne 1)
                return deuxieme_partie
    
    # Si le mot de recherche n'est pas trouvé, renvoie None
    return None

