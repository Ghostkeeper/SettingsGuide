Largeur de ligne
====
Il s'agit de la largeur horizontale des lignes que l'imprimante va placer vers le bas. Normalement, le diamètre de l'ouverture de la buse détermine la largeur des lignes, mais en extrudant plus ou moins de matière, l'imprimante peut faire varier légèrement la largeur des lignes.

![Lignes très fines](../../../articles/images/line_width_small.png)
![Lignes très larges](../../../articles/images/line_width_large.png)

La réduction de la largeur de la ligne permet à l'imprimante d'imprimer plus de détails. En particulier, cela permet également à l'imprimante d'imprimer des parties fines. La largeur de ligne est l'un des paramètres les plus influents de votre impression. En voici quelques effets :
* L'impression de lignes plus fines permet d'imprimer des pièces plus fines, puisqu'elle peut même faire tenir une ligne dans les parties les plus fines.
* Le fait d'ajuster la largeur de la ligne à un multiple pair de l'épaisseur de votre impression peut rendre l'objet plus solide et améliorer le flux de matière.
* Une largeur de ligne plus petite rendra votre surface supérieure plus lisse.
* Des lignes d'impression légèrement plus petites que la taille de votre buse ont tendance à améliorer la résistance. Cela permet à la buse de fusionner les lignes adjacentes entre elles lorsqu'elle effectue un second passage légèrement supérieur à la ligne précédente.
* Les lignes d'impression trop larges entraînent une sous-extrusion. L'imprimante tentera d'extruder plus de matière, suffisamment pour remplir la largeur de ligne souhaitée. Ce matériau tentera de s'écouler dans n'importe quelle direction. Toutefois, à un moment donné, la contre-pression devient trop importante, de sorte que le matériau ne s'écoule plus jusqu'au bord des lignes très larges. Cela laisse alors des espaces entre les lignes.
* Les lignes d'impression trop petites entraînent également une sous-extrusion. Si le matériau ne s'écoule pas assez rapidement à travers la buse, la tension superficielle du matériau le fera coaguler en petites gouttelettes, ce qui rendra l'extrusion inégale et laissera des espaces entre les gouttelettes.
* L'impression de lignes plus fines augmentera considérablement le temps d'impression.

*Il n'est pas conseillé de réduire la largeur des lignes en dessous de 60% de la taille de la buse ou au-dessus de 150%. Dans les deux cas, il se peut que le matériau ne soit pas suffisamment extrudé.*

Ajuster la largeur des lignes pour qu'elles s'adaptent à un nombre suffisant de parois
----
Lorsque vous imprimez des objets mécaniques qui doivent être minces mais solides, vous vous heurtez régulièrement au problème que votre pièce n'est pas un multiple net et régulier de la largeur de la ligne. Si ce n'est pas un multiple pair, Cura réduira normalement le flux de certaines lignes en raison du paramètre [Compenser les chevauchements de paroi](../shell/travel_compensate_overlapping_walls_enabled.md). Cela modifie le débit à travers la buse, ce qui nuit à la qualité visuelle. S'il s'agit d'un multiple net de la largeur de la ligne mais pas d'un nombre pair, l'une des parois sera réduite à 0.

La production de contours nets avec des lignes paires peut rendre l'impression plus forte et plus belle. L'une des compétences principales de tout utilisateur expert de Cura est de pouvoir modifier la largeur de la ligne de manière à ce que le nombre de contours souhaité remplisse l'impression.

![Largeur de ligne par défaut, lorsque les contours ne sont pas ajustés et que certaines lignes sont plus épaisses que d'autres](../../../articles/images/line_width_fit_bad.png)
![Réduire la largeur de la ligne permet de l'ajuster uniformément](../../../articles/images/line_width_fit_good_small.png)
![Augmenter la largeur de la ligne fonctionne également](../../../articles/images/line_width_fit_good_large.png)

Maintenir le flux constant
----
Les grandes fluctuations de débit sont parfois problématiques pour les imprimantes FDM. La chambre de la buse maintient une partie du matériau sous pression, ce qui retarde le débit réel à la sortie de la buse. Il faut un certain temps pour que le débit augmente ou diminue. Les imprimantes équipées d'un système Bowden pour alimenter le filament ont également un effet de ressort dans le tube Bowden, ce qui aggrave encore l'effet. Par conséquent, vous obtiendrez une sous-extrusion lorsque vous passerez à un débit plus élevé et une surextrusion lorsque vous passerez à un débit plus faible. C'est pourquoi il est bon de maintenir le débit aussi constant que possible.

La largeur de la ligne influence grandement le débit. Il est conseillé de garder les largeurs des lignes proches les unes des autres et proches de la taille de la buse. Si la largeur de la ligne est importante, vous pouvez aussi envisager d'ajuster la vitesse d'impression afin de maintenir le débit plus constant. Cela permettra d'améliorer la précision dimensionnelle de votre impression.
