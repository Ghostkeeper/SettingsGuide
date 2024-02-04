Resolução de colisão de suporte à arorescente
====

Uma grande desvantagem do suporte à árvore é que leva muito tempo para calculá -lo quando ativado.A maioria dos cálculos necessários para o apoio da árvore está relacionada aos galhos da árvore para evitar colisões com a malha.Este parâmetro determina a precisão desses cálculos de prevenção de colisões.Aumentar essa resolução (baixa precisão) economizará muito tempo nos cálculos, mas também aparecerá o suporte como triturado quando estiver próximo da malha.

![Baixa resolução (0,2 mm) leva a uma queda nos ramos](../../../articles/images/support_tree_collision_resolution_lo.png)

![Alta resolução (0,02 mm) cria ramificações lisas](../../../articles/images/support_tree_collision_resolution_hi.png)

O contexto técnico deste parâmetro é o seguinte.Para evitar colisões com o objeto impresso quando o suporte da árvore for ativado, o Cura calculará os volumes tridimensionais em que os centros dos galhos da árvore não podem entrar.Esse volume é calculado para cada possível diâmetro dos galhos da árvore, que leva muito tempo.O número de diâmetros de ramos possíveis aumenta consideravelmente à medida que a árvore se torna maior e com grandes valores para [ângulo de diâmetro dos ramos de suporte da arborescente](support_tree_branch_diameter_angle.md).Por esse motivo, o diâmetro é arredondado para os múltiplos mais próximos deste parâmetro de resolução.No entanto, em certos pontos da altura da árvore, o volume de colisão que o ramo precisa evitar se apegar à sala pode variar fortemente, dependendo do diâmetro de um ramo, que repentinamente requer mais espaço para que o ramo possa ser posicionado.Isso dá à árvore uma aparência desfiada.

Ao aumentar esse parâmetro, o cálculo levará menos tempo na cura.Isso também tornará o suporte mais desfiado, o que compromete sua solidez e aumentará o risco de que o suporte quebre durante a impressão, o que pode causar falhas na impressão.