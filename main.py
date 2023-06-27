# Ce script Python va traiter un fichier CSV nommé "Passage de grade 2023.csv". 
# Ce fichier contient plusieurs informations pour chaque ligne un participant avec les colonnes suivantes:
#     - Titre, Membres (à formater), Date de l'examen, Date de naissance, Grade actuel, Grade cible, URL Image, Paiement, Résultat, ...

# Sur la base des informations de ce fichier, le script va créer automatiquement sur base d'un template d'image
#     - Ajouter les informations suivantes:
#         - Membres --> au centre et en bas à droite
#         - Date de naissance --> au centre
#         - Grade cible --> au centre
#         - Date de l'examen --> en haut à droit
#     - Enregistrer le template de l'image sous le nom "Membres_ + nom de l'image template

from PIL import Image, ImageDraw, ImageFont
import pandas as pd

# Lire les données du CSV
data = pd.read_csv('csv files/Passage de grade 2023.csv')

# Nettoyer les données dans la colonne 'Membres'
data['Membres'] = data['Membres'].str.split(' \\(').str[0]
# print(data)
print('Début du script')

# Parcourir chaque ligne du CSV
for index, row in data.iterrows():
    # Ouvrir l'image du template
    img = Image.open(row['URL IMAGE'])

    # Initialiser un objet ImageDraw pour dessiner sur l'image
    draw = ImageDraw.Draw(img)

    # Définir la police (vous devrez ajuster le chemin et la taille selon vos besoins)
    font = ImageFont.truetype("font/arial_mt_black/ARIBL0.ttf", 17)
    font_small = ImageFont.truetype("font/arial_mt_black/ARIBL0.ttf", 12)

    # Ajouter le texte à l'image 
    draw.text((1000, 180), f"{row['Date examen']}", font=font, fill='black')
    draw.text((580, 420), f"{row['Membres']}", font=font, fill='black')
    draw.text((580, 465), f"{row['Date de naissance']}", font=font, fill='black')
    draw.text((580, 510), f"{row['Grade cible']}", font=font, fill='black')
    draw.text((970, 720), f"{row['Membres']}", font=font, fill='black')
    font = ImageFont.truetype("font/arialn/Arialn.ttf", 14)
    draw.text((950, 745), f"Signature du candidat", font=font_small, fill='black')

    # Extrait le nom du fichier de l'URL de l'image
    filename = row['URL IMAGE'].split('/')[-1]

    # Enregistrez l'image avec le nouveau nom
    img.save(f"{row['Membres']}_{filename}")



print('Images modifiées avec succès.')
