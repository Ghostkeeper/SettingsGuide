Préférence de jointure d'angle
===

Avec ce réglage, vous pouvez contrôler la position des coutures par rapport aux coins de votre modèle.

En général, il existe deux options pour l'endroit où la couture peut être placée : cachée dans un coin intérieur ou exposée dans un coin extérieur. Il est généralement préférable de cacher la couture dans un coin intérieur, car la couture y sera à peine visible. Mais il est également possible de la placer dans un coin extérieur afin de pouvoir couper le joint avec un couteau ou de le poncer avec du papier de verre, si un post-traitement peut être effectué sur la pièce.

Voici les options disponibles pour ce réglage et leurs effets.
* **Aucun :** Il n'y a aucune préférence pour les coins. La couture sera choisie de manière à correspondre au mieux aux exigences de [Z Seam Alignment](z_seam_type.md).
* **Masquer jointure :** Il est préférable de cacher la couture dans un coin intérieur. Si l'alignement de la couture en Z est réglé sur "coin le plus net", le coin le plus intérieur est toujours choisi. S'il est réglé sur "le plus court", un coin intérieur est choisi qui est proche de la position actuelle de la buse lorsqu'elle commence le contour.
* **Exposer jointure :** Il est préférable d'exposer la couture sur un coin extérieur. Si l'alignement du joint en Z est réglé sur "Coin le plus net", le coin extérieur le plus net est toujours choisi. S'il est réglé sur "le plus court", un coin extérieur est choisi qui est proche de la position actuelle de la buse lorsqu'elle commence le contour.
* **Masquer ou exposer jointure :** Cette fonction permet de placer un joint sur un coin pointu, qu'il soit intérieur ou extérieur, tant qu'il ne se trouve pas sur un mur plat.
* **Masquage intelligent(Introduit dans Cura 4.2)** * Cela permet de placer le joint sur un coin, comme pour "Masquer ou exposer jointure", mais les coins intérieurs sont choisis plus souvent que les coins extérieurs si des coins intérieurs sont disponibles dans le contour. S'il n'y a pas de coins intérieurs, on choisira un coin extérieur.
