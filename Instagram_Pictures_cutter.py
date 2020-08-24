#importe le module image de la bibliothéque PIL
from PIL import Image

#récupère l'image original
image_original = Image.open( str( input( "Entre le nom de l\'image mise au préalable dans le meme dossier que ce programme" ) ) )

#récupère les dimensions (en pixel) de l'image
longueur, largeur = image_original.size

#crée les variables de haut et bas 
haut = 0
bas = largeur

#determine le nombre d'images possible de faire dans le fichier
nombre_de_decoupe = longueur // largeur

#créé les images au format carré de l'image original
for i in range(nombre_de_decoupe):
    gauche = largeur * i
    droite = largeur * ( i + 1 )
    image_modif = image_original.crop((gauche,haut,droite,bas))
    image_modif.save( "image" + str(i + 1) + ".jpg" )


