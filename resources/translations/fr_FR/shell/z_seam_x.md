X Jointure en Z
====
Si l'emplacement de la couture est défini sur "Spécifié par l'utilisateur" dans le paramètre [Alignement de la jointure en Z](z_seam_type.md), la couture est placée près de l'emplacement spécifié avec les paramètres **X Jointure en Z** et [Y Jointure en Z](z_seam_y.md).

![La couture est située sur le côté gauche](../../../articles/images/z_seam_x_left.png)
![La couture est située sur le côté droit](../../../articles/images/z_seam_x_right.png)

Ce paramètre indique une position absolue sur le plateau d'impression si [Relatif à la jointure en Z](z_seam_relative.md) est désactivé, ou une position relative au centre du modèle si l'option [Relatif à la jointure en Z](z_seam_relative.md) est activé. Lorsque la position est absolue, la coordonnée se trouve dans le système de coordonnées g-code, qui est différent des coordonnées que Cura indique pour le placement des objets.

Il est utile de choisir un emplacement pour la couture qui soit à peine visible dans l'application de votre impression. Si un tel emplacement n'est pas disponible ou si un post-traitement peut être effectué après l'impression, vous pouvez choisir de placer la couture à un endroit où elle peut être facilement coupée au couteau ou poncée.
