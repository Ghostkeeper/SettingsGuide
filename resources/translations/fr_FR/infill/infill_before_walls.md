Imprimer le remplissage avant les parois
====
Cela affecte l'ordre dans lequel les choses sont imprimées. Lorsque ce paramètre est activé, le remplissage d'une pièce sera imprimé avant que les parois de cette pièce sur cette couche ne soient imprimées.

![Le paramètre est désactivé, donc les murs sont imprimés en premier](../../../articles/images/infill_before_walls_disabled.gif)
![Le paramètre est activé, donc le remplissage est imprimé en premier](../../../articles/images/infill_before_walls_enabled.gif)

Ce réglage est un compromis entre la précision et la force :
* Si les murs sont imprimés avant le remplissage, les murs pourraient n'avoir rien à quoi se fixer, ce qui les ferait s'affaisser davantage. Cependant, les murs se seront solidifiés en premier et ne seront pas repoussés par le remblai, ce qui empêche le remblai de briller à travers les murs.
* Si le remplissage est imprimé avant les murs, les murs seront repoussés à l'endroit où le remplissage est fixé aux murs, ce qui rend les murs moins précis et peut faire briller le remplissage à travers la surface, créant ainsi un motif visible à l'extérieur. Cependant, le remplissage maintiendra mieux les murs en place pendant l'impression.
