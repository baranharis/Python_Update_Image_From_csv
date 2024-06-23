# Ce script Python va traiter un fichier CSV nommé "Passage de grade 2023.csv". 
# Ce fichier contient plusieurs informations pour chaque ligne un participant avec les colonnes suivantes:
#     - Titre, Membre (à formater), Date de l'examen, Date de naissance, Grade actuel, Grade cible, URL Image, Paiement, Résultat, ...

# Sur la base des informations de ce fichier, le script va créer automatiquement sur base d'un template d'image
#     - Ajouter les informations suivantes:
#         - Membre --> au centre et en bas à droite
#         - Date de naissance --> au centre
#         - Grade cible --> au centre
#         - Date de l'examen --> en haut à droit
#     - Enregistrer le template de l'image sous le nom "Membre_ + nom de l'image template

from PIL import Image, ImageDraw, ImageFont
import pandas as pd

# Lire le fichier CSV brut pour vérifier son contenu
# with open('csv files/Passage de grade 2024.csv', 'r') as file:
#     content = file.read()
#     print("Contenu brut du fichier CSV :\n", content)

# Lire les données du CSV avec le bon séparateur et en spécifiant la ligne d'en-tête
data = pd.read_csv('csv files/Passage de grade 2024.csv', sep=';', header=0)

# Afficher les noms des colonnes pour vérifier
# print("Colonnes disponibles dans le CSV :", data.columns)

# Afficher les premières lignes du CSV pour un aperçu
# print("Aperçu des données du CSV :", data.head())

# Vous pouvez également utiliser `data.info()` pour plus de détails
# print(data.info())

# Vérifier si la colonne 'Membre' existe
if 'Membre' in data.columns:
    # Nettoyer les données dans la colonne 'Membre'
    data['Membre'] = data['Membre'].str.split(' \\(').str[0]
    print('Début du script')

    # Parcourir chaque ligne du CSV
    for index, row in data.iterrows():
        # Ouvrir l'image du template
        img = Image.open(row['URL Image'])

        # Initialiser un objet ImageDraw pour dessiner sur l'image
        draw = ImageDraw.Draw(img)

        # Définir la police (vous devrez ajuster le chemin et la taille selon vos besoins)
        font = ImageFont.truetype("font/arial_mt_black/ARIBL0.ttf", 77)
        font_small = ImageFont.truetype("font/arial_mt_black/ARIBL0.ttf", 72)

        # Ajouter le texte à l'image 
        draw.text((4000, 700), f"{row['Date examen']}", font=font, fill='black')
        draw.text((2300, 1680), f"{row['Membre']}", font=font, fill='black')
        draw.text((2300, 1860), f"{row['Date de naissance']}", font=font, fill='black')
        draw.text((2300, 2030), f"{row['Grade cible']}", font=font, fill='black')
        # draw.text((970, 720), f"{row['Membre']}", font=font, fill='black')
        font = ImageFont.truetype("font/arialn/Arialn.ttf", 14)
        # draw.text((950, 745), f"Signature du candidat", font=font_small, fill='black')

        # Extrait le nom du fichier de l'URL de l'image
        filename = row['URL Image'].split('/')[-1]

        # Enregistrez l'image avec le nouveau nom
        img.save(f"updated images/{row['Membre']}_{filename}")

    print('Images modifiées avec succès.')
else:
    print("Erreur : La colonne 'Membre' n'existe pas dans le CSV.")
print('Fin du script')
