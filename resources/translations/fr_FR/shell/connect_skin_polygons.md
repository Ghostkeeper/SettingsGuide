Relier les polygones supérieurs / inférieurs
===

Lorsque vous utilisez un motif concentrique haut/bas (un motif composé de contours fermés, également appelés polygones), connectez tous les contours entre eux de manière à ce qu'ils forment un seul chemin.

![Modèle concentrique naïf](../../../articles/images/connect_skin_polygons_original.png)
![Tous les contours sont connectés pour former une courbe](../../../articles/images/connect_skin_polygons_enabled.png)

Cela empêche la plupart des déplacements. Cependant, cela crée de nouveaux angles vifs où la buse devra accélérer et décélérer beaucoup, ce qui compensera le gain en temps d'impression. Le motif ondulé sera également visible à l'extérieur, ce qui donne un effet visuel intéressant.

Les contours créés par [Nombre supplémentaire de parois extérieures](./skin_outline_count.md) ne sont pas reliés.
