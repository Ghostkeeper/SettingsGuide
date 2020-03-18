Débit de paroi du pont
====
Ce réglage permet d'ajuster la quantité de matériau qui est extrudé pour imprimer les parois de pontage.

La réduction de la quantité de matériau réduira effectivement la largeur des lignes des parois qui forment un pont. Avec une largeur de ligne réduite, le rapport surface/masse des lignes est plus important, ce qui leur permet de refroidir plus rapidement et les empêche de s'affaisser autant.

Toutefois, une réduction trop importante du débit entraînera une grande modification du débit, surtout lorsqu'elle est combinée à une [vitesse d'impression plus faible](bridge_wall_speed.md). En réalité, le matériau ne pourra pas changer son débit très rapidement, ce qui fait que les lignes seront un peu plus épaisses que prévu lorsque le débit est ralenti, et un peu plus fines que prévu lorsque le débit est accéléré. Le premier de ces effets peut être compensé par un certain [cabotage](bridge_wall_coast.md), mais cela nécessite un réglage minutieux.
