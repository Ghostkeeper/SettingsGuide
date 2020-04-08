
`M104 T1 S{material_standby_temperature, 1}`

`M204 P{machine_acceleration} T{machine_acceleration}`

Faites attention aux vitesses. Le code G accepte normalement la vitesse d'avance en millimètres par *minute*, alors que les réglages sont indiqués en millimètres par *seconde*. Il n'est pas possible de sélectionner la vitesse d'avance correcte pour le moment. Il est impossible de faire des calculs dans ces références.

Autres informations
----
Par la même syntaxe que les références aux paramètres, certaines informations auxiliaires sont également disponibles :

* `{time}` fait référence à l'heure locale actuelle du jour où il a été découpé.
* `{date}` fait référence à la date à laquelle il a été découpé.
* `{day}` se réfère au jour de la semaine où il a été découpé.
* `{initial_extruder_nr}` fait référence à l'extrudeuse avec laquelle l'impression commencera.

*Ce paramètre est un paramètre de machine, il n'apparaîtra donc pas dans la liste normale des paramètres. Il peut être modifié en allant dans la liste des imprimantes dans l'écran des préférences et en cliquant sur "Paramètres machine".*
