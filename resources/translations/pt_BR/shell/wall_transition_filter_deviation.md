Filtro de transição de Marge da parede
====
Alguns modelos têm peças finas que oscilam em torno do limite, onde diferentes números de cabos são usados.Isso pode alternar o número de cabos em uma direção ou outra, mesmo que a largura real da sala não varie muito.Essa alternância prejudica a qualidade da impressão, exigindo muitas mudanças de fluxo e adicionando mais viagens.Ao usar esse recurso, as transições são excluídas se tivessem alternadas.

Quando uma transição é excluída, algumas linhas podem se tornar temporariamente muito grandes ou muito finas.Este parâmetro limita as transições que são filtradas limitando a largura ou a delicadeza da linha.

![Com uma margem baixa, ele alterna entre 2 e 3 cabos](../../../articles/images/wall_transition_filter_off.png)

![Com uma margem maior, ele não alterna mais](../../../articles/images/wall_transition_filter_on.png)

Para ser preciso, as linhas podem se tornar mais finas que a [largura mínima da linha de parede](min_wall_line_width.m) dessa margem, se ela permitir vir e vir entre o número diferente de paredes.Da mesma forma, as linhas estão autorizadas a se tornar um pouco mais ampla dessa margem, mesmo que uma parede adicional da largura mínima da linha de parede possa ter sido integrada.

Este filtro tem como objetivo resolver um problema atual com peças finas usando malhas 3D de baixa resolução.O modelo 3D, composto de triângulos planos, não pode representar exatamente uma curva, mas apenas se aproximar.A curva terá bordas, com superfícies planas entre eles.Quando você modela uma peça curva de largura constante, é importante que as bordas externas estejam alinhadas com as bordas internas.Se não for esse o caso, a largura do anel varia ligeiramente, o que pode causar o efeito ilustrado acima.Se for esse o caso, o filtro de transição deve impedir que o efeito seja muito grande.

Aumentar a margem evita a criação de pequenos segmentos de linha em alguns casos.Este método é mais rápido para imprimir e pode dar uma aparência mais suave à superfície.No entanto, isso também torna possível criar linhas mais amplas, o que pode não ser bem extrudado pelo seu bico.Ao imprimir modelos de baixa resolução com peças finas, o aumento da margem pode ajudar a melhorar a qualidade.Com materiais difíceis, é melhor permanecer no lado da segurança.

** Este parâmetro não se aplica apenas às paredes normais, mas também a paredes de contorno adicionais, paredes de suporte, paredes de enchimento e padrões concêntricos. **