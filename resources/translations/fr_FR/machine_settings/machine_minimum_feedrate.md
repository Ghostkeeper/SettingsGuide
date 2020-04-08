Vitesse minimale
====
Le microprogramme Marlin pour imprimantes 3D, dont la plupart des microprogrammes d'imprimantes sont dérivés, a une vitesse minimale pour tous ses mouvements. Ce paramètre indique quelle est cette vitesse minimale pour le microprogramme de votre imprimante.

La vitesse minimale est un ajustement destiné à éviter les erreurs dans le microprogramme dues à des divisions par zéro. Le microprogramme doit calculer les intervalles de temps entre les pas afin d'envoyer un signal aux moteurs avec le bon timing. Si le moteur doit se déplacer à une vitesse de 0 (c'est-à-dire s'arrêter), il s'agit d'un intervalle de temps infini, que le microprogramme ne peut pas bien gérer. Cela ne s'applique que si aucun des moteurs de l'imprimante ne tourne réellement. Par exemple, en se déplaçant dans la direction X, le moteur qui contrôle l'axe Y ne tourne toujours pas, mais en raison de la complexité des moteurs pas à pas, la vitesse d'avance minimale ne s'applique pas ici.

Cura utilise cette vitesse d'avance minimale pour produire des estimations de temps correctes. Elle est appliquée lors de l'accélération au début de l'impression ou après une pause, et lors de la décélération jusqu'à l'arrêt à la fin d'une impression ou avant une pause.

*Comme il s'agit d'un réglage de la machine, ce paramètre n'est normalement pas visible dans la liste des paramètres.*
