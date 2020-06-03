Position anti-suintage rétractée
====
Pour certaines imprimantes, lorsqu'un matériau est rétracté pour un interrupteur à filament, le matériau doit être coupé proprement afin de le faire passer dans le chargeur sans s'emmêler. Ce réglage configure une partie de la procédure pour le rompre proprement.

Ce réglage ajuste la première position dans laquelle le matériau est rétracté afin d'empêcher qu'il ne suinte. Le matériau n'est pas encore cassé à ce stade. Le but est seulement de supprimer rapidement la pression sur la chambre de la buse en la tirant vers l'intérieur.

![D'abord, le matériau est rétracté pour arrêter le suintement, selon ce réglage](../../../articles/images/filament_switch_anti_ooze.svg)
![Deuxièmement, le filament est lentement rétracté pour tirer un fil fin qui est facile à casser et laisser ce fil se solidifier](../../../articles/images/filament_switch_break_preparation.svg)
![Troisièmement, le filament est rapidement rétracté davantage pour le rompre](../../../articles/images/filament_switch_break.svg)

**Ce paramètre n'est actuellement jamais visible dans l'interface de Cura. Il ne peut être défini que par les profils. Il n'est pas non plus utilisé par Cura pendant le découpage. Cependant, les imprimantes qui comprennent le format de fichier matériel de Cura peuvent l'utiliser pour configurer correctement leur procédure de changement de filament ** Grâce à un script de post-traitement, la commande "M600" peut être insérée dans l'impression, ce qui déclenchera un changement de filament.**
