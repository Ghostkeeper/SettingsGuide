Distance d'expansion de la couche extérieure
====
Élargissez ou réduisez les couches pleines en haut et en bas de votre impression dans le sens horizontal. Normalement, les couches pleines ne sont générées que dans les parties où il y a du vide au-dessus ou en dessous, mais avec ce réglage, vous pouvez l'élargir horizontalement un peu plus, ce qui améliore la résistance en faisant en sorte que la peau s'attache mieux aux parois adjacentes et en fermant les interstices de la peau.

![Comment les contours extérieur (les parties jaunes) ont normalement sont créés](../../../articles/images/skin_preshrink_original.png)
![Contours extérieurs agrandis de 1mm](../../../articles/images/expand_skins_expand_distance_1mm.png)

* Si vous avez de petits trous dans les couches supérieures ou inférieures de l'impression (trous qui sont remplis par le motif de remplissage), le fait de régler ce paramètre un peu plus haut les fermera. Cela permet à l'imprimante d'imprimer en continu les lignes du bas, ce qui améliore considérablement la résistance.
* Si votre modèle a une surface horizontale à côté d'une paroi raide, augmenter ce réglage peut améliorer l'adhérence entre les parois de la surface raide et la peau, car la peau sera imprimée directement au contact de ces parois.
* Si vous réglez ce paramètre sur une valeur négative, la largeur des couches supérieure et inférieure sera réduite et remplacée par un remplissage. Cela peut permettre de gagner du temps d'impression, au détriment de la résistance.

**En raison de limitations techniques, vous ne pouvez pas réduire ce paramètre en dessous de la valeur de [Largeur de retrait de la couche extérieure](skin_preshrink.md). Augmentez le paramètre Skin Removal Width afin d'enlever plus de peau.**
