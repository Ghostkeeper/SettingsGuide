G-Code de fin
====
Avec ce paramètre, il est possible d'écrire le g-code qui sera exécuté à la toute fin de chaque impression. Grâce à ce code g, l'imprimante peut éteindre ses composants et se nettoyer après l'impression.

Voici quelques exemples de choses qui sont généralement exécutées dans le g-code final :

* Rétraction du matériel.
* Refroidir la ou les buses.
* Refroidissement de la plaque de montage.
* Éteindre les ventilateurs.

Pour une liste assez complète des g-codes disponibles que vous pouvez écrire ici, reportez-vous au [RepRap Wiki] (https://reprap.org/wiki/G-code).

Références aux paramètres
----
Lorsque vous modifiez le code g de fin, vous pouvez vous référer aux valeurs d'autres paramètres. Ceci utilise une certaine syntaxe. Les paramètres sont désignés par leur *clé*. Cette clé est un nom interne à Cura. Elle n'est pas visible dans l'interface utilisateur. Pour une liste complète de toutes les clés, consultez [ce document] (https://github.com/Ultimaker/Cura/blob/master/resources/definitions/fdmprinter.def.json) dans le code source de Cura.

La syntaxe pour obtenir la valeur d'un paramètre global est la suivante :

`{setting_key}` (clé de réglage)

En d'autres termes, écrivez la clé du lieu entre parenthèses. Vous obtiendrez ainsi la valeur globale d'un réglage. De nombreux réglages peuvent cependant être différents pour chaque extrudeuse. Ils doivent être référencés comme suit :

`{setting_key, #}`

Ici, à la place du symbole "#", vous devez écrire le numéro de l'extrudeuse dont vous voulez obtenir le réglage. Les extrudeuses commencent à compter à partir de 0. Les réglages globaux peuvent également être obtenus en spécifiant une extrudeuse, mais ils seront les mêmes pour toutes les extrudeuses. Lorsque vous essayez d'obtenir une température spécifique à l'extrudeuse sans spécifier le numéro de l'extrudeuse, vous obtiendrez le réglage global par défaut de votre imprimante, avant qu'un profil de matériau ou quoi que ce soit n'ait été appliqué (puisque les matériaux sont spécifiques à l'extrudeuse).

Vous pouvez par exemple utiliser ces références pour refroidir à une température de veille, ou rétablir l'accélération et la secousse par défaut de l'imprimante. Voici quelques exemples :

`M104 T0 S{material_standby_temperature, 0} ;stand-by for the next print`

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
