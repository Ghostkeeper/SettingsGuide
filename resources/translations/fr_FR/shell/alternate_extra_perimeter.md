Alterner les parois supplémentaires
====

Ce paramètre ajoute une paroi supplémentaire une couche sur deux. De cette façon, le remplissage est coincé verticalement entre les murs, ce qui donne des impressions plus solides.

Par exemple, si vous réglez le nombre de lignes de paroi à deux parois et que vous activez l'option "Alterner les parois supplémentaires", deux parois seront imprimés sur les couches paires et trois parois sur les couches impaires.

![Cette image montre les parois affectés lorsque vous modifiez ce paramètre.](../../../articles/images/alternate_extra_perimeter.gif)

L'activation de ce paramètre prendra plus de temps, environ la moitié de ce que prendrait l'ajout d'une paroi supplémentaire. D'une certaine manière, cette parois supplémentaire alternée est presque aussi bon qu'une paroi supplémentaire complete, et d'une autre manière, il ne l'est pas :
* Il augmente considérablement l'adhérence entre le remplissage et les murs, puisque les lignes de remplissage peuvent également adhérer verticalement à la paroi supplémentaire au-dessus et au-dessous d'elles. À cet égard, la paroi supplémentaire est un atout majeur. Elle est très efficace. 
* Il ajoute à la rigidité de l'impression autant que la moitié d'une paroi supplémentaire. En adhérant à la paroi adjacente, elle répartit les contraintes sur un plus grand nombre de brins et offre une plus grande résistance aux forces dans la direction horizontale. La paroi supplémentaire alternée n'a pas d'avantage particulier à faire cela, ni d'inconvénient particulier.
* Une vraie paroi supplémentaire ajouterait également à la force de liaison des couches. Les parois sont imprimées lentement, elles sont donc une source importante de force de liaison des couches. Cependant, la paroi supplémentaire alternée ne se lie pas aux couches adjacentes car elle ne se produit qu'une couche sur deux.

Par conséquent, la paroi supplémentaire alternée est un moyen efficace d'ajouter une rigidité horizontale, mais pas un moyen efficace d'ajouter une résistance verticale.