import csv
import os



Folder = "CSV"

def search_object(nom_fichier, mot_recherche):
    
    Path = os.path.join(Folder, nom_fichier)
    #print(Path)
        # Ouvrez le fichier CSV en mode lecture
    with open(Path, mode='r', newline='') as file:
            # Créez un objet lecteur CSV
            lecteur_csv = csv.reader(file)

            # Parcourez chaque ligne du fichier
            for ligne in lecteur_csv:
                #print(ligne[0])
                # Vérifiez si le mot de recherche est présent dans la première colonne (colonne 0)
                premiere_partie = ligne[0].split(';')[0].strip()  # Obtenir la première partie jusqu'au premier point-virgule
                if premiere_partie == mot_recherche:
                    #print("TRUE")
                    return True  # Renvoie True si le mot est trouvé dans la première colonne
            # Si le mot de recherche n'est pas trouvé, renvoie False
            #print("False")
            return False
            


