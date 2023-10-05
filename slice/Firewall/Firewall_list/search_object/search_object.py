import csv
import os



Folder = "CSV"

def search_object(nom_fichier, mot_recherche):
    
    Path = os.path.join(Folder, nom_fichier)

    with open(Path, mode='r', newline='') as file:

            lecteur_csv = csv.reader(file)

    
            for ligne in lecteur_csv:
  
                premiere_partie = ligne[0].split(';')[0].strip()  
                if premiere_partie == mot_recherche:
  
                    return True  
 
            return False
            


