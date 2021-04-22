Imprimer le remplissage avant les parois
====
Cela affecte l'ordre dans lequel les choses sont imprimées. Lorsque ce paramètre est activé, le remplissage d'une pièce sera imprimé avant que les parois de cette pièce sur cette couche ne soient imprimées.

![Le paramètre est désactivé, donc les parois sont imprimés en premier](../../../articles/images/infill_before_walls_disabled.gif)
![Le paramètre est activé, donc le remplissage est imprimé en premier](../../../articles/images/infill_before_walls_enabled.gif)

Ce réglage est un compromis entre la précision et la force :
* Si les parois sont imprimées avant le remplissage, les parois pourraient n'avoir rien à quoi se fixer, ce qui les ferait s'affaisser davantage. Cependant, les parois se seront solidifiées en premier et ne seront pas repoussés par le remplissage, ce qui empêche le remplissage de ressortir à travers les parois.
* Si le remplissage est imprimé avant les parois, les parois seront repoussées à l'endroit où le remplissage est fixé aux parois, ce qui rend les parois moins précises et peut faire ressortir le remplissage à travers la surface, créant ainsi un motif visible à l'extérieur. Cependant, le remplissage maintiendra mieux les parois en place pendant l'impression.
