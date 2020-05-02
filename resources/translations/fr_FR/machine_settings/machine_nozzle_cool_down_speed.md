Vitesse de refroidissement
====
Ce réglage indique à Cura la vitesse à laquelle votre buse se refroidit lorsqu'elle n'est pas chauffée. Il sert à prédire quand il faut commencer à pré-refroidir la buse avant de changer d'extrudeuse.

![Les buses commencent à chauffer à l'avance avant de changer d'extrudeuse](../images/temperature_regulation_fr.svg)

Lorsqu'il change d'extrudeuse, Cura commence à pré-refroidir la buse active juste avant qu'elle ne soit terminée, afin qu'elle suinte un peu moins en attendant. Cura essaiera également de prédire la quantité de refroidissement de la buse lorsqu'elle était inactive. De cette façon, il sait de combien de temps il aura besoin pour la réchauffer par la suite.

Si la buse refroidit effectivement plus vite que ce que ce réglage indiqué, la buse sera à la température de veille plus vite que ce que Cura prévoit. Par conséquent, le réchauffement de la buse peut prendre plus de temps que prévu par Cura, et l'imprimante attendra, au niveau de l'interrupteur de la buse, que celle-ci se réchauffe davantage.

Si la buse se refroidit plus lentement que ce que ce réglage indique, il est possible qu'elle soit encore chaude lorsque Cura envoie une commande de préchauffage, ce qui la fait chauffer trop vite. Elle sera à une température d'impression pendant un certain temps avant que ce soit au tour de la buse d'imprimer. Pendant ce temps, elle suinte un peu et le plastique se dégrade un peu plus.

La vitesse de refroidissement réelle n'est pas un taux constant en degrés par seconde. Elle dépendra plus probablement de la différence entre la température actuelle de la buse et la température du volume de production. Ainsi, il se refroidira plus rapidement lorsqu'il est chaud, et plus lentement lorsqu'il s'approchera de la température d'attente. Si vous réglez ce paramètre, essayez de le régler en mesurant le temps de refroidissement entre la [température finale d'impression](../material/material_final_print_temperature.md) et la [température d'attente](../material/material_standby_temperature.md). C'est la piste la plus importante que Cura tentera de prévoir. Pour les petits tirages, vous pouvez augmenter légèrement la vitesse de refroidissement afin d'ajuster la température pour qu'elle reste chaude plus souvent.

*Comme il s'agit d'un réglage de la machine, ce réglage n'est normalement pas visible dans la liste des paramètres.*

