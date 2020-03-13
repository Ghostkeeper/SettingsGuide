Certains modèles, en particulier ceux qui sont destinés à des techniques de fabrication comme le moulage par injection, ont tendance à présenter des cavités internes qui ne sont pas visibles. Si ce paramètre est activé, Cura supprime ces cavités internes.

![Ce modèle a un trou au centre](../../../articles/images/meshfix_union_all_remove_holes_disabled.png)
![Avec ce paramètre activé, le trou est supprimé](../../../articles/images/meshfix_union_all_remove_holes_enabled.png)

Les cavités à l'intérieur peuvent être conçues pour économiser de la matière, mais avec l'impression en 3D, certaines contraintes font que ces modèles s'impriment moins bien. Par exemple, les imprimantes 3D ne fonctionnent pas bien avec des parois minces qui ne sont pas un multiple de la largeur de la ligne, et la peau supérieure a tendance à s'affaisser si elle n'est pas soutenue par un remplissage. Il est généralement préférable de faire un maillage solide et de laisser le trancheur décider de la manière de le remplir. Ce paramètre de fixation du maillage vous permet de le faire sans avoir à modifier le maillage.

Cura ne regardera qu'horizontalement si une cavité est complètement fermée. Il ne verra pas si une cavité est accessible par le haut ou par le bas. La différence peut toujours être visible du haut ou du bas.
