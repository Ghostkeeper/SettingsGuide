Image de densité du remplissage croisé
====
Dans ce paramètre, vous pouvez fournir une image qui spécifie la densité à différents endroits du remplissage. La densité de remplissage variera à certains endroits en fonction de la luminosité de l'image. Cela ne fonctionne que pour le [motif en croix (3D)](../infill/infill_pattern.md), car ce motif est capable d'ajuster sa densité sans hacher les lignes, ce qui entraînerait une interruption du flux et une réduction de la force.

![La densité de remplissage varie selon l'objet](../../../articles/images/cross_infill_density_image.png)
![Le fichier image utilisé pour créer ce motif](../../../articles/images/cross_infill_density_image_mask.png)

Le chemin vers l'image est fourni comme un chemin local, par exemple `C:\Projects\3D Printing\infill_density.png` sous Windows ou `/home/ghostkeeper/3d_printing/infill_density.png` sous Unix. Les formats de fichiers supportés sont JPG, PNG, TGA, BMP, PSD, GIF, HDR et PIC. L'image est mise à l'échelle sur l'objet de telle sorte qu'elle s'adapte exactement à la boîte de délimitation de l'objet. La luminosité de l'image détermine la densité de remplissage :
* Lorsque l'image est noire, la [densité de remplissage](../infill/infill_sparse_density.md) est utilisée.
* Lorsque l'image est blanche, la densité de remplissage est proche de 0 %.

La densité de remplissage ne dépassera jamais la valeur spécifiée par la [distance de la ligne de remplissage](../infill/infill_line_distance.md). Elle peut seulement être réduite. Le modèle est également limité dans les cas où il peut réduire sa densité. Bien qu'il essaie de se rapprocher le plus possible de la densité de remplissage souhaitée, cela n'est pas toujours possible. Si la densité de remplissage est vraiment faible, il y aura particulièrement peu de possibilités d'ajuster la densité de remplissage, ce qui fait que l'impression suit l'image de manière très lâche. Dans les endroits où la densité de remplissage est élevée, l'image sera suivie de très près. La densité choisie est également fortement quantifiée. La densité peut seulement être doublée ou réduite de moitié, mais Cura [dither](https://en.wikipedia.org/wiki/Dither) le motif afin d'obtenir une plus grande précision effective.

Avec ce réglage, vous pouvez personnaliser votre remplissage très loin. Comme les motifs de remplissage en croix sont principalement utilisés avec des matériaux flexibles, ce réglage est utilisé pour obtenir des contraintes de douceur ou de dureté très spécifiques. Par exemple, on peut imprimer une semelle de chaussure avec une douceur personnalisée pour mieux s'adapter aux pieds, ou un dispositif mécanique qui doit se plier en des parties spécifiques. 

**Ce paramètre ne sera pas bien transféré dans les fichiers du projet Cura. Le fichier de projet enregistrera le chemin d'accès à l'image comme valeur de réglage, mais ne stockera pas l'image. Si le fichier de projet est ouvert sur un autre ordinateur, l'image de densité ne sera probablement pas restaurée.**

