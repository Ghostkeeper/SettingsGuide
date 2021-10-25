G-Code de démarrage
====
Avec ce paramètre, il est possible d'écrire un peu de G-Code qui sera exécuté au tout début de chaque impression. Grâce à ce G-Code, l'imprimante peut être configurée pour être prête à l'impression.

Voici quelques exemples de choses qui sont généralement exécutées dans le g-code de départ :
* Amorçage de la ou des buses.
* Chauffage du plateau d'impression.
* Chauffage de la (des) buse(s).
* S'assurer que la bonne extrudeuse est sélectionnée.
* Configurer les ventilateurs, les accélérations ou les saccades.
* Mise à niveau automatique du plateau.
* Configurer l'avance linéaire.

Pour une liste assez complète des g-codes disponibles que vous pouvez écrire ici, consultez le [RepRap Wiki](https://reprap.org/wiki/G-code).

Références aux réglages
----
Lorsque vous modifiez le code g de démarrage, vous pouvez vous référer aux valeurs d'autres paramètres. Ceci utilise une certaine syntaxe. Les paramètres sont désignés par leur *clé*. Cette clé est un nom interne à Cura. Elle n'est pas visible dans l'interface utilisateur. Pour une liste complète de toutes les clés, consultez [ce document](https://github.com/Ultimaker/Cura/blob/master/resources/definitions/fdmprinter.def.json) dans le code source de Cura.

La syntaxe pour obtenir la valeur d'un paramètre global est la suivante :

`{setting_key}` (clé de réglage)

En d'autres termes, écrivez la clé du lieu entre parenthèses. Vous obtiendrez ainsi la valeur globale d'un réglage. De nombreux réglages peuvent cependant être différents pour chaque extrudeuse. Ils doivent être référencés comme suit :

`{setting_key, #}`

Ici, à la place du symbole "#", vous devez écrire le numéro de l'extrudeuse dont vous voulez obtenir le réglage. Les extrudeuses commencent à compter à partir de 0. Les réglages globaux peuvent également être obtenus en spécifiant une extrudeuse, mais ils seront les mêmes pour toutes les extrudeuses. Lorsque vous essayez d'obtenir une température spécifique à l'extrudeuse sans spécifier le numéro de l'extrudeuse, vous obtiendrez le réglage global par défaut de votre imprimante, avant qu'un profil de matériau ou quoi que ce soit n'ait été appliqué (puisque les matériaux sont spécifiques à l'extrudeuse).

Vous pouvez utiliser ces références par exemple pour préchauffer à la bonne température, ou pour régler les accélérations. Voici quelques exemples :

`M104 S{material_print_temperature_layer_0, 0} ;prechauffage`

`M140 S{material_bed_temperature_layer_0} ;Chauffage plateau`

`M204 P{acceleration_print, 0} T{acceleration_travel, 0}`

`M205 X{jerk_print, 0}`

Faites attention aux vitesses. Le code G accepte normalement la vitesse d'avance en millimètres par *minute*, alors que les réglages sont indiqués en millimètres par *seconde*. Il n'est pas possible de sélectionner la vitesse d'avance correcte pour le moment. Il est impossible de faire des calculs dans ces références.

Autres informations
----
Par la même syntaxe que les références aux paramètres, certaines informations auxiliaires sont également disponibles :

* `{time}` fait référence à l'heure locale actuelle du jour où il a été découpé.
* `{date}` fait référence à la date à laquelle il a été découpé.
* `{day}` se réfère au jour de la semaine où il a été découpé.
* `{initial_extruder_nr}` fait référence à l'extrudeuse avec laquelle l'impression commencera.
<!--if cura_version>=4.12-->
* `{material_id}` fait référence à un identifiant unique du matériau actif. Spécifiez l'extrudeur de la même manière que les autres paramètres.
* `{material_name}` fait référence au nom de la matière active. Il s'agit généralement du nom que vous verrez sur un site Web vendant cette matière.
* `{material_type}` fait référence à la classe de matériau actif, comme PLA ou ABS.
* `{material_brand}` fait référence au fabricant de la matière active.
<!--endif-->

Chauffage avant le démarrage G-Code
----
Cura émettra automatiquement des commandes de chauffage avant que votre G-Code de démarrage ne commence. De cette façon, votre G-Code de démarrage ne doit pas tenir compte du fait que la buse doit chauffer. Vous pouvez immédiatement commencer à amorcer la buse. Si votre  G-Code de démarrage contient une référence à une température quelconque (pour la buse ou le plateau), celle-ci sera désactivée (pour la buse ou le plateau, respectivement).

*Ce réglage est un réglage machine, il n'apparaîtra donc pas dans la liste normale des réglages. Il peut être modifié en allant dans la liste des imprimantes dans l'écran des préférences et en cliquant sur "Réglages machine".*

