Epaisseur du support du bord de la peau
===

Lors de l'impression de formes concaves, il y aura une peau supérieure qui se terminera quelque part à mi-chemin du remplissage. Ce réglage ajoute une ligne supplémentaire à travers le remplissage pour soutenir le bord de la peau, de sorte qu'elle s'affaisse un peu moins.

![Un périmètre est tracé à travers le remplissage sous le bord de la peau](../../../articles/images/skin_edge_support_thickness.png)

Une seule ligne à travers les interstices du remplissage s'affaissera toujours, de sorte que la ligne peut être tracée sur plusieurs couches sous le bord de la peau qui a besoin d'être soutenue. Ce réglage permet de configurer l'épaisseur verticale de la ligne sous le bord de la peau. Vous pouvez également ajuster directement le [nombre de couches](skin_edge_support_layers.md) sous le bord de la peau où cette ligne sera tracée.

L'augmentation de cette épaisseur aura généralement les effets suivants sur l'impression :
* Le bord de la peau sera mieux supporté, ce qui rendra la face supérieure plus lisse, car la peau peut passer complètement d'un côté à l'autre.
* L'impression prend un peu plus de temps et utilise plus de matière.

Si le taux de remplissage est élevé, ce réglage n'aura pratiquement aucun effet sur la surface supérieure et pourrait provoquer une [surextrusion](../troubleshooting/overextrusion.md) dans le remplissage. Il est donc préférable de le laisser à 0 mm.
