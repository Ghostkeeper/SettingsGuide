Séquence d'impression
====
Lorsque plusieurs modèles sont placés sur le plateau d'impression, cela détermine l'ordre dans lequel les couches de ces objets sont imprimées. Il existe deux options :

Tout en même temps
----
Tous les objets seront imprimés en même temps, ce qui signifie que les couches seront imprimées de bas en haut pour tous les objets en même temps. On imprimera une couche de chaque objet avant de passer à la couche suivante.

Cela présente deux avantages majeurs :
* La couche précédente a plus de temps pour refroidir, ce qui permet d'obtenir une meilleure qualité lors de l'impression de petits objets.
* Le volume complet peut être utilisé pour votre impression.

Un à la fois
----
Les objets seront imprimés un par un, ce qui signifie qu'il imprimera toutes les couches d'un objet, puis retournera au plateau d'impression pour imprimer l'objet suivant.

Les principaux avantages de ce mode sont les suivants :
* Si l'impression échoue pour une raison quelconque, tous les objets qui ont été terminés avant l'échec sont tout à fait utilisables.
* Moins de déplacements sont nécessaires pour passer d'un modèle à l'autre. Cela permet de gagner un peu de temps d'impression et de réduire le nombre de cicatrices sur la surface où la buse est sortie et est entrée dans l'objet.

Ce mode est toutefois assorti de quelques contraintes, afin d'éviter que la tête et le portique n'entrent en collision avec le modèle.
* Vous ne pouvez pas imprimer d'objets plus hauts que la hauteur du portique de votre imprimante. La hauteur du portique peut être ajustée dans la boîte de dialogue des paramètres machine de l'imprimante. Cette hauteur de portique indique la distance verticale entre la pointe de la buse et le système qui porte la tête d'impression. La raison de cette limitation est que la tête d'impression devra descendre jusqu'à la plaque de construction pour imprimer le deuxième objet. Cela signifie que le premier objet peut être touché par le portique lorsque le deuxième objet est imprimé. En théorie, le dernier objet imprimé peut être autorisé à être plus haut que le portique, mais pour simplifier, Cura ne l'autorisera pas de toute façon.
* Les objets doivent être plus éloignés les uns des autres, afin d'éviter que la tête d'impression ne heurte les modèles précédemment imprimés sur le côté.
* L'ordre dans lequel les objets sont imprimés est fixe et optimisé afin de permettre aux objets d'être imprimés plus près les uns des autres. Si votre tête d'impression n'est pas symétrique, cela peut permettre de gagner beaucoup de place sur la plaque de construction.

**Un à la fois n'est disponible qu'en extrusion simple. Si vous utilisez une imprimante multi-extrusion, vous devez désactiver toutes les extrudeuses sauf une pour que ce paramètre apparaisse.**

