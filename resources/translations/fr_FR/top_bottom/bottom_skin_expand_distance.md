Distance d'expansion de la couche extérieure inférieure
====
Élargissez ou réduisez les couches solides du fond de votre impression dans le sens horizontal. Normalement, les couches solides ne sont générées qu'au-dessus des parties où il y a de l'air en dessous, mais avec ce réglage, vous pouvez l'élargir horizontalement un peu plus, ce qui améliore la résistance en faisant en sorte que la peau s'attache mieux aux parois adjacentes et en fermant les interstices de la peau.

![Comment les peaux (les parties jaunes) ont normalement l'air](../../../articles/images/skin_preshrink_original.png)
![Peaux agrandies de 1mm](../../../articles/images/expand_skins_expand_distance_1mm.png)

* Si vous avez de petits trous dans les couches inférieures de la peau (trous qui sont remplis avec le motif de remplissage), le fait de régler ce paramètre un peu plus haut les fermera. Cela permet à l'imprimante d'imprimer en continu les lignes du bas, ce qui améliore considérablement la résistance.
* Si la face inférieure n'est pas directement sur le platau d'impression, il y aura des parois sous la peau. Cela améliorera l'adhérence entre les couches inférieures et ses parois voisines, car les couches inférieures seront imprimées directement sur les parois.
* Le réglage de ce paramètre à une valeur négative réduira la largeur des couches inférieures, en la remplaçant par un remplissage. Cela peut permettre de gagner du temps d'impression, au détriment de la résistance.

**En raison de limitations techniques, vous ne pouvez pas réduire ce paramètre en dessous de la valeur de [Largeur de retrait de la couche extérieure inférieure](bottom_skin_preshrink.md). Augmentez le paramètre Bottom Skin Removal Width afin d'enlever plus de peau.**
