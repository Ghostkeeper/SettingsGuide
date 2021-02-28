Essuyer le bec d'impression inactif sur la tour d'amorçage
====
Si cette fonction est activée, l'imprimante essuie la buse précédente après avoir amorcé la suivante dans la tour d'amorçage.

L'ordre des événements sera le suivant si cette option est activée :
1. L'imprimante passe à la nouvelle extrudeuse.
2. La nouvelle extrudeuse est amorcée par l'impression d'une tour d'amorçage.
3. La buse qui était active avant le passage à l'extrudeuse est essuyée sur la tour d'amorçage.
4. L'imprimeur continue d'imprimer la pièce avec la nouvelle extrudeuse.

Notez que l'imprimante essuie alors la buse qui était active avant la mise en marche de l'extrudeuse, et non la buse actuellement active. Si votre imprimante possède plusieurs buses avec une certaine distance entre elles, vous pouvez voir un déplacement en vue de la couche qui semble inutile. En effet, le mouvement vers cet endroit fait que la buse précédente se déplace au-dessus de la tour d'amorçage (qui n'est pas représentée en vue en couches).

Lorsqu'une buse est mise en veille, elle reste encore assez chaude pendant un certain temps. Pendant qu'elle est chaude, certains matériaux ont tendance à suinter. En amorçant la buse suivante dans la tour d'amorçage, elle aura eu la chance de refroidir un peu, ce qui aura permis de ralentir le suintement. Ce réglage permet d'essuyer le suintement qui s'est écoulé au milieu de la tour d'amorçage, afin qu'il ne se retrouve pas sur le côté de votre modèle imprimé.
