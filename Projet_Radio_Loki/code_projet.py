import json

with open(r"C:\Users\Fab\Documents\Cours_Python_Fabrice\Projet_Radio_Loki\playlist.json") as pl_brute:
    donnees_brutes = json.load(pl_brute)
    pl_brute.close()

dict_brut = donnees_brutes["playlist"]["trackList"]["track"]

cles_voulues = ["title", "album", "creator", "duration"]

# Fonction qui recherche clés voulues dans chaque dictionnaire de track brut
def construire_pl(cle, dict_track_brut): 
    if cle in dict_track_brut.keys():
        return cle, dict_track_brut[cle]
    else:
        return cle, None

def imprime_playlist(dict_brut):
    for dict_track_brut in dict_brut:
        for cle in cles_voulues:
            item, info = construire_pl(cle, dict_track_brut)
        print(f"{item} : {info}")            
        print("=================================================")


import math

def convertir_mil_en_min_sec(milliemes):
    total_secondes = round(milliemes / 1000)
    minutes = total_secondes//60
    secondes = total_secondes % 60
    duree_min_sec = f"{minutes} ' {secondes}"
    return duree_min_sec

def construire_liste_dict(dict_brut):
    dictionnaire = []
    for dict_track_brut in dict_brut:
        morceau = {}
        for cle in cles_voulues:
            if cle == "duration":
                item, info = construire_pl(cle, dict_track_brut)
                info = convertir_mil_en_min_sec(int(info))
            else:
                item, info = construire_pl(cle, dict_track_brut)       
           
            morceau[item] = info
        dictionnaire.append(morceau)
    return dictionnaire

print(construire_liste_dict(dict_brut))

# faire_playlist(infos_liste)

# Pour construire le csv, j'utilise la classe csv.DictWritter, trouvée en faisant des recherches :
"""- Le paramètre fieldnames est une séquence de clés identifiant l'ordre d'écriture des valeurs du dictionnaire transmis à la méthode writerow() dans le fichier f.
Exemple extrait de https://www.geeksforgeeks.org/python/how-to-save-a-python-dictionary-to-a-csv-file/

import csv

cars = [
    {"Brand": "Toyota", "Model": "Corolla", "Year": 2020},
    {"Brand": "Honda", "Model": "Civic", "Year": 2019},
    {"Brand": "Ford", "Model": "Focus", "Year": 2018}
]

# CSV file name
csv_filename = "cars.csv"

# Define the field names (headers)
fieldnames = ["Brand", "Model", "Year"]

# Writing to CSV
with open(csv_filename, mode='w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()  # Write header row
    writer.writerows(cars)  # Write data rows

"""


    

import csv

with open('playlist.csv', 'w', newline='') as csvfile:
    # cles_voulues = ["title", "album", "creator", "duration"]
    writer = csv.DictWriter(csvfile, fieldnames=cles_voulues)
    writer.writeheader()
    writer.writerows(construire_liste_dict(dict_brut))   

 



# A faire : afficher de manière claire (avec des ----) les infos intéressantes (en print)
# Construire un dict 
# Si motivé : créer un cvs avec les données. Option : durée en minutes / secondes
# Idée sur pas 2 fois le même artiste de suite
# Essayer de faire dans Gradio : 1. lister des morceaux de moins de ... 2. Trouver auteur ... 