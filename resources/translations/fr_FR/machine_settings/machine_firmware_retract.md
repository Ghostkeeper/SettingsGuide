Rétraction du firmware
====
Normalement, Cura provoque une rétraction en contrôlant le mouvement du chargeur, en lui commandant de déplacer le filament un peu vers l'arrière. Si ce paramètre est activé, il écrira à la place une commande "G10" pour signifier que l'imprimante doit rétracter le filament, ou une commande "G11" pour le retirer.

En choisissant d'utiliser les rétractions du microprogramme, le microprogramme de l'imprimante contrôle la distance et la vitesse de rétraction du filament. L'imprimante en sait peut-être plus sur sa propre géométrie que Cura, et peut donc mieux décider de la manière de rétracter le filament. Cependant, cela signifie que Cura ne contrôle plus ces rétractions et que Cura en sait plus sur l'impression elle-même. Pour l'essentiel, le trancheur et le microprogramme ont des informations différentes, et ce réglage décide lequel des deux peut être choisi.

*Comme il s'agit d'un réglage de la machine, ce réglage n'est normalement pas visible dans la liste des réglages.*
