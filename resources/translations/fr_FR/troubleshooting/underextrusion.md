Sous-extrusion
===

L'un des problèmes les plus courants de l'impression en 3D est que l'imprimante n'extrude pas assez de matière pour produire un bel objet solide. Lorsque cela se produit, on parle de "sous-extrusion" : La buse extrude moins de matière que prévu.

![Un cas extrême de sous-extrusion, où l'on peut même voir l'intérieur de l'objet](../../../articles/images/underextrusion.jpg)

La sous-extrusion peut également se manifester de nombreuses manières. Dans le cas le plus extrême, l'objet est très fragile et ses parties intérieures sont visibles à travers la surface. Parfois, on le voit en raison de la largeur trop faible des lignes, de sorte qu'elles ne se relient pas aux lignes adjacentes. Parfois, il se manifeste seulement par de petits trous dans la surface supérieure ou de minuscules fractures dans les parois.

Il existe une multitude de causes possibles de sous-extrusion, ce qui rend le dépannage très difficile. Le reste de cet article décrit quelques-unes des causes les plus probables et la manière d'y remédier.

Buse bouchée
----
Si votre imprimante imprimait auparavant très bien, et qu'elle présente soudain une sous-extrusion sans modification significative de l'objet imprimé ou des paramètres, il est probable que le problème se situe quelque part dans le train de l'extrudeuse. En général, le maillon le plus faible est la buse.

Les buses bouchées sont un phénomène courant avec toute imprimante 3D. Cela peut se produire lorsque le filament est contaminé par des éléments qui ne fondent pas bien et est poussé dans la buse. Cela peut également se produire lorsque le filament lui-même est brûlé dans la buse. Cela peut se produire lorsque le plastique est chauffé trop fort ou maintenu à une température élevée pendant trop longtemps. Le matériau se dégrade, les polymères se cristallisent et vous vous retrouvez avec un morceau de plastique dur qui ne fond pas dans la buse. Pour y remédier, vous devez retirer les débris de la buse.

Il existe plusieurs techniques pour extraire les débris de la buse. Si vous avez une aiguille d'acupuncture ou une autre broche métallique fine, vous pouvez la pousser par le bas. Cependant, la technique la plus courante est connue sous le nom de "Atomic Pull". Pour exécuter cette technique, prenez un morceau de filament d'au moins 50 cm de long, de préférence en un matériau à point de fusion élevé. Chauffez la buse jusqu'au point de fusion de ce filament (par exemple 190°C pour le PLA), puis poussez le filament à l'intérieur avec une pince jusqu'à ce qu'une certaine matière sorte de la buse. Ensuite, laissez la buse refroidir jusqu'à sa température de transition vitreuse (par exemple 60°C pour le PLA), tout en poussant le filament vers le bas dans la buse. Juste avant que la température de transition vitreuse ne soit atteinte, tirez rapidement sur le filament pour le faire sortir. Si l'extrémité du filament est sale avec du plastique noirci, coupez l'extrémité et essayez à nouveau jusqu'à ce qu'elle soit propre. Essayez à nouveau d'imprimer quelque chose et, avec un peu de chance, il s'extrude mieux maintenant.

Glissement de l'extrudeur
----
Parfois, l'extrudeur n'a pas assez de prise sur le filament pour le pousser assez fort vers le bas à travers la buse. Pendant l'impression, on peut alors entendre le filament glisser périodiquement, avec un léger claquement toutes les quelques secondes. C'est le dispositif d'alimentation qui essaie de pousser le filament vers l'intérieur, mais le filament glisse à nouveau de temps en temps.

La plupart des feeders ont des points de réglage pour ajuster la force qu'ils exercent sur le filament. Essayez de régler le distributeur un peu plus serré sur le filament. Si l'alimentateur pousse trop fort sur le filament, il peut le casser ou causer trop de friction et commencer à le broyer. S'il est trop lâche, vous constaterez souvent une sous-extrusion.

Diamètre du filament non uniforme
----
Si la plupart des filaments sont fins, il arrive parfois qu'un lot soit produit alors que le filament est juste un peu trop fin. Cela peut avoir de grandes conséquences sur la quantité d'extrusion dans votre impression. Les filaments moins chers sont souvent plus susceptibles de présenter ce problème. Vous pouvez utiliser un pied à coulisse pour mesurer le diamètre réel de votre filament. Assurez-vous de mesurer à plusieurs endroits différents sur la longueur du filament, et ne mesurez pas l'endroit où le chargeur a broyé le filament.

Si le diamètre du filament est trop éloigné (une différence 50μm commence à être visible sur l'impression), vous pouvez alors ajuster le diamètre de votre filament dans le gestionnaire de matériel. Si vous utilisez un matériau intégré de Cura, vous devrez dupliquer ce matériau avant de le modifier. Cura compensera alors le nouveau diamètre en ajustant la vitesse du chargeur.

Fusion du matériau
----
Outre le fait que votre imprimante 3D soit en parfait état, les paramètres que vous utilisez pour imprimer doivent également correspondre aux propriétés du matériau que vous utilisez. Le plus important est la température d'impression.

Si la [température d'impression](../material/material_print_temperature.md) est trop basse, vous constaterez très rapidement une sous-extrusion. Si le matériau est trop froid, il sera très visqueux, ce qui le rendra plus difficile à sortir correctement de la buse. Combiné à une vitesse d'impression élevée, le matériau n'a pas le temps de fondre correctement et n'a pas non plus le temps de s'écouler en position. Certains matériaux, comme le PVA ou le nylon, ont tendance à absorber l'humidité de l'air. Cette humidité s'évapore lorsque le matériau est imprimé, ce qui refroidit le plastique. Pour compenser l'effet de l'humidité de l'air, il est nécessaire d'utiliser des matériaux de remplacement.

Faire circuler le matériel
----
Il y a toujours un certain temps de latence entre le moment où l'imprimante fait avancer le matériau et celui où elle commence effectivement à extruder. Cette latence peut entraîner une sous-extrusion si elle n'est pas prise en compte. Lorsque l'imprimante pousse le matériau vers l'avant, la pression dans la chambre de la buse augmente progressivement jusqu'à ce qu'elle soit suffisante pour pousser le matériau fondu vers l'extérieur à l'autre extrémité. Il peut s'écouler jusqu'à une seconde avant que le matériau n'atteigne son débit normal. Si l'imprimante est équipée d'un tube Bowden entre le chargeur et la buse, ce délai peut même être beaucoup plus important, dans le parc de billes de 10 secondes environ.

Lorsque l'imprimante doit commencer à extruder plus de matière qu'auparavant, elle alimentera la matière plus rapidement, mais il faudra un certain temps avant que celle-ci n'arrive à l'extrémité de la buse. Pendant ce temps, la buse essaiera de tracer une ligne, mais cette ligne sera sous-extrudée. Surtout lorsque l'impression est très détaillée, cela peut provoquer une sous-extrusion considérable.

Il y a deux réglages que vous pouvez faire pour remédier à cela : L'amorçage et le réglage de la vitesse.

L'amorçage consiste à pousser un peu de matériau avant que la partie importante de l'impression ne commence. Souvent, cela est fait au début d'une impression dans une routine séparée, en imprimant une petite ligne ou une goutte de plastique dans un coin de la plaque de construction. Vous pouvez également utiliser une [jupe ou un bord](../platform_adhesion/adhesion_type.md), qui imprimera un certain nombre de lignes autour de l'impression elle-même. Lorsque le matériau s'écoule correctement et que tout l'air est sorti de la chambre de la buse, il s'extrudera de manière plus uniforme.

Lorsque le matériau est rétracté, le flux de matériau est interrompu. Lorsque la matière est repoussée dans la buse, il peut s'écouler un certain temps avant qu'elle ne reprenne son flux. La réduction de la [vitesse à laquelle elle est repoussée](../travel/retraction_prime_speed.md) permet au matériau de mieux fondre avant d'être extrudé, ce qui aide un peu. Sinon, vous pouvez également essayer de pousser le matériau un peu plus loin qu'avant la rétraction en [amorçant un peu plus](../travel/retraction_extra_prime_amount.md) pour compenser la sous-extrusion. Le réglage est cependant très délicat.

Équilibrer les vitesses
----
Si vous constatez une sous-extrusion uniquement dans certaines structures de l'impression, comme le remplissage et le support, cherchez à égaliser davantage le débit dans votre impression. Il y a toujours un délai entre le moment où le margeur alimente le matériau et celui où ce matériau sort réellement de la buse. Si la vitesse d'impression est augmentée pendant une partie de l'impression, la tête d'impression accélère relativement vite, mais le flux de matériau reste à la traîne jusqu'à ce que la pression dans la chambre de la buse soit augmentée pour faire face à la vitesse d'extrusion plus élevée. Cela entraîne également une sous-extrusion. De même, en ralentissant la vitesse d'extrusion, il y a toujours une surextrusion.

Certains microprogrammes sont capables de compenser cet effet. Marlin possède une fonction appelée [Linear Advance] (http://marlinfw.org/docs/features/lin_advance.html) qui commence à augmenter la pression à l'intérieur de la chambre de la buse à l'avance afin qu'elle puisse sortir de la buse plus tôt. Sailfish a une [fonction similaire] (https://www.sailfishfirmware.com/doc/tuning-jkn-advance.html) qu'il appelle JKN Advance. Pour régler les paramètres de ces fonctions, regardez quel g-code vous devez écrire dans le g-code de départ.

Si ces fonctions sont indisponibles ou inefficaces, vous devrez vous assurer qu'il n'y a pas de changements soudains et importants du débit dans l'impression. [Réduisez l'épaisseur de la couche de remplissage](../infill/infill_sparse_thickness.md) et [l'épaisseur de la couche de support](../support/support_infill_sparse_thickness.md). Ces paramètres multiplient le taux d'extrusion pour obtenir une plus grande hauteur de couche.

Plus important encore, vous devez vous assurer que le remplissage, les parois intérieures, la paroi extérieure, la peau et le support sont imprimés avec un taux d'extrusion similaire. Le taux d'extrusion d'une ligne est le produit de sa largeur, de la hauteur de la couche, du débit et de la vitesse (moyenne). Multipliez ces quatre valeurs ensemble et assurez-vous que le résultat est approximativement le même pour le remplissage ([hauteur de la couche](../infill/infill_sparse_thickness.md), [largeur de la ligne](../resolution/infill_line_width.md), [débit de remplissage](../material/infill_material_flow.md) et [speed](../speed/speed_infill.md)), peau ([line width](../resolution/skin_line_width.md), [débit du dessus/dessous](../material/skin_material_flow.md) et [speed](../speed/speed_topbottom.md)), paroi extérieure ([line width](../resolution/wall_line_width_0.md), [débit de paroi externe](../material/wall_0_material_flow.md) et [speed](../speed/speed_wall_0.md)), paroi intérieure ([Largeur de ligne de la (des) paroi(s) interne(s)](../resolution/wall_line_width_x.md), [flow](../material/wall_x_material_flow.md) et [vitesse](../speed/speed_wall_x.md)) et support ([hauteur de la couche](../support/support_infill_sparse_thickness.md), [largeur de la ligne](../resolution/support_line_width.md), [débit](../material/support_material_flow.md) et [vitesse](../speed/speed_support.md)). Si [compensation du chevauchement des parois](../shell/travel_compensate_overlapping_walls_enabled.md), assurez-vous d'activer [égaliser le débit de filaments
](../speed/speed_equalize_flow_enabled.md) de sorte que la vitesse soit ajustée plutôt que le débit.

Limites de la buse
----
L'extrusion d'une trop grande quantité de matériau à travers une petite buse peut également provoquer une sous-extrusion. Lors de l'impression à grande hauteur de couche, largeur de ligne ou vitesse en utilisant une petite buse, le matériau ne pourra physiquement pas s'écouler hors de la buse à temps. L'augmentation de la température peut contribuer à rendre le matériau plus fluide jusqu'à un certain point, mais il y a toujours des limites à ce qu'une buse peut extruder. Au-delà de cette limite, il faut envisager d'acheter une buse plus grosse.

D'autre part, l'extrusion d'une quantité trop faible de matière peut également entraîner une sous-extrusion. Si la pression dans la chambre de la buse est très faible, la tension de surface du plastique liquide peut maintenir le matériau dans la chambre de la buse. Parfois, il sera poussé vers l'extérieur par une grosse gouttelette, laissant de l'air à d'autres endroits. Cela peut donner un effet similaire à la sous-extrusion.

Ajuster directement le débit
----
Si tout le reste échoue, Cura dispose également d'un réglage permettant d'ajuster directement le débit : [Débit](../material/material_flow.md). Cette méthode d'ajustement peut compenser un défaut inconnu quelque part dans le système.

Elle ne fonctionnera pas si l'on empêche physiquement la matière de s'écouler plus rapidement (par exemple, à cause d'une buse bouchée). Dans d'autres cas, elle provoquera probablement une surextrusion à certains endroits. Il s'agit cependant d'un moyen simple d'ajuster l'impression en fonction des besoins.
