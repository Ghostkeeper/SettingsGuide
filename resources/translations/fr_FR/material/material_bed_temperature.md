Température du plateau par défaut
====
Certaines imprimantes ont un plateau chauffé. Ce réglage détermine la température du plateau.

En chauffant le plateau, le matériau reste légèrement fluide et collant. Certains matériaux forment des cristaux lors de la congélation, ce qui entraîne un rétrécissement important du matériau lors de la congélation. Le lit chauffant maintient le matériau juste au-dessus de la température de congélation pour éviter ce retrait. Tout ceci a pour but d'améliorer l'adhérence de l'impression à le plateau d'impression.

Cependant, si le plateau d'impression est maintenue trop chaude, l'impression sera très fluide à l'endroit où elle touche le plateau. Le matériau s'affaisse alors un peu, ce qui provoque une patte d'éléphant sur la face inférieure de l'empreinte. Ce phénomène peut être compensé par le paramètre [Expansion horizontale de la couche initiale](../shell/xy_offset_layer_0.md), mais il affecte la précision dimensionnelle. Le chauffage du plateau d'impression crée également une différence de température entre le matériau qui repose sur le plateau et le matériau situé plus haut dans le modèle, ce qui provoque un [gauchissement](../troubleshooting/warping.md) lorsque le matériau situé plus haut commence à se rétracter.

Si ce paramètre est réglé sur 0 degré, Cura n'émettra aucune commande pour modifier la température de le plateau d'impression, ce qui pourrait perturber le microprogramme s'il n'y a pas de plateau d'impression.

**Lorsque vous ajustez la température de le plateau d'impression dans un profil de matériau, le paramètre [Température du plateau par défaut](default_material_bed_temperature.md) est ajusté. Normalement, la température de le plateau d'impression sera égale à la température de le plateau d'impression par défaut, mais parfois, le choix d'une qualité différente peut entraîner de légers ajustements de la température de le plateau d'impression. Ce réglage de la température de le plateau d'impression est celui qui est réellement utilisé pour l'impression.**
