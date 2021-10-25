Décollement
====
Le décollement est un problème de l'impression finale où l'empreinte se recroqueville après l'impression, laissant l'objet final déformé. Généralement, les coins du bas de l'impression se recourbent vers le haut, ou bien des parties fines de l'impression deviennent ondulées.

![Les pointes s'enroulent](../../../articles/images/warping.jpg)

Cause
----
Le décollement est causé par une combinaison d'effets, mais principalement par une contrainte interne due à la traction de la buse sur le plastique fondu. Lorsqu'il est en transition vitreuse, le plastique se comporte un peu comme le caoutchouc ou la gomme. Si vous tirez dessus, le matériau s'étire, mais si vous arrêtez de tirer, il reprend sa forme initiale. La même chose se produit également lors de l'impression. Lorsque vous imprimez une longue ligne, la buse tire sur la ligne de plastique, qui s'étire sur la longueur de la ligne. Lorsque la buse s'éloigne et cesse de tirer, la ligne de plastique se contracte. Cette contraction provoque une traction sur tout ce qui y est attaché. Lorsqu'un nombre suffisant de lignes de plastique tirent à l'unisson, elles peuvent déformer l'impression. Cela est particulièrement fréquent lorsque de nombreuses lignes sont parallèles, comme dans la peau.

Un deuxième effet qui provoque le décollement est le rétrécissement de la matière lorsqu'elle refroidit. La plupart des matériaux ont tendance à rétrécir lorsqu'ils refroidissent. Si l'objet refroidit de manière non uniforme, certaines parties de l'impression rétrécissent plus que d'autres, ce qui déforme l'objet. Au fur et à mesure que l'objet continue à refroidir, il se solidifie davantage, ce qui verrouille cette déformation de façon permanente.

Certains matériaux sont plus sensibles au rétrécissement que d'autres en raison de leur cristallinité inhérente. Voici quelques coefficients de rétrécissement des matériaux d'impression 3D courants. Il s'agit approximativement de la quantité de rétrécissement de chaque type de matériau lorsqu'il refroidit de sa température de transition vitreuse à la température ambiante. Une certaine variation se produit entre les mélanges. Un retrait plus important entraînera un gauchissement plus important.
* PLA : 0,21%.
* ABS : 0,70 %.
* TPU : 0,63%.
* HIPS : 0.64%
* PETG et CPE : 0,45%.
* Nylon : 0.62%
* PC : 0,70%.
* PP : 1,2%

En outre, le décollement peut être évité si d'autres matériaux sont en travers de la route. Si une partie de l'impression est complètement dense, le matériau environnant peut se rétracter moins ou pas du tout. Si d'autres parties ne sont pas complètement denses, vous obtiendrez une impression partiellement rétractée. La partie rétractée de l'impression tirera sur le reste, ce qui peut également provoquer un gauchissement. Ce phénomène est fréquent à la frontière entre la peau et le remplissage, car la peau est complètement dense, mais le remplissage ne l'est pas.

Le décollement est le plus fréquent dans la partie inférieure de l'empreinte. C'est là que le gradient de température est le plus important, car le bas de l'impression est souvent chauffé par un lit chauffant et le reste de l'impression ne l'est pas. La face inférieure est généralement constituée de nombreuses et longues lignes de peau. Si le [motif du bas](../top_bottom/top_bottom_pattern.md) est réglé sur Lignes ou Zigzag, ces lignes sont longues, droites et parallèles, ce qui leur permet de tirer à l'unisson dans la même direction pour déformer l'objet.

Prévention
----
* Si le décollement se produit dans la face inférieure de l'impression, réglez le [Couche initiale du motif du dessous](../top_bottom/top_bottom_pattern_0.md) sur concentrique. De cette façon, la contraction des lignes de la peau du bas ne se fera plus à l'unisson. La tension interne se répartira uniformément à l'intérieur de la couche inférieure. Si cela ne suffit pas à empêcher la déformation, vous pouvez également régler le modèle ordinaire [Motif du dessus/dessous](../top_bottom/top_bottom_pattern.md) sur Concentrique.
* Pour réduire les gradients de température à l'intérieur de l'impression, réduisez la [température du plateau d'impression](../material/material_bed_temperature.md). L'objet devrait alors refroidir de manière plus uniforme.
* Selon la matière de votre imprimante, l'impression dans une chambre chauffée fermée peut également empêcher le gauchissement. D'une part, cela réduira la différence de température entre le volume de construction et le plateau d'impression, et la différence entre le volume de construction et la buse. Cela permettra également au plastique de [recuire](https://en.wikipedia.org/wiki/Annealing_%28glass%29) plus longtemps, réduisant ainsi les contraintes internes et donc la traction des lignes imprimées qui causent le gauchissement. Si votre imprimante le permet, pensez à augmenter la [température du volume d'impression](../material/build_volume_temperature.md).
* Pour éviter que la face inférieure ne se déforme, une bonne adhérence du plateau d'impression est utile. Cela augmente la force nécessaire pour que le matériau se déforme. Par exemple, augmentez la [largeur de la bordure](../platform_adhesion/brim_width.md) ou la [marge supplémentaire du radeau](../platform_adhesion/raft_margin.md).
* L'utilisation d'un [radeau au lieu d'une bordure](../platform_adhesion/adhesion_type.md) enlève l'impression directe sur le plateau d'impression et place un morceau de plastique plein entre la pièce et le plateau, conçu pour résister au gauchissement.
* Essayez d'imprimer en [activant le bouclier](../experimental/draft_shield_enabled.md). Cela crée une chambre autour de votre impression, ce qui empêche les courants d'air extérieurs de refroidir votre impression avant qu'elle ne soit terminée. Cependant, n'oubliez pas que le bouclier lui-même peut aussi se rétracter. Si le bouclier ne fonctionne pas, vous pourriez voir beaucoup de filasses dans votre impression.
* L'impression est réalisée dans un matériau qui rétrécit moins, comme le PLA.
* Si vous êtes libre de faire des ajustements au modèle imprimé, essayez d'éviter de placer des coins extérieurs très pointus sur le plateau d'impression. Vous pouvez choisir d'arrondir certains coins extérieurs. Cela empêche toute la force de la contrainte interne de se concentrer en un point, réduisant ainsi la probabilité de déformation.
