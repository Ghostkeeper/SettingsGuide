Vitesse de paroi en porte-à-faux
====
Ce paramètre permet de régler la vitesse à laquelle une [paroi en surplomb](wall_overhang_angle.md) est imprimée. La vitesse est définie comme un rapport de leur vitesse d'impression normale, qui est soit la [Vitesse de la paroi extérieure](../speed/speed_wall_0.md) soit la [Vitesse de la paroi intérieure](../speed/speed_wall_x.md).

L'impression en surplomb à des vitesses plus faibles peut être très efficace pour réduire l'affaissement. Cela a un certain nombre d'effets positifs sur votre impression.
* Les parois ont plus de temps pour se fixer aux parois adjacentes de la couche précédente. Cela les aide à mieux se tenir debout, ce qui réduit l'affaissement.
* Si la vitesse de votre ventilateur est élevée, les ventilateurs ont plus de temps pour refroidir le filament. Il se solidifie ainsi plus rapidement. Si la vitesse d'impression est élevée, le matériau a plus de temps pour s'affaisser.
* Le matériau en surplomb est toujours relié à une perle sortant de la buse. Lorsque l'impression est plus lente, la buse reste plus proche pendant la solidification, ce qui signifie que la traction de la buse sur le matériau est plus efficace pour maintenir le bourrelet en hauteur pendant qu'il se solidifie.

Toutefois, l'impression en surplomb à des vitesses plus faibles (ou différentes vitesses peuvent également avoir des effets négatifs) :
* L'impression sera évidemment plus longue à réaliser.
* La bordure où la vitesse d'impression est différente peut être très visible à l'extérieur. Cela introduit une bordure visible dans votre impression qui peut ne pas être souhaitable.
* En réduisant la vitesse, il y aura brièvement une certaine surexpulsion de la buse en raison de la haute pression dans la chambre de la buse. Cela peut entraîner des blips ou aggraver la qualité du surplomb. En augmentant la vitesse, il y aura une certaine sous-extrusion. En général, cette technique fonctionne mieux pour les grandes surfaces de surplomb que pour les petites.
