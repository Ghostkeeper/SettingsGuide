Ordre monotone de la surface supérieure
====
Normalement, Cura ordonne les lignes de telle sorte que la distance de déplacement entre elles soit faible. Si ce paramètre est activé, il ordonnera les lignes de la surface supérieure de telle sorte que les lignes adjacentes soient toujours imprimées en se chevauchant dans la même direction.

Lors de l'impression des lignes de la surface supérieure, les lignes se chevauchent généralement un peu avec les lignes voisines, car la forme d'une ligne n'est pas un rectangle parfait. Ce chevauchement donne aux lignes une légère inclinaison, ce qui fait qu'elles réfléchissent la lumière différemment dans différentes directions. Si les lignes adjacentes se chevauchent différemment, cette réflexion change. Vous pouvez le voir dans le résultat final. Il donne à différentes zones de la surface une brillance différente. L'impression dans un ordre monotone garantit que le chevauchement est le même sur toute la surface, de sorte qu'il n'y a pas de différence dans la façon dont elle reflète la lumière. La surface paraît ainsi plus homogène et plus lisse.

<!--screenshot {
"image_path": "skin_monotonic_disabled.gif",
"models": [
    {
        "script": "yen.scad",
        "transformation": ["scale(0.5)"]
    }
],
"camera_position": [0, 0, 130],
"settings": {
    "wall_line_count": 1,
    "skin_outline_count": 0,
    "skin_monotonic": false
},
"layer": 1,
"line": [29, 45, 61, 77, 93, 109, 125, 141, 157, 161, 177, 193, 199, 211, 231, 246, 262, 280, 296, 312, 326, 342, 358, 374, 397, 417, 433, 449, 464, 480, 499],
"delay": 125,
"colours": 32
}-->
<!--screenshot {
"image_path": "skin_monotonic_enabled.gif",
"models": [
    {
        "script": "yen.scad",
        "transformation": ["scale(0.5)"]
    }
],
"camera_position": [0, 0, 130],
"settings": {
    "wall_line_count": 1,
    "skin_outline_count": 0,
    "skin_monotonic": true
},
"layer": 1,
"line": [31, 47, 63, 77, 93, 109, 115, 131, 147, 163, 181, 197, 213, 229, 244, 263, 281, 296, 319, 340, 356, 372, 379, 395, 411, 427, 443, 459, 475, 491, 507, 511],
"delay": 125,
"colours": 32
}-->
![Ordre non monotone](../../../articles/images/skin_monotonic_disabled.gif)
![Ordre monotone, toujours à partir du coin inférieur droit](../../../articles/images/skin_monotonic_enabled.gif)

L'ordre monote augmente légèrement la longueur des déplacements, mais cet effet est très minime. Il n'a qu'un effet visuel sur l'impression. L'ordre monote ne présente aucun avantage mécanique.

Pour obtenir une surface lisse, envisagez de combiner ce paramètre avec le paramètre [Mode de détours](../travel/retraction_combing.md) pour éviter les peaux, et peut-être d'activer la [Hauteur du décalage en Z](../travel/retraction_hop.md). Vous pouvez également activer l'[étirage](../top_bottom/ironing_enabled.md), mais cela annule complètement l'utilité de ce paramètre. L'étirage a sa propre [option monotone](../top_bottom/ironing_monotonic.md).
