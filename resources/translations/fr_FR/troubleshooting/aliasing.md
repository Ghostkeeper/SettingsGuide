Les moteurs pas à pas tournent par pas discrets. Leur capacité à rester en position entre ces pas est limitée. La taille des pas des moteurs sert de limite à la résolution que l'imprimante peut atteindre. Lors de l'impression de murs qui sont presque, mais pas tout à fait, alignés sur l'axe X ou Y, cette résolution se traduit parfois par un motif de lignes.

![Le motif d'aliasing apparaissant sur les côtés de cet objet](../../../articles/images/aliasing.jpg)

La résolution d'un moteur pas à pas dans une imprimante 3D grand public typique est de l'ordre de 50 à 200 pas par millimètre. La taille de chaque pas est donc de l'ordre de 10 micromètres. Si une ligne est tracée presque parallèlement à l'autre axe, disons à 0,5° de l'orthogonal, alors un tel pas se produira tous les 1,15 mm le long de la ligne. Ce pas est en soi trop petit pour être visible, mais les vibrations sont visibles, surtout si elles résonnent avec la fréquence naturelle du cadre.

Prévention
----
Les moteurs pas à pas peuvent choisir entre plusieurs stratégies pour faire tourner leur arbre, mais c'est un compromis entre la résolution, le couple et le bruit. Certains microprogrammes ajustent automatiquement ces paramètres en fonction de la vitesse de déplacement. Certains microprogrammes vous permettent également d'ajuster cela à partir du code G. Par exemple, la commande "M350" du g-code peut être placée dans le g-code de départ pour le configurer manuellement. Cura (actuellement) n'a pas de méthode pour configurer cela automatiquement en fonction de la vitesse ou de la structure.

La manière la plus fiable d'éviter ce phénomène est cependant d'ajuster le modèle de telle sorte que l'aliasing ne soit pas visible. Faites pivoter votre modèle de manière à ce que l'effet d'aliasing ne se produise pas. Si votre modèle présente une paroi (presque) droite, assurez-vous qu'elle est soit complètement alignée avec les axes, soit inclinée de plusieurs degrés par rapport à elle.
