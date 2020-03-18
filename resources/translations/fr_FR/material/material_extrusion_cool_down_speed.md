Modificateur de vitesse de refroidissement de l'extrusion
====
Si la fonction [Auto Temperature](../experimental/material_flow_dependent_temperature.md) est activée, la température d'impression sera ajustée en fonction de la quantité de matière extrudée.

Lorsque le matériau est chauffé à l'intérieur de la chambre de la buse, la chaleur est évacuée de la buse. L'extrusion plus rapide de la matière a tendance à retirer plus de chaleur de la buse. Si la sonde de température n'est pas exactement à l'extrémité de la buse, la buse a une température légèrement plus basse pendant l'extrusion de la matière qu'à l'arrêt, même avec un bon régulateur PID.

Ce réglage décrit la quantité de chaleur perdue dans la buse pendant l'impression. La chaleur supplémentaire perdue par l'extrusion sera alors compensée par l'augmentation de la température d'impression souhaitée à partir du code g. La valeur du réglage dépend de la conception de la buse, de la capacité thermique du matériau imprimé et de la vitesse d'extrusion.
