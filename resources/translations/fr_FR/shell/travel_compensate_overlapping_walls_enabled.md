Compenser les chevauchements de paroi
====
Lors de l'impression de pièces fines, les parois opposées peuvent se rapprocher suffisamment pour se chevaucher. En imprimant les deux parois avec leur largeur de ligne normale, elles dépasseraient. Ce réglage permet d'éviter cette surextrusion en réduisant la largeur de l'une des lignes, ce qui permet d'éviter cette surextrusion et d'obtenir une meilleure précision dimensionnelle.

![Où la largeur de ligne est réduite](../images/travel_compensate_overlapping_walls_enabled_schematic_fr.svg)
![Toutes les lignes sont extrudées sur toute leur largeur, ce qui crée une partie trop large](../../../articles/images/travel_compensate_overlapping_walls_enabled_disabled.png)
![La moitié des lignes ont réduit leur largeur, ce qui permet une impression plus précise](../../../articles/images/travel_compensate_overlapping_walls_enabled_enabled.png)

La largeur de la ligne de la paroi qui chevauche une autre paroi est réduite par la zone de chevauchement. Cela permet de compenser la surextrusion.

Comme décrit ci-dessus, cette caractéristique tend à améliorer la précision dimensionnelle. Toutefois, l'inconvénient est que le débit devient moins régulier, ce qui entraîne une sous-extrusion à certains endroits et une sur-extrusion à d'autres. De plus, le débit peut être réduit en dessous du débit minimum de la buse et de l'extrudeuse, ce qui entraîne un flux et un bourrelet irréguliers. Pour réduire cet effet, vous pouvez définir le [Débit minimal de la paroi](wall_min_flow.md) qui transformera certaines des parois les plus fines en mouvements de translation au détriment de la précision dimensionnelle.

**Ce réglage a tendance à être plus désordonné en mode aperçu. Dans l'impression réel, il n'y a pas de frontières entre les lignes. La vue en couches ne montre que les chemins du G-Code, mais en réalité, le matériau est repoussé par l'autre paroi avec laquelle il chevauche. En outre, de minuscules réductions de débit ne seront pas perceptible pas dans l'impression réelle, car le débit à travers la buse ne peut pas s'ajuster aussi rapidement. Ces effets rendent l'impression plus lisse que ne le prévoit la vue en couches.**

