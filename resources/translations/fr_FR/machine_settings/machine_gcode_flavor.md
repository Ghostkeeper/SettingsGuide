Format G-code
====
Bien que le G-Code soit un format standardisé pour la communication des instructions aux machines à commande numérique telles que les imprimantes 3D, il existe encore quelques différences dans la manière dont les G-Codes sont pris en charge par chaque imprimante, dans leur état initial et parfois dans la manière dont ils interprètent les commandes. Avec le format G-Code, vous pouvez indiquer en grande partie quel ensemble de commandes votre imprimante accepte.

La différence entre ces formats de code g est généralement assez faible. Les commandes les plus importantes, comme le déplacement et le chauffage de la buse, sont généralement les mêmes.

Pour sélectionner le bon G-Code, reportez-vous à la documentation du microprogramme de votre imprimante. Elle devrait vous indiquer quelles fonctions sont prises en charge et lesquelles ne le sont pas. Il s'agit des formats disponibles dans Cura, et de leurs différences.

Marlin
----
Marlin est considéré comme le format par défaut du G-Code. Il est destiné au microprogramme principal [Marlin firmware](https://marlinfw.org/) qui est le microprogramme d'impression 3D le plus populaire et la base de la plupart des microprogrammes alternatifs disponibles sur le marché.

Marlin (Volumétrique)
----
C'est une variante du Marlin où les commandes d'extrusion spécifient la quantité d'extrusion en millimètres cubes, plutôt qu'en longueurs de filament. Ce sont les changements notables :
* Le paramètre "E" de la commande "G1" est calculé en millimètres cubes, le volume du plastique alimenté, plutôt que la longueur du filament à alimenter pendant ce mouvement.
* Les statistiques au début du code g mentionnent également le filament utilisé en millimètres cubes.

RepRap
----
Il s'agit d'un format axée sur le soutien aux imprimantes, qui sont issues du [projet RepRap](https://reprap.org/wiki/RepRap). Il comporte un certain nombre d'exceptions notables :
* Toujours mentionner l'extrudeuse lors du réglage de la température de la couche initiale, même s'il n'y a qu'une seule extrudeuse.
* Revenir à l'extrusion relative après l'impression.
* Changer les accélérations en utilisant les paramètres "P" et "T" de la commande "M204", pour respectivement l'accélération d'impression et l'accélération de déplacement, plutôt que le paramètre "S".
* Changer la jerk en utilisant la commande `M566`, plutôt que la commande `M205`.

Ultimaker 2
----
Ce format de G-Code est destiné à la famille Ultimaker 2. Le microprogramme de cette famille avait l'étrange idée de laisser l'imprimante contrôler les réglages liés au matériel plutôt que le trancheur. Ce sont les exceptions :
* Il n'y aura pas de commande de température d'impression dans le g-code.
* Il n'y aura pas de commande de température de la plaque d'impression dans le code g.
* Il n'y aura pas de commande de température de volume de construction dans le code g.
* La première buse est supposée avoir la [température d'impression de la couche initiale](../material/material_print_temperature_layer_0.md) lorsque l'impression commence.
* La plaque de montage est supposée avoir la [température de la plaque de montage de la couche initiale](../material/material_bed_temperature_layer_0.md) lorsque l'impression commence.
* Le paramètre "E" de la commande "G1" est calculé en millimètres cubes, le volume du plastique alimenté, plutôt que la longueur du filament à alimenter pendant ce mouvement.
* Les statistiques au début du code g mentionnent le filament utilisé en millimètres cubes.

Griffin
----
Il s'agit de la version G-Code des imprimantes Ultimaker modernes, l'Ultimaker 3 et les plus récentes. Ces imprimantes nécessitent un ensemble de métadonnées dans un certain format au début du G-Codee. Les différences dans ce format de G-Code sont les suivantes :
* Il y a un grand en-tête au début du g-code contenant des informations sur les métadonnées telles que la durée de l'impression, le nom du travail d'impression et quelques informations pratiques telles que la température de départ et le cadre de l'impression.
* Il n'y aura pas de commandes de température de volume de construction dans le G-Code.
* La première buse est supposée avoir la [température d'impression de la couche initiale](../material/material_print_temperature_layer_0.md) lorsque l'impression commence.
* La plaque de montage est supposée avoir la [température de la plaque de montage de la couche initiale](../material/material_bed_temperature_layer_0.md) lorsque l'impression commence.
* L'imprimante n'est pas supposée démarrer sur la première extrudeuse, donc elle passera toujours à l'extrudeuse de départ au début de l'impression en utilisant une commande `T`.
* Une goutte d'amorce est imprimée avec `G280` pour chaque extrudeuse lorsqu'elle commence l'impression, au lieu d'un retrait.

Makerbot
----
Il s'agit d'un format de G-Code destinée aux microprogrammes basés sur [Sailfish](https://www.sailfishfirmware.com/). Ce microprogramme est utilisé dans la génération des imprimantes Makerbot originales. Quelques différences notables sont à noter :
* Lors de la modification de la température d'impression, "M109" (réglage de la température et attente) n'est pas pris en charge. Il produit à la place `M104`, qui n'attend pas que la température soit atteinte. Il utilise ensuite `M116` pour commander à l'imprimante d'attendre que cette température soit atteinte.
* La dimension "E" de la commande d'extrusion "G1" n'est pas réinitialisée pendant l'impression. Pour les autres saveurs, ce paramètre est réinitialisé tous les 10 mètres de filament par une commande `G92 E0`, pour éviter les erreurs d'arrondi en virgule flottante dans le firmware, mais pas avec celui-ci.
* Le changement d'extrudeuse se fait avec la commande `M135` plutôt qu'avec les commandes `T`.
* La vitesse du ventilateur n'est pas sortie. Le ventilateur est soit complètement en marche, soit éteint. Cura commandera à l'imprimante de mettre en marche le ventilateur si elle souhaite une vitesse de 50% ou plus.

Bits from Bytes
----
Il s'agit d'une version G-Code destinée aux imprimantes Bits from Bytes qui disposaient de leur propre microprogramme personnalisé. Leur format de G-Code diffère considérablement des autres. Ce sont les changements que Cura va apporter :
* Les quantités d'extrusion sont écrites en utilisant le RPM du chargeur plutôt que le paramètre "E".
* Les rétractions sont écrites avec "M101" ou "M201", selon l'extrudeuse active.
* La vitesse de rétraction est écrite avec une commande séparée `M108`.
* Les déplacements sont indiqués par une commande `M103`, au lieu de remplacer `G1` par `G0`. Il n'y aura pas de commande "G0".
* L'imprimante est configurée pour utiliser la rétraction automatique en utilisant la commande "M227".
* Cura produira des nouvelles lignes de style Windows avec un retour chariot devant, plutôt qu'un simple symbole de nouvelle ligne.
* La dimension "E" de la commande d'extrusion "G1" n'est pas réinitialisée pendant l'impression. Pour les autres saveurs, ce paramètre est réinitialisé tous les 10 mètres de filament par une commande `G92 E0`, pour éviter les erreurs d'arrondi en virgule flottante dans le firmware, mais pas avec celui-ci.

Mach3
----
C'est un format de G-Code qui se rapproche de la façon dont les machines CNC attendent le G-Codeu Il n'y a qu'une seule différence notable :
* Les quantités d'extrusion sont écrites en utilisant le paramètre "A" de la commande "G1", plutôt que le paramètre "E".

Repetier
----
Il s'agit d'un format G-Code destinée aux imprimantes 3D de Repetier. Il imite la sortie du trancheur Repetier. Ce sont les différences notables avec ce format G-Code :
* Si les rétractions du micrologiciel sont activées, les rétractions pour un commutateur d'extrudeuse utilisent "G10 S1" pour indiquer qu'il s'agit d'une rétraction pour un commutateur d'extrudeuse.
* Les changements d'accélération sont effectués en utilisant les commandes "M201" et "M202" (pour respectivement imprimer l'accélération et l'accélération de déplacement) plutôt que "M204".
* Les changements d'accélération sont effectués à l'aide de la commande "M207" plutôt que de la commande "M205".

*Comme il s'agit d'un réglage machine, il ne sera normalement pas listé dans la liste normale des réglages. Il existe cependant un menu de sélection pour ce paramètre dans la boîte de dialogue des paramètres de l'imprimante, qui peut être trouvé dans la liste des imprimantes ajoutées dans la boîte de dialogue des préférences.*
