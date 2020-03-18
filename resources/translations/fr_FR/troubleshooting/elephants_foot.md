Le pied d'éléphant
===

Parfois, la face inférieure de l'empreinte est légèrement plus large que le reste de l'empreinte, ce qui donne une petite lèvre à cet endroit. C'est ce qu'on appelle une "patte d'éléphant", car elle ressemble aux pattes d'un éléphant dont les orteils sont légèrement plus larges que le reste de la patte.

Il existe plusieurs effets que les gens appellent "pied d'éléphant", dont les causes inhérentes sont complètement différentes. Ces effets nécessitent également des solutions complètement différentes. Cet article vous aidera à trouver la cause première.

![Pieds d'éléphant causés par la force des couches de la peau](../../../articles/images/elephants_foot.jpg)

Brim
----
Parfois, la patte de l'éléphant n'est en fait qu'une partie du bord qui n'a pas été enlevée correctement. Si vous avez arraché le rebord à la main, vous pouvez le dire parce que la ligne du rebord est complètement adjacente à la ligne normale du mur, et la ligne normale du mur est directement sous le reste du mur. Pour enlever complètement le bord, il est préférable d'utiliser un couteau bien aiguisé pour graver le bas de votre empreinte.

Si le modèle n'a pas un grand côté inférieur, envisagez plutôt de définir la [méthode d'adhésion](../platform_adhesion/adhesion_type.md) sur une jupe. Si cela pose trop de problèmes d'adhérence au lit, vous pouvez essayer d'autres méthodes pour améliorer l'adhérence, par exemple en réglant la [méthode d'adhérence de la couche initiale du fond](../shell/top_bottom_pattern_0.md) sur "concentrique".

Gauchissement
----
La cause la plus fréquente de la patte d'un éléphant est peut-être le gauchissement. Lorsque le matériau se refroidit, il rétrécit un peu. La matière de la ou des couches inférieures ne peut parfois pas se rétracter. Elles conservent leur taille d'origine, mais les couches supérieures se rétractent un peu. Plusieurs raisons peuvent expliquer pourquoi les couches inférieures ne peuvent pas se rétracter :
* Elle est collée à la plaque de construction, qui ne rétrécit pas.
* Elle est chauffée par la plaque de montage, ce qui l'empêche de rétrécir.
* Il y a de la peau à côté, ce qui bloque le rétrécissement. (Sur les couches supérieures, il peut y avoir du remblaiement à la place).

Pour éviter le gauchissement, jetez un coup d'œil à l'[article de dépannage](warping.md) à ce sujet. Pour ce type de déformation, voici quelques exemples de ce que vous pouvez essayer :
* Augmenter l'[épaisseur de la paroi](../shell/wall_thickness.md) pour empêcher les parois à côté du remplissage de rétrécir.
* Réduire la [température de la plaque de construction](../material/material_bed_temperature.md) pour permettre à la première couche de se rétracter autant que les autres couches. Si la température du lit était très élevée, cela peut aussi permettre au matériau de s'affaisser un peu, ce qui le rend plus large au fond. Cet effet est généralement faible, mais il sera également évité en réduisant la température du lit.
* Augmenter l'[épaisseur du fond](../shell/bottom_thickness.md) pour passer plus progressivement à une taille plus réduite. Vous pouvez même envisager d'imprimer le modèle de façon complètement solide (de préférence en fixant l'épaisseur du fond à un niveau extrêmement élevé) pour éliminer complètement la différence de rétrécissement.

Ajustement des plaques de construction
----
La patte d'éléphant peut également être causée par le fait que la plaque de montage est trop proche de la buse alors que la première couche est imprimée. Cela entraîne une surextrusion, qui pousse la première couche vers l'extérieur.

Pour ajuster la plaque de montage, consultez le manuel de votre imprimante 3D. La plupart des imprimantes sont équipées de vis de réglage dans le lit ou le portique pour ajuster la différence de hauteur de la plaque de montage pendant la première couche. Ajustez la plaque de montage pendant l'impression (de préférence pendant le bord, la jupe ou le radeau) jusqu'à ce que la première couche soit bien lisse et pas plus fine que les autres.

Vous pouvez également ajuster directement le [flux dans la première couche](../material/material_flow_layer_0.md) dans Cura pour compenser toute surextrusion. Une autre solution consiste à réduire la [Largeur de la ligne de la couche initiale](../resolution/initial_layer_line_width_factor.md) pour normaliser suffisamment l'extrusion afin d'éviter la patte d'éléphant.

Solutions générales
----
Voici quelques solutions que vous pouvez essayer pour vous débarrasser de n'importe quel type de patte d'éléphant, quelle que soit sa cause :
* L'utilisation d'un [radeau](../platform_adhesion/adhesion_type.md) permet de déplacer toute l'empreinte de la plaque de montage, ce qui évite les effets causés par la plaque de montage tels que sa température et le fait qu'elle colle trop à la plaque de montage, et évite également d'avoir à la couper.
* Réduire l'[Expansion horizontale de la couche initiale](../shell/xy_offset_layer_0.md) (éventuellement à quelque chose de négatif). Cela permet de compenser le pied de l'éléphant dans la première couche.
