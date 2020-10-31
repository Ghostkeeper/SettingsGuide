Glossaire
===

Cette page explique certains des termes utilisés par Cura dans l'industrie. Cura n'est pas toujours le plus cohérent dans l'utilisation de la terminologie, certains termes sont donc des synonymes.
* **Couches adaptatives :** (Adaptive layers) Une technique qui fait varier la hauteur de la couche sur l'impression afin de réduire la visibilité de la topologie tout en imprimant assez rapidement.
* **Aliasing :** (Aliasing) Un défaut d'impression (Effet d'escalier) où la limite de résolution des moteurs pas à pas est visible sur l'extérieur de l'impression.
* **Maille anti-débordement :** (Anti-overhang mesh) Un modèle qui empêchera la génération d'un soutien pour soutenir tout dépassement avec lequel le modèle chevauche. Synonyme de "bloqueur de support".
* **Bourrelet :** (Bead) Un brin de matériau après avoir été déposé par le train de l'extrudeuse. Le terme "bourrelet" est utilisé en science où il est important de considérer la forme réelle du brin de filament après qu'il ait été solidifié. Semblable à "ligne".
* **Goutte :** (Blob) Un point d'excès de matière à l'extérieur de l'impression.
* **Tube Bowden :** (Bowden tube) Un tube creux et flexible utilisé pour guider le filament dans la ligne d'extrusion.
* **Pont :** (Bridging) Technique permettant d'imprimer des lignes en surplomb dans l'air, en étirant des lignes droites entre deux points d'appui. Cura peut ajuster les paramètres des lignes de pontage et ajustera la direction de certaines lignes pour créer des ponts.
* **Bordure :** (Brim) Une bordure de matériau, fixé à l'empreinte, qui agit comme une jupe mais fixe également mieux l'impression au plateau d'impression en offrant plus de surface pour que le matériau puisse adhérer.
* **Plateau d'impression :** (Build plate) La plaque sur laquelle l'impression est placée pendant sa construction. Certains plateaux d'impression sont chauffés pour que le matériau adhère mieux pendant l'impression.
* **Volume de construction :** (Build volume) L'espace 3D que l'imprimante peut atteindre pour extruder le matériau.
* **Roue libre :** (Coasting) Technique dans laquelle la dernière partie d'un trajet d'extrusion est imprimée avec un débit de 0%, ce qui permet de vider la buse de sa surpression.
* **Détour :** (Combing) Un mouvement qui tente d'éviter de traverser les murs lors des déplacements, pour éviter de créer une cicatrice visible à l'extérieur de l'empreinte.
* **Coordonnées de l'origine :** (Coordinate origin) L'emplacement sur le plateau d'impression où une buse se déplacerait si on lui demandait de se déplacer vers les coordonnées [0, 0, 0].
* **CuraEngine :** (CuraEngine) Un programme que Cura utilise pour faire le gros du travail de tranchage. Convertit les modèles 3D en g-code.
* **Maillage de découpe :** (Cutting mesh) Un modèle sur le plateau d'impression qui peut changer les réglages pour la partie de son volume qui chevauche les modèles imprimés réels. Le modèle lui-même n'est pas imprimé, mais il découpe des morceaux d'autres modèles et peut ensuite modifier les réglages ou l'extrudeuse avec laquelle ces pièces sont imprimées.
* **Zone interdite :** (Disallowed area) Un endroit sur le plateau d'impression où vous n'êtes pas autorisé à placer un modèle pour l'impression. Par exemple, parce qu'elle heurterait les clips qui maintiennent le lit, la tour principale, ou parce que votre impression comporterait des parties auxiliaires qui sortiraient du volume de construction.
* **Bouclier :** (Draft shield) Une enveloppe de matériau imprimé autour de l'objet qui maintient la température constante autour de l'impression .
* **Pied d'éléphant :** (Elephant's foot) Défaut d'impression où le côté inférieur de l'impression est légèrement plus large que souhaité.
* **Extrudeuse :** (Extruder) Ensemble comprenant l'alimentation, le tube Bowden optionnel, la zone de chauffe, la ''hot end'' et la buse. Certaines imprimantes disposent de plusieurs extrudeuses ou ont plusieurs parties de ligne d'extrusion. Abréviation de "ligne d'extrusion".
* **Commutateur d'extrudeuse :** (Extruder switch) En général, une seule des extrudeuses est active à la fois. Le passage d'une extrudeuse à l'autre se fait en changeant l'extrudeuse active d'une extrudeuse à l'autre.
* **Ligne d'extrusion :** (Extruder train) Ensemble comprenant l'alimentation, le tube Bowden optionnel, la zone de chauffe, la ''hot end'' et la buse. Certaines imprimantes ont plusieurs lignes d'extrusion ou ont plusieurs parties de la ligne d'extrusion.
* **Extrusion :** (Extrusion) L'action de pousser le filament à travers la ligne d'extrusion de telle sorte que la matière sorte de la buse, qui, théoriquement, est déposée au bon endroit pour former l'impression.
* **Face :** (Face) Une surface plane d'un maillage 3D. Avec les maillages triangulaires (le seul type que Cura peut traiter), toutes les faces sont des triangles dans l'espace 3D.
* **Ventilateur :** (Fan) Pas n'importe quel ventilateur de l'imprimante, mais plus précisément le ou les ventilateurs fixés à la tête d'impression qui refroidissent l'impression juste après l'extrusion du matériau.
* **Impression FDM :** (FDM printing) Modélisation des dépôts fondus. Type d'impression 3D réalisée par l'extrusion de lignes de plastique d'une certaine forme. C'est la seule technique d'impression 3D que Cura soutient. Synonyme d'"impression FFF".
* **Alimentation :** (Feeder) Un moteur et un réducteur qui poussent ou tirent le filament à travers la ligne d'extrusion.
* **Vitesse :** (Feedrate) Vitesse à laquelle le filament est introduit dans la ligne d'extrusion.
* **Impression FFF :** (FFF printing) Fabrication de filaments fondus. Type d'impression 3D réalisée par l'extrusion de lignes de plastique d'une certaine forme. C'est la seule technique d'impression 3D que Cura soutient. Synonyme de "impression FDM".
* **Filament :** (Filament) Un fil de plastique est introduit dans l'imprimante 3D,à partir de bobines. Une fois extrudé, ce n'est plus un filament mais juste de la matière.
* **Débit :** (Flow) Le taux de matériau d'extrusion par rapport à son taux normal. Un débit supérieur à 100 % permet théoriquement d'extruder plus de matière que ne le permettrait le volume alloué. Un débit inférieur à 100 % extrude théoriquement trop peu de matière.
* **Portique :** (Gantry) Le cadre mécanique qui déplace la tête d'impression autour du volume de construction.
* **Combler les trous :** (Gap filling) Technique utilisée par Cura pour remplir de petits espaces dans l'impression avec du matériau utilisant de très petits segments de ligne.
* **Remplissage progressif :** (Gradual infill) Une technique où la quantité de matériau est réduite dans les parties inférieures d'un volume, mais toujours élevée dans les parties supérieures pour soutenir correctement le matériau au-dessus. Cette technique n'est pas seulement utilisée pour le matériau mais aussi pour le support.
* **Dureté :** (Hardness) Mesure d'une impression par rapport à sa capacité de résistance à la déformation élastique ou à la perforation.
* **Bloc de chauffe :** (Heater) Un élément chauffant qui amène le filament à la température requise pour l'impression 3D.
* **Zone de chauffe :** (Heat zone) La zone où le filament s'échauffe en se dirigeant vers la buse. Au début de la zone de chauffe, le filament est à température ambiante. À la fin, il est à la température d'impression.
* **Saut :** (Hop) Une technique où la buse est déplacée vers le haut (+Z) afin de se déplacer sur l'impression avec un peu d'espace. Synonyme de "Saut en Z"..
* **Hot end :** (Hot end) La pièce en métal chaud ou en céramique contenant la buse, l'élément chauffant et le capteur de température.
* **Remplissage :** (Infill) Une structure créée à l'intérieur d'une empreinte qui soutient la peau supérieure et apporte une résistance supplémentaire à l'impression.
* **Maillage de remplissage :** (Infill mesh) Semblable à la "maille coupante", mais ne s'applique que lorsqu'elle chevauche le volume de remplissage d'un autre modèle. Il s'agit d'un modèle qui ajuste les paramètres de remplissage d'un autre modèle.
* **Murs intérieurs :** (Inner walls) Tous les murs sauf le mur extérieur. Si une partie d'une couche n'a qu'une seule paroi extérieure, elle peut avoir un nombre quelconque de parois intérieures.
* **Inset :** (Inset) Une opération sur les polygones qui produit un polygone plus petit/plus fin, dont le contour garde une certaine distance par rapport au contour du polygone original. Un encart avec une distance négative est appelé "décalage".
* **Étirage  :** (Ironing) Une technique qui consiste à repasser sur la surface supérieure  pour la rendre encore plus lisse.
* **Secousse :** (Jerk) Une limite sur la quantité de changement instantané de la vitesse appliquée au début de chaque mouvement. Ce n'est pas la même chose que la définition courante de "secousse" en physique !
* **Couche :** (Layer) L'impression en 3D se fait sur de fines couches de matériau. Ces couches sont des formes 2D d'une certaine épaisseur qui, lorsqu'elles sont empilées verticalement, forment une impression 3D.
* **Décalage de couche :** (Layer shift) Un défaut d'impression où la position horizontale d'une couche est involontairement déplacée, déplaçant généralement le reste de l'impression également.
* **Séparation des couches :** (Layer split) Un défaut d'impression où les couches ne collent pas assez bien ensemble et se fissurent.
* **Ligne :** (Line) Un brin de matériau après avoir été déposé par le train de l'extrudeuse. Dans Cura, les lignes sont modélisées comme des blocs rectangulaires ayant une certaine largeur, épaisseur (hauteur de la couche) et longueur. Semblable à un "bourelet".
* **Segment de ligne :** (Line segment) Pour éviter toute ambiguïté avec le terme d'impression 3D "ligne", Cura utilisera toujours le terme complet "segment de ligne" pour indiquer une ligne géométrique droite de longueur limitée lorsqu'il se réfère à un segment de ligne au sens mathématique.
* **Matière :** (Material) Le matériau dont se compose votre impression 3D. Généralement un thermoplastique dans l'impression FFF.
* **Maillage :** (Mesh) Une collection de triangles qui forment ensemble un modèle. Bien qu'il soit parfois utilisé comme synonyme d'"objet" et de "modèle", il est généralement utilisé dans le contexte d'une donnée plutôt que dans celui d'un document que vous souhaitez imprimer.
* **Modèle :** (Model) Un modèle 3D chargé dans la scène 3D de Cura (avant le découpage). Synonyme de "objet".
* **Buse :** (Nozzle) L'ouverture où le matériel d'impression sort de la ligne d'extrusion.
* **Objet :** (Object) Un modèle 3D chargé dans la scène 3D de Cura (avant le découpage). Synonyme de "modèle".
* **Décalage :** (Offset) Une opération sur les polygones qui produit un polygone plus grand/plus gros, dont le contour garde une certaine distance par rapport au contour du polygone original. Un décalage avec une distance négative est appelé "incrustation".
* **Mode "un à la fois" :** (One-at-a-time mode) Mode d'impression de plusieurs objets où chaque objet est entièrement terminé avant de passer à l'objet suivant, alors que normalement il imprime une couche pour chaque objet avant de passer à la couche suivante.
* **Bouclier de suintement :** (Ooze shield) Une coquille de matière imprimée autour de l'empreinte qui capte toute matière suintante lorsqu'un déplacement déplace la buse vers l'empreinte.
* **Suintement :** (Oozing) Fuite de matière par la buse alors qu'elle n'est pas prévue. En général, cela laisse un cordon de matériau le long du chemin.
* **Mur extérieur :** (Outer wall) Le mur le plus extérieur. Il n'y a qu'un seul mur extérieur par partie et par couche.
* **Surextrusion :** (Overextrusion) Extrusion d'une trop grande quantité de matériau dans un volume limité, ce qui fait que le matériau se répand là où il n'est pas censé aller.
* **Surplomb :** (Overhang) Une partie de l'impression qui n'est pas (ou pas complètement) supportée par le matériau des couches inférieures. Si le débordement est trop important pour bien imprimer, il est nécessaire de le soutenir ou de le ponter.
* **Surpression :** (Overpressure) Pendant l'impression, la chambre de la buse est maintenue à une forte pression pour garantir que le matériau est extrudé de manière constante.
* **Parquage :** (Parking) Le fait de mettre l'impression en pause pendant un moment alors que la buse est éloignée de l'impression, pour laisser le temps au matériau de refroidir.
* **Pièce :** (Part) Une forme continue (polygone) sur une seule couche. Un modèle unique peut se diviser en plusieurs parties sur certaines couches, lorsqu'il est tranché.
* **Motif :** (Pattern) Technique consistant à remplir un volume de matière, mais pas nécessairement à 100% de densité. Cura permet de choisir entre plusieurs motifs tels que lignes, grille, concentrique, tétraédrique, etc.
* **Matelassage :** (Pillowing) Un défaut d'impression où la peau supérieure est bombée ou se brise entre les deux, où elle repose sur les lignes de remplissage en dessous.
* **Polygone :** (Polygon) Une forme 2D ou une boucle fermée constituée d'une série de points avec des segments de ligne droite entre eux.
* **Goutte d'amorçage :** (Prime blob) Une goutte de matière qui est purgée au début d'une impression pour amorcer une extrudeuse.
* **Tour d'amorçage :** (Prime tower) Une structure créée en plus de l'impression qui permet à l'imprimante d'amorcer ses buses sur les couches supérieures sans que l'excès de matériau ne se retrouve sur le côté de l'impression réelle. Utilisé pour les impressions où plusieurs extrudeuses sont impliquées pour amorcer une extrudeuse après avoir été en attente pendant un certain temps.
* **Amorçage :** (Priming) Action de purger une matière pour s'assurer que le filament est aligné sur l'extrémité de la buse et que la chambre de la buse est remplie et mise sous pression correctement. Habituellement, cette opération est effectuée au début d'une impression ou après un changement d'extrudeuse.
* **Purge :** (Purging) L'acte d'extruder une matière en tant que déchet. Une raison courante de purge est l'"amorçage".
* **Radeau :** (Raft) Technique permettant d'améliorer l'adhérence des plaques en imprimant une plaque solide sous votre impression, qui est ensuite jetée. La plaque a une grande surface et est imprimée avec des lignes épaisses qui adhèrent bien, et rattrapent les irrégularités de la planéité de le plateau d'impression.
* **Rétraction :** (Retraction) L'action d'utiliser l'alimentateur pour ramener la matière dans la chambre de la buse. Habituellement, il s'agit d'arrêter temporairement la matière qui s'écoule de la buse pour effectuer un trajet propre.
* **Oscillation :** (Ringing) Un défaut d'impression où la surface vacille en raison d'une extrusion incohérente ou d'une oscillation de la buse. Cela se produit généralement après avoir fait des angles vifs trop rapidement.
* **Cicatrice :** (Scar) Une marque de dommage sur l'extérieur de l'impression où la buse a fait fondre le matériau en passant.
* **Couture :** (Seam) L'endroit où une boucle fermée commence et s'arrête. Ce point est généralement visible sur l'impression finale, vous souhaitez donc le placer à un endroit peu visible.
* **Coquille :** (Shell) Tant les murs que la peau.
* **Peau :** (Skin) Les faces supérieure et inférieure de l'impression. Ils sont toujours imprimés à 100 % de densité, généralement avec le motif des lignes. Synonyme de "haut/bas".
* **Jupe :** (Skirt) Un contour dessiné autour de l'impression sur la première couche pour à la fois amorcer le matériau et permettre à l'utilisateur de voir si le plateau d'impression est complètement à niveau.
* **Découpage :** (Slicing) Le processus de conversion d'un modèle 3D en instructions pour qu'une imprimante 3D puisse l'imprimer. Dans le contexte de Cura Engine, ce processus est aussi parfois utilisé pour la création de coupes transversales du modèle, qui est l'une des étapes du processus de découpage complet.
* **Mode spirale :** (Spiralise mode) Un mode permettant d'imprimer uniquement le contour des modèles, généralement en augmentant progressivement la coordonnée Z dans toute la couche pour éliminer le joint Z en imprimant le modèle en une grande spirale. En dehors de Cura, ce mode est également connu sous le nom de "mode vase".
* **En attente :** (Stand-by) Lorsque l'impression se fait avec plusieurs extrudeuses, une seule d'entre elles est généralement active à la fois. Les autres extrudeuses sont en attente.
* **Couture :** (Stitching) Une partie du processus de découpage. La création de sections transversales d'un groupe de triangles donne lieu à un ensemble de segments de lignes sur chaque couche. La couture combine ces segments de ligne en polygones et détermine ce qu'est l'intérieur de la couche.
* **Force :** (Strength) Terme englobant indiquant diverses mesures de résistance au mouvement, y compris la dureté, la rigidité et la ténacité lorsque différents types de force sont appliqués.
* **Filasse :** (Stringing) Lors d'un déplacement avec de la matière qui suinte, cela crée de minces brins de matière appelés "cordage". Ces brins ne s'étendent pas nécessairement sur toute la longueur d'un déplacement. Une forme moins extrême de ce phénomène donne lieu à des "gouttes".
* **Support :** (Support) Une partie de l'impression qui est enlevée après l'impression, mais qui était nécessaire pour maintenir des parties de l'impression en place pendant que l'impression était encore en cours, pour éviter que le matériau ne tombe ou ne vacille trop.
* **Bloqueur de support :** (Support blocker) Un modèle qui empêchera que le soutien soit généré pour soutenir tout dépassement avec lequel le modèle chevauche. Synonyme de "maillage anti-dépassement".
* **Plancher de soutien :** (Support floor) La face inférieure du support, utilisée là où le support repose sur le modèle. Cette partie du support peut éventuellement être imprimée avec différents réglages. Il n'y a pas de plancher de support où le support repose sur le plateau d'impression.
* **Remplissage de soutien :** (Support infill) La principale composante des éléments dit d'aide. S'il n'y a pas d'interface de soutien, le soutien consiste uniquement en un remplissage de soutien.
* **Interface de support :** (Support interface) Le toit et le plancher de soutien, où le modèle repose sur le support et où le support repose sur le modèle. Le côté inférieur du support, où le support repose sur le plateau d'impression, n'a pas d'interface de support.
* **Maillage de soutien :** (Support mesh) Un modèle qui est rempli d'une structure de support, au lieu d'être imprimé comme une impression normale. Peut être utilisé pour personnaliser la forme de votre support.
* **Toit de soutien :** (Support roof) La face supérieure du support, utilisée là où le modèle repose sur le support. Cette partie du support peut éventuellement être imprimée avec différents réglages.
* **Support coniques :** (Support towers) Une technique permettant de soutenir des parties très fines ou petites de l'impression. La partie est soutenue par la pointe d'une tour qui s'élargit vers le bas afin que le support ne s'effondre pas pendant l'impression.
* **Thermoplastique :** (Thermoplastic) Un type de plastique qui devient mou en fondant. Seuls les thermoplastiques peuvent être utilisés pour l'impression FFF.
* **Épaisseur :** (Thickness) La taille d'une structure dans la direction verticale (Z). Comparer avec "largeur".
* **Dessus/dessous :** (Top/bottom) Les faces supérieure et inférieure de l'impression. Ils sont toujours imprimés à 100 % de densité, généralement avec le motif des lignes. Synonyme de "peau".
* **Surface du dessus :** (Top surface) La partie la plus haute de la peau supérieure. Rarement plus d'une couche, cette surface supérieure peut être imprimée avec des réglages séparés pour obtenir une meilleure qualité sans que cela ne coûte beaucoup de temps d'impression supplémentaire.
* **Topographie :** (Topography) L'effet où la hauteur limitée des couches transforme une surface presque plane en quelque chose qui ressemble à une carte de hauteur géographique avec des anneaux où les couches se terminent.
* **Résistance :** (Toughness) Mesure d'une impression pour savoir dans quelle mesure elle peut résister à la déformation plastique.
* **Déplacement :** (Travel , move) Déplacer la buse d'un endroit à l'autre sans extruder de matière.
* **Sous-extrusion :** (Underextrusion) Extrusion de trop peu de matière pour remplir correctement un volume ou pour créer correctement des perles solides et continues.
* **La sous-pression :** (Underpressure) Lorsqu'elle est rétractée, la chambre de la buse est maintenue à une pression négative, afin d'aspirer la matière à l'intérieur, ce qui empêche le suintement.
* **Mode Vase :** (Vase mode) Un mode permettant d'imprimer uniquement le contour des modèles, généralement en augmentant progressivement la coordonnée Z sur toute la couche pour éliminer la couture Z. Cura appelle toujours ce mode "spiralisé".
* **Murs :** (Walls) Les côtés de l'impression. Ils s'enroulent autour du modèle horizontalement.
* **Gauchissement :** (Warping) Déformation de l'impression après l'impression, due au rétrécissement du matériau ou à des contraintes internes tirant sur le matériau alors qu'il n'est pas encore solidifié.
* **Largeur :** (Width) La taille d'une structure dans le sens horizontal (X/Y). Comparer avec "épaisseur".
* **Sens d'enroulement :** (Winding order) L'ordre des points formant un polygone. Soit dans le sens des aiguilles d'une montre, soit dans le sens inverse. Dans Cura, un sens d'enroulement dans le sens inverse des aiguilles d'une montre indique une forme positive tandis qu'un ordre d'enroulement dans le sens des aiguilles d'une montre indique un trou. Les modèles 3D d'entrée doivent avoir des triangles avec un ordre d'enroulement dans le sens inverse des aiguilles d'une montre lorsqu'ils sont vus de l'extérieur.
* **Essuyage :** (Wiping) Technique consistant à faire traverser à la buse une structure préalablement imprimée afin d'essuyer toute matière suintante pendante à l'extrémité de la buse, pour éviter que cette matière ne soit placée sur l'extérieur de l'impression.
* **Impression filaire :** (Wire printing) Technique permettant d'imprimer un modèle en imprimant uniquement un cadre métallique autour de sa coque. Très expérimental (Désactivé dans les dernières version de cura).
* **Couture en Z :** (Z seam) Un point visible sur la paroi extérieure où la buse se déplace d'une couche à l'autre. Souvent utilisé à tort au lieu de "joint".
* **Saut en Z :** (Z hop) Une technique où la buse est déplacée vers le haut (+Z) afin de se déplacer sur l'impression avec un peu d'espace. Synonyme de "Saut".
