Le pied d'éléphant
====
Parfois, la face inférieure de l'empreinte est légèrement plus large que le reste de l'empreinte, ce qui donne une petite lèvre à cet endroit. C'est ce qu'on appelle un "pied d'éléphant", car elle ressemble aux pattes d'un éléphant dont les orteils sont légèrement plus larges que le reste de la patte.

Il existe plusieurs effets que les gens appellent "pied d'éléphant", dont les causes inhérentes sont complètement différentes. Ces effets nécessitent également des solutions complètement différentes. Cet article vous aidera à trouver la cause première.

![Pieds d'éléphant causés par la force des couches de la peau](../../../articles/images/elephants_foot.jpg)

Bordure
----
Parfois, la patte de l'éléphant n'est en fait qu'une partie de la bordure qui n'a pas été enlevée correctement. Si vous avez arraché la bordure à la main, vous pouvez le voir parce que la ligne du rebord est complètement adjacente à la ligne normale de la paroi, et la ligne normale de la paroi est directement sous le reste de la paroi. Pour enlever complètement le bord, il est préférable d'utiliser un couteau bien aiguisé pour ébavurer le bas de votre empreinte.

Si le modèle n'a pas un grand côté inférieur, envisagez plutôt de définir le [type d'adhérence](../platform_adhesion/adhesion_type.md) sur une jupe. Si cela pose trop de problèmes d'adhérence au lit, vous pouvez essayer d'autres méthodes pour améliorer l'adhérence, par exemple en réglant la [méthode d'adhérence de la couche initiale du fond](../top_bottom/top_bottom_pattern_0.md) sur "concentrique".

Gauchissement
----
La cause la plus fréquente de la patte d'un éléphant est souvent le gauchissement. Lorsque le matériau se refroidit, il rétrécit un peu. La matière de la ou des couches inférieures ne peut parfois pas se rétracter. Elles conservent leur taille d'origine, mais les couches supérieures se rétractent un peu. Plusieurs raisons peuvent expliquer pourquoi les couches inférieures ne peuvent pas se rétracter :
* Elle est collée au plateau d'impression, qui ne rétrécit pas.
* Elle est chauffée par le plateau d'impressio, ce qui l'empêche de rétrécir.
* Il y a de la peau à côté, ce qui bloque le rétrécissement. (Sur les couches supérieures, il peut y avoir du remplissage à la place).

Pour éviter le gauchissement, jetez un coup d'œil à l'[article de dépannage](warping.md) à ce sujet. Pour ce type de déformation, voici quelques exemples de ce que vous pouvez essayer :
* Augmenter l'[épaisseur de la paroi](../shell/wall_thickness.md) pour empêcher les parois à côté du remplissage de rétrécir.
* Réduire la [température de la plaque de construction](../material/material_bed_temperature.md) pour permettre à la première couche de se rétracter autant que les autres couches. Si la température du lit était très élevée, cela peut aussi permettre au matériau de s'affaisser un peu, ce qui le rend plus large au fond. Cet effet est généralement faible, mais il sera également évité en réduisant la température du lit.
* Augmenter l'[épaisseur du fond](../top_bottom/bottom_thickness.md) pour passer plus progressivement à une taille plus réduite. Vous pouvez même envisager d'imprimer le modèle de façon complètement solide (de préférence en fixant l'épaisseur du fond à un niveau extrêmement élevé) pour éliminer complètement la différence de rétrécissement.

Ajustement du plateau d'impression 
----
La patte d'éléphant peut également être causée par le fait que le plateau d'impression est trop proche de la buse alors que la première couche est imprimée. Cela entraîne une surextrusion, qui pousse la première couche vers l'extérieur.

Pour ajuster la plaque de montage, consultez le manuel de votre imprimante 3D. La plupart des imprimantes sont équipées de vis de réglage pour le plateau d'impression ou sur le portique pour ajuster la différence de hauteur du plateau d'impression pendant la première couche. Ajustez la plaque le plateau d'impression pendant l'impression (de préférence pendant la réalisation de la bordure, de la jupe ou du radeau) jusqu'à ce que la première couche soit bien lisse et pas plus fine que les autres.

Vous pouvez également ajuster directement le [Débit de la première couche](../material/material_flow_layer_0.md) dans Cura pour compenser toute surextrusion. Une autre solution consiste à réduire la [Largeur de la ligne de la couche initiale](../resolution/initial_layer_line_width_factor.md) pour normaliser suffisamment l'extrusion afin d'éviter la patte d'éléphant.

Déformation au-dessus de la transition vitreuse
----
Dans le cas de très petits pièces, il est possible que la couche précédente ne se soit pas encore solidifiée lorsque la couche suivante est imprimée par-dessus. La matière est expulsée avec une force considérable par la buse, donc si la couche précédente n'est pas encore solidifiée, cette couche sera écrasée et se dilatera horizontalement. Cela se manifeste sous la forme d'une patte d'éléphant. La solution consiste à s'assurer que la matière est solidifiée au moment où la couche suivante est poussée par-dessus. Essayez de régler les paramètres suivants :

* Réduisez la [température d’impression couche initiale](../material/material_print_temperature_layer_0.md), afin que le matériau n'ait pas à refroidir autant.
* Réduire la [température du plateau couche initiale](../material/material_bed_temperature_layer_0.md), de sorte que la première couche se refroidisse plus rapidement, en envoyant plus de chaleur au plateau d'impressione. Les plastiques pour l'impression 3D sont conçus pour se solidifier très rapidement à un point de température précis, sa [température de transition vitreuse](https://en.wikipedia.org/wiki/Glass_transition#Transition_temperature_Tg). Pour éviter toute déformation, consultez la température de transition vitreuse de votre filament dans sa fiche technique, et assurez-vous que la température du plateau ne dépasse pas trop cette température de transition.
* Augmentez la [vitesse des ventilateurs initiale](../cooling/cool_fan_speed_0.md), pour refroidir le matériau plus rapidement. Envisagez également d'augmenter le paramètre [Vitesse régulière du ventilateur à la hauteur](../cooling/cool_fan_full_at_height.md), pour continuer à refroidir les premières couches.
* Réduire la [vitesse de la couche initiale](../speed/speed_layer_0.md). Cela permet de laisser plus de temps à la première couche pour refroidir après l'impression.
* Augmenter la [Durée minimale d’une couche](../cooling/cool_min_layer_time.md). Le but est de garantir un certain temps de refroidissement pour chaque couche avant que la couche suivante ne soit placée par-dessus, et d'utiliser la [vitesse maximale du ventilateur](../cooling/cool_fan_speed_max.md). Il s'agit en fait d'un moyen plus simple de combiner les ajustements de la vitesse de la couche initiale et de la vitesse du ventilateur énumérés ci-dessus. Gardez à l'esprit que cela s'applique à l'ensemble de l'impression cependant, et pas seulement à la première couche.

Solutions générales
----
Voici quelques solutions que vous pouvez essayer pour vous débarrasser de n'importe quel type de patte d'éléphant, quelle que soit sa cause :
* L'utilisation d'un [radeau](../platform_adhesion/adhesion_type.md) permet de déplacer toute l'empreinte du plateau d'impression, ce qui évite les effets causés par le plateau d'impression tels que sa température et le fait qu'elle colle trop au plateau d'impression, et évite également d'avoir à la décoller.
* Réduire l'[Expansion horizontale de la couche initiale](../shell/xy_offset_layer_0.md) (avec une valeur négative). Cela permet de compenser le pied de l'éléphant dans la première couche.
