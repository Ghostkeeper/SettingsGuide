Distância do filtro de transição da parede
====
Alguns modelos incluem peças finas que estão no limite, onde diferentes números de cabos são usados.Isso pode alternar o número de cabos para frente e para trás, mesmo que a largura real da sala não varie muito.Essa alteração prejudica a qualidade da impressão, exigindo muitas mudanças de fluxo e adicionando mais viagens.Graças a essa funcionalidade, se as transições na frente e nas costas forem realizadas a uma certa distância, essas transições serão excluídas.

![Filtro sem filtro, ele alterna entre 2 e 3 cabos.](../../../articles/images/wall_transition_filter_off.png)

![Com o filtro, ele não alterna mais](../../../articles/images/wall_transition_filter_on.png)

Quando uma transição é excluída, certas linhas podem se tornar temporariamente muito largas ou muito finas, excedendo assim a [largura mínima da linha de parede](min_wall_line_width.md).Afinal, houve uma transição para este local para se adaptar melhor à largura da sala.Sem essa transição, o número de cabos utilizados será menor ou maior do que o ideal, e a largura dessas paredes será ajustada de acordo.Isso é autorizado para a [margem do filtro de transição da parede](Wall_transition_Filter_Devionce.md).Se a largura das paredes varia muito, a transição não será excluída.

Este filtro tem como objetivo resolver um problema atual com peças finas usando malhas 3D de baixa resolução.O modelo 3D, composto de triângulos planos, não pode representar exatamente uma curva, mas apenas se aproximar.A curva terá bordas, com superfícies planas entre eles.Quando você modela uma peça curva de largura constante, é importante que as bordas externas estejam alinhadas com as bordas internas.Se não for esse o caso, a largura do anel varia ligeiramente, o que pode causar o efeito ilustrado acima.Se for esse o caso, o filtro de transição deve impedir que o efeito seja muito grande.

Ao aumentar a distância, evitamos a criação de pequenos segmentos de linha em alguns casos.Este método é mais rápido para imprimir e pode dar uma aparência mais suave à superfície.No entanto, isso também leva a uma largura de linha extrema em uma parte maior da impressão, o que pode não ser bem extrudado pelo seu bico.Ao imprimir modelos de baixa resolução com peças finas, o aumento da distância pode ajudar a melhorar a qualidade.Para materiais difíceis, é melhor permanecer do lado da segurança.

** Atualmente, este parâmetro não está visível para o usuário.O filtro só pode ser ajustado usando a [margem do filtro de transição da parede](Wall_Transition_Filter_Devionce.md).Afeta não apenas as paredes normais, mas também as paredes de contorno adicionais, as paredes de suporte, as paredes de enchimento e os padrões concêntricos **.