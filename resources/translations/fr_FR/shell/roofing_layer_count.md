Une partie du haut de l'impression peut être séparée et imprimée avec différents paramètres. Ce paramètre détermine la taille de la partie à séparer. Combien de couches de la partie supérieure de l'impression obtiendront des paramètres différents ?

![La couche supérieure est imprimée plus lentement (bleu) que le reste de la peau (vert)](../../../articles/images/roofing_layer_count.png)

Certains réglages peuvent améliorer considérablement la qualité de la surface supérieure de l'impression, mais ils peuvent rendre l'impression beaucoup plus longue car ils sont appliqués sur toutes les couches de la peau en haut. Un effet similaire peut être obtenu en réglant ces paramètres uniquement pour la ou les deux couches supérieures, mais en imprimant plus rapidement le reste des couches de la peau. Cela n'aura alors pas un effet négatif aussi important sur le temps d'impression.

Les paramètres qui peuvent être ajustés pour la surface supérieure sont les suivants :
* [Top Surface Skin Extruder](roofing_extruder_nr.md)
* [Débit de la peau de la surface supérieure](../material/roofing_material_flow.md)
* [Vitesse de la peau en surface](../speed/speed_roofing.md)
* [Accélération de la couche supérieure de la peau](../speed/acceleration_roofing.md)
* [secousse de la peau supérieure](../speed/jerk_roofing.md)
* [Largeur de la ligne de la surface supérieure](../experimental/roofing_line_width.md)
* [Top Surface Skin Pattern](../experimental/roofing_pattern.md)
* [Directions de la ligne de la surface supérieure de la peau](../experimental/roofing_angles.md)

Pour obtenir une surface supérieure plus agréable, essayez de réduire la vitesse et d'augmenter la secousse.

Lorsque vous imprimez la surface supérieure dans une couleur différente (en utilisant le paramètre [Top Surface Skin Extruder](roofing_extruder_nr.md)), il est souvent nécessaire d'imprimer plus d'une couche dans l'autre couleur. Sinon, la couleur d'origine sera toujours perdue.
