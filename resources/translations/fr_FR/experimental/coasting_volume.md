Volume en roue libre
====
Ce paramètre détermine à quelle distance avant la fin du contour l'extrudeuse cessera d'alimenter le matériau. La longueur de la distance est cependant configurée en volume de matériau. Elle est plus étroitement liée au volume à l'intérieur de la chambre de la buse.

![Accostage 0.2mm³ de matière](../../../articles/images/coasting_enable.png)
![Accostage de 0,1mm³ de matière](../../../articles/images/coasting_volume_0_1.png)

L'augmentation du volume en roue libre fait que la buse s'arrête d'extruder plus tôt avant d'avoir fini le contour. Le résultat est qu'il y aura plus de sous-extrusion vers la fin. La fonction de l'impression en roue libre est de compenser la marque lorsque le contour est cousu, de sorte que l'augmentation du volume de roue libre peut compenser des marques plus grandes.

Cependant, une augmentation trop importante du volume en roue libre provoquera une forte sous-extrusion vers la fin du contour. Cela peut même entraîner une certaine sous-extrusion dans ce qui est imprimé après le contour, puisque la pression sur la buse est alors encore faible.
