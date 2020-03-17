Angle de parois en porte-à-faux
===

Ce réglage indique l'angle de seuil après lequel un mur sera marqué comme "mur en surplomb". Ces murs en surplomb peuvent être imprimés à une vitesse différente en utilisant le paramètre [Vitesse de paroi en porte-à-faux](./wall_overhang_speed_factor.md).

Si ce paramètre est réglé sur 0°, tous les murs seront traités comme des murs en surplomb. Si ce paramètre est réglé sur 90°, aucun mur ne sera traité comme un mur en surplomb. Les murs qui reposent sur un support ne sont pas non plus traités comme des murs en surplomb.

Le but de cette fonction est de fournir de meilleures qualités de surplomb pour les zones qui auraient presque besoin d'être soutenues par [support](../support/support_enable.md), mais pas tout à fait. Au lieu de passer plus de temps et de matériel sur le support et de marquer la surface en enlevant ce support, vous pouvez choisir d'imprimer ces murs en surplomb un peu plus lentement et de régler l'[Angle de surplomb du support](../support/support_angle.md) un peu plus haut. Cela permet d'obtenir une approche plus progressive de l'impression en augmentant mieux les angles de surplomb.

Le fait de régler ce paramètre plus haut que l'angle de surplomb du support réduit considérablement l'effet de cette fonction, car les murs au-dessus du support ne sont pas marqués comme des murs en surplomb, et donc tous les murs qui sont imprimés à un angle de surplomb qui serait considéré comme un mur en surplomb seraient également supportés et non imprimés à des vitesses différentes. Toutefois, cette caractéristique a toujours un effet si le support est désactivé ou pour les parties en surplomb qui ne sont pas supportées pour d'autres raisons, telles que [Surface de support minimale](../support/minimum_support_area.md).
