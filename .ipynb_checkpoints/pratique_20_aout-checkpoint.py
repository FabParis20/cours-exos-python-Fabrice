def annee_naissance(age):
    annee = 2025 - age    
    return annee
    

# print(annee_naissance(47))

def centrer(chaine):
    car_restant = 40 - len(chaine)
    espace_avant = car_restant//2
    espace_apres = car_restant - espace_avant
    mis_en_forme = "|" + (" " * espace_avant) + chaine + (" " * espace_apres) + "|"
    return(mis_en_forme)
    
# print(centrer("Loki"))

def centrer_def(chaine, largeur = 40):
    car_restant = largeur - len(chaine)
    espace_avant = car_restant//2
    espace_apres = car_restant - espace_avant
    mis_en_forme = "|" + (" " * espace_avant) + chaine + (" " * espace_apres) + "|"
    return(mis_en_forme)

# print(centrer_def("Fabrice", 50))

def encadrer(chaine, largeur = 40, motif = "#"):
    mis_en_forme = centrer_def(chaine, largeur)
    frise = motif * len(mis_en_forme)
    return(frise + "\n" + mis_en_forme + "\n" + frise)

# print(encadrer("Cédric", motif="{"))

def adapter_valeur(truc):
    for carac in truc
    if type(truc) == str:
        return truc
    else:
        for carac in truc:
            if type(carac) == str    
    
print(c_quoi(123))

Paris75
1.37
Loki



