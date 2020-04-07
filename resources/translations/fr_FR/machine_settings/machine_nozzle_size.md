Diamètre de la buse
====
Ce réglage mesure le diamètre de l'ouverture de la buse à travers laquelle la matière s'écoule.

! [Dimensions de la tête d'impression](../images/head_dimensions_fr.svg)

C'est une dimension importante sur laquelle d'autres paramètres peuvent se baser par défaut. Plus important encore, la [Largeur de ligne](../resolution/line_width.md) est normalement ajustée en fonction de la taille de la buse. Certains profils d'imprimante limitent également la hauteur de la couche en fonction de la taille de la buse, car la taille de la buse est le facteur le plus important pour la vitesse d'extrusion du matériau.

La taille de la buse est également utilisée directement, pour un détail : Lors du remplissage de [minuscules espaces](../shell/fill_perimeter_gaps.md), les morceaux de ligne plus éloignés que deux tailles de buse ne sont pas fusionnés.

N'ajustez pas la taille de la buse à moins que vous ne modifiiez réellement la buse physique. Certaines trancheuses (dont Cura 15.04 et antérieures) utilisent le terme "taille de buse" pour désigner la largeur des lignes de l'impression. Cura utilise le paramètre [Largeur ligne](../resolution/line_width.md) pour cela.

*Comme il s'agit d'un réglage de la machine, ce paramètre n'est normalement pas visible dans la liste des paramètres. Si votre imprimante possède des profils spécifiques pour les buses disponibles, vous pouvez les sélectionner dans le menu de configuration de l'imprimante en haut au centre de l'écran. Sinon, vous pouvez ajuster le diamètre des buses dans la boîte de dialogue des paramètres de l'imprimante, qui se trouve dans la liste des imprimantes ajoutées dans la boîte de dialogue des préférences.*
