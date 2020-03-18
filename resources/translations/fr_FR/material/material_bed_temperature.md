Température du plateau par défaut
===

Certaines imprimantes ont un plateau chauffé. Ce réglage détermine la température du plateau.

En chauffant le plateau, le matériau reste légèrement fluide et collant. Certains matériaux forment des cristaux lors de la congélation, ce qui entraîne un rétrécissement important du matériau lors de la congélation. Le lit chauffant maintient le matériau juste au-dessus de la température de congélation pour éviter ce retrait. Tout ceci a pour but d'améliorer l'adhérence de l'impression à la plaque de montage.

Cependant, si la plaque de montage est maintenue trop chaude, l'impression sera très fluide à l'endroit où elle touche la plaque de montage. Le matériau s'affaisse alors un peu, ce qui provoque une patte d'éléphant sur la face inférieure de l'empreinte. Ce phénomène peut être compensé par le paramètre [Expansion horizontale de la couche initiale](../shell/xy_offset_layer_0.md), mais il affecte la précision dimensionnelle.

Si ce paramètre est réglé sur 0 degré, Cura n'émettra aucune commande pour modifier la température de la plaque de montage, ce qui pourrait perturber le microprogramme s'il n'y a pas de plaque de montage.

*Lorsque vous ajustez la température de la plaque de montage dans un profil de matériau, le paramètre [Température du plateau par défaut](./default_material_bed_temperature.md) est ajusté. Normalement, la température de la plaque de montage sera égale à la température de la plaque de montage par défaut, mais parfois, le choix d'une qualité différente peut entraîner de légers ajustements de la température de la plaque de montage. Ce réglage de la température de la plaque de montage est celui qui est réellement utilisé pour l'impression.*
