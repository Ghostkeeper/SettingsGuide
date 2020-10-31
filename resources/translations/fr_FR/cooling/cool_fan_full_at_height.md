Vitesse régulière du ventilateur à la hauteur
=====

La vitesse du ventilateur commence à la valeur du paramètre [vitesse des ventilateurs initiale](cool_fan_speed_0.md) au début de l'impression. Pendant les premières couches de l'impression jusqu'à ce qu'elle atteigne la hauteur spécifiée dans ce paramètre, la vitesse du ventilateur sera progressivement augmentée jusqu'à la [vitesse régulière du ventilateur](cool_fan_speed_min.md).

![Quelle vitesse de ventilateur est utilisée où](../images/cool_fan_speed_fr.svg)

Normalement, la vitesse initiale du ventilateur est considérablement réduite car la couche initiale doit rester chaude pendant l'impression. Si la couche initiale refroidit, le matériau commence à [se déformer](../troubleshooting/warping.md). La première couche se décole alors du plateau d'impression, ce qui fait échouer l'impression. Cependant, si la deuxième couche refroidit trop rapidement, elle continuera à rétrécir et, par frottement de cisaillement, tirera la première couche vers le haut, ce qui décollera également l'impression. Le but de ce réglage est de permettre l'impression de plusieurs couches avec une vitesse de ventilation plus faible. De cette façon, le gauchissement peut être évité jusqu'à ce que l'impression ait une rigidité suffisante pour résister au gauchissement.

Le simple fait de réduire la vitesse du ventilateur pendant les premières couches créerait une variation brutale de la vitesse du ventilateur qui serait visible dans la qualité de la surface de l'impression finale. Cela crée un phénomène de bandes, visible sur l'impression. Au lieu de cela, la vitesse du ventilateur est progressivement modifiée pour atteindre la vitesse normale du ventilateur.

* L'augmentation de ce paramètre peut améliorer l'adhérence au plateau d'impression.
* Réduisez ce réglage si vous constatez des problèmes de pattes d'éléphant ou de suintement.
* Si votre plateau d'impression est chauffé à une température élevée, vous devrez peut-être réduire ce réglage afin d'éviter les pattes d'éléphant ou les suintements.
