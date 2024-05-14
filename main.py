import pandas as pd
import os

# Chemin vers le répertoire contenant vos fichiers CSV
repertoire = "./fusion1"

# Liste pour stocker les DataFrames de chaque fichier CSV
frames = []

# Parcours des fichiers dans le répertoire
for fichier in os.listdir(repertoire):
    if fichier.endswith(".csv"):
        chemin_fichier = os.path.join(repertoire, fichier)
        # Charger chaque fichier CSV dans un DataFrame
        df = pd.read_csv(chemin_fichier)
        # Ajouter le DataFrame à la liste
        frames.append(df)

# Concaténer tous les DataFrames en un seul
resultat = pd.concat(frames, ignore_index=True)

# Enregistrer le DataFrame résultant dans un nouveau fichier CSV
resultat.to_csv("tweet_senegal.csv", index=False)

print("Fusion terminée. Le fichier fusion.csv a été créé avec succès.")

'''

# Chemin vers votre fichier CSV
chemin_fichier = "./fusion.csv"

# Lire le fichier CSV dans un DataFrame
df = pd.read_csv(chemin_fichier)

# Afficher les premières lignes du DataFrame pour visualiser son contenu
print(df[:20])

'''