Ordre d'étirage monotone
====
Normalement, Cura ordonne les lignes d'étirage de telle sorte que la distance de déplacement entre elles soit faible. Si ce paramètre est activé, il ordonnera les lignes d'étirage de telle sorte que les lignes adjacentes soient toujours imprimées en se chevauchant dans la même direction.

Les lignes d'étirage sont par défaut beaucoup plus fines que la buse avec laquelle elles sont imprimées, de sorte que les lignes se chevauchent beaucoup avec les lignes voisines. Ce chevauchement donne aux lignes une légère inclinaison, ce qui fait qu'elles réfléchissent la lumière différemment dans différentes directions. Si les lignes adjacentes se chevauchent différemment, cette réflexion change. Vous pouvez le voir dans le résultat final. Il donne à différentes zones de la surface une brillance différente. L'impression dans un ordre monotone garantit que le chevauchement est le même sur toute la surface, de sorte qu'il n'y a pas de différence dans la façon dont elle reflète la lumière. La surface paraît donc plus homogène et plus lisse.

Cependant, contrairement à [l'équivalent pour les lignes du haut et du bas](skin_monotonic.md), cet effet est pour l'étirage est annulé par un autre effet. L'étirage a un débit si faible que le changement de débit provenant de l'impression ordinaire est très important. Cela rend la couche d'étirage plus épaisse lorsqu'elle commence à imprimer, et laisse toujours une bordure visible là où l'impression a été interrompue. Une option monotone ne supprimera pas ces bordures. Bien que la surface puisse sembler légèrement plus lisse, en pratique, l'impression des lignes d'étirage en ordre monotone est largement inefficace, à moins que votre imprimante ne dispose d'un contrôle très précis du débit.

L'ordre monotone augmentera légèrement la longueur des déplacements, mais cet effet est très minime.

Pour obtenir une surface lisse, pensez à associer ce paramètre au paramètre [Mode de détours](../travel/retraction_combing.md) pour éviter les peaux, et peut-être à activer la [Hauteur du décalage en Z](../travel/retraction_hop.md).


