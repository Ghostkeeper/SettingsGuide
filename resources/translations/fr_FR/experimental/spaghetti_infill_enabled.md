Si ce paramètre est activé, Cura extrudera tout le remplissage de plusieurs couches à la fois dans une couche supérieure. Ceci constitue une forme extrême de [Infill Layer Thickness](../infill/infill_sparse_thickness.md), mais sans le but de maintenir la rigidité du remplissage. Il possède une certaine fonctionnalité pour faire face aux quantités extrêmes d'extrusion.

Cette caractéristique n'est pas fonctionnelle pour les matériaux ordinaires. Vous voudrez normalement soit la résistance des motifs de remplissage ordinaires, soit ne pas tenir compte du remplissage. Il existe cependant deux cas d'utilisation.

Cas d'utilisation
----
Avec des matériaux souples, cette technique peut produire des textures très douces. Les spaghettis de remplissage ont tendance à produire des anneaux mal placés qui n'adhèrent pas bien les uns aux autres. Ces anneaux sont également compacts dans toutes les directions. Pour obtenir cet effet, la densité de remplissage ne doit cependant pas être trop faible, sinon tous les spaghettis se retrouveront au fond de l'impression. Il est conseillé d'utiliser une [densité de flux](spaghetti_flow.md) comprise entre 30 et 60 %, en fonction de la largeur de la ligne et de la hauteur de la couche. Le résultat sera un remplissage qui sera également rigide dans toutes les directions et assez souple.

L'autre application du remplissage spaghetti est le moulage. Si vous avez une imprimante qui comprend un outil pour couler à des endroits spécifiques, cette fonction peut être utilisée pour remplir votre modèle de manière assez uniforme avec des dépôts de matériaux contrôlés. Si vous utilisez cette fonction, la [densité d'écoulement](spaghetti_flow.md) doit probablement être d'environ 100 %, en fonction du ratio de contraction/dilatation du matériau coulé.

Réglage d'autres paramètres pour le remplissage de spaghetti
----
Ces deux demandes nécessitent un traitement très particulier de votre demande de remplissage. Voici quelques paramètres que vous voudrez très probablement adapter à vos besoins :
* La [vitesse d'impression du remplissage](../speed/speed_infill.md) doit être massivement réduite. Si la buse doit extruder le matériau de remplissage de 10 couches en même temps, vous devrez réduire la vitesse d'impression d'au moins un facteur 8.
* Réglez votre [épaisseur de la couche de remplissage] (../infill/infill_sparse_thickness.md) pour qu'elle soit égale à la hauteur de la couche.
* Augmentez légèrement votre [température d'impression](../material/material_print_temperature.md) (pour l'extrudeuse qui imprimera le remplissage). Cela permet au matériau de s'écouler correctement hors de la buse et permet une extrusion plus rapide.
* Définissez le [alignement du joint](../shell/z_seam_type.md) de manière aléatoire pour étaler la structure de manière aléatoire.

**Dans la vue en couches de Cura, le remplissage apparaîtra sous forme de lignes très épaisses. C'est parce que Cura suppose que le matériau reste sur la même couche et s'y étale. En réalité, il va tomber.

**Lorsqu'un remplissage de spaghetti est utilisé, le paramètre [infill line width](../resolution/infill_line_width.md) n'a plus d'effet. La largeur de la ligne est ajustée pour répondre aux besoins des paramètres [distance de la ligne de remplissage](../remplissement/distance_ligne_de_remplissage.md) et [débit des spaghettis](débit_des spaghettis.md).**


