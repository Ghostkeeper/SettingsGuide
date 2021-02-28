Angle du bouclier de suintage
====
Le bouclier de suintement suivra la forme du modèle. Il doit rester proche, sinon le trajet entre le bouclier et la maquette suintera du nouveau matériau. Mais la maquette peut avoir des surfaces horizontales, ce qui créerait des surplombs abrupts dans le bouclier de suintement. Ce réglage limite l'inclinaison du bouclier de suintement afin qu'il ne s'effondre pas.

![Au lieu de suivre le modèle en bas et en haut, il n'est pas plus raide que l'angle spécifié](../images/ooze_shield_fr.svg)

* Une valeur de 0 rend le bouclier de suintement complètement vertical autour de la forme entière. Plus l'angle est faible, plus le bouclier sera stable.
* Une valeur de 90 fait que le bouclier antifuite suit exactement le modèle. Plus l'angle est élevé, mieux la bouclier antifuite empêchera le suintement sur le modèle.

Alors qu'il serait théoriquement logique d'utiliser ici une valeur similaire à celle de l'[Angle de porte-à-faux de support](../support/support_angle.md), le bouclier de suintement n'est qu'une simple ligne. Cette ligne unique est plus faible que votre modèle et plus sujette au gauchissement. Il est bon d'utiliser un angle légèrement plus faible que celui qui serait normalement imprimé sur votre modèle, pour éviter que le bouclier de suintement ne se fende.
