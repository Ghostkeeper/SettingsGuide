Impression filaire
====
Ce paramètre permet un mode d'impression complètement différent appelé Wire Printing. Lorsque l'impression à fil est utilisée, l'imprimante ne fabrique pas un objet solide, mais seulement un treillis triangulaire de la forme extérieure à partir de fils fins.

Cette technique présente un certain nombre d'avantages :
* Elle permet d'imprimer beaucoup plus rapidement qu'un objet solide.
* Elle n'utilise qu'une fraction de la matière utilisée par l'impression normale.
* Elle a un aspect spécial, comme si elle était construite manuellement avec un stylo d'impression 3D.

L'objet qui en résulte n'est cependant pas fonctionnel. Il aura à peu près la bonne taille, ce qui le rend utile pour prototyper la sensation d'échelle de l'impression, bien que la taille ne soit pas très précise non plus. L'objet obtenu est extrêmement fragile, non seulement pendant l'impression, mais aussi après. Il est difficile de l'enlever de la plaque de montage sans l'endommager. Le modèle perdra également la plupart de ses détails.

L'impression au fil de fer consiste à déposer des anneaux de matériau avec un espacement vertical assez important de plusieurs millimètres. Entre ces anneaux, elle dessine une forme en dents de scie qui permet à l'anneau suivant de reposer sur le précédent. Lorsque la surface du modèle est horizontale, une technique similaire est utilisée pour fermer le sommet. Dans le toit, il y a des anneaux concentriques maintenus ensemble par une forme en dents de scie, soigneusement suspendue en l'air par un bâtiment de l'extérieur (où elle peut reposer sur un mur) vers l'intérieur.

L'impression au fil de fer ne fonctionne vraiment de manière fiable qu'avec des formes presque entièrement verticales, comme le type de modèle qui fonctionnerait bien avec le mode [Spiraliser le contour extérieur](../blackmagic/magic_spiralize.md). Si la surface est horizontale sur de grandes surfaces, la technique de fermeture du toit doit couvrir une distance extrêmement grande. Dans ce cas, il est fort probable que la technique échouera. Si le modèle continue ensuite à monter à mi-chemin sur une surface horizontale, il sera presque certainement imprimé en plein air.

**La vue en couches de Cura n'affichera pas correctement l'impression au fil de fer directement après le découpage. Cependant, le résultat peut toujours être prévisualisé en enregistrant le g-code sur le disque et en ouvrant à nouveau ce g-code avec Cura.**
