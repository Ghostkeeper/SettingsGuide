Pont à faible densité de remplissage max
====
Si vous imprimez avec une très faible densité de remplissage, la peau supérieure a tendance à s'affaisser, ce qui provoque des [coussins](../troubleshooting/pillowing.md) et des surfaces généralement irrégulières sur la face supérieure de l'impression. En option, les techniques de pontage peuvent également être appliquées à la peau supérieure. Ce paramètre permet de configurer la vitesse de remplissage à laquelle la technique de pontage commencera à être appliquée.

![La peau forme un pont sur le remplissage](../../../articles/images/bridge_sparse_infill_max_density.png)

Ce paramètre est configuré comme un seuil, afin de permettre aux profils de contenir une seule valeur. Pendant que l'utilisateur ajuste la densité de remplissage en permanence, le pontage pour la peau sera automatiquement activé ou désactivé.

Le pontage pour la peau supérieure produit généralement une surface supérieure plus lisse à des taux de remplissage très faibles. Cependant, assurez-vous que si vous utilisez cette technique, il y a suffisamment de [couches supérieures](../shell/top_layers.md) pour fermer correctement la surface sans appliquer la technique de pontage sur les couches les plus élevées. La technique de pontage, en particulier avec une [largeur de ligne](bridge_skin_material_flow_3.md) réduite ne fermera pas complètement la surface. Si la peau supérieure n'a pas assez de couches, vous vous retrouverez avec des trous dans l'impression et une résistance compromise.
