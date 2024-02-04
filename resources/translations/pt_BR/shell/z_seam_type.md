Alinhamento da junta Z
====
Este parâmetro permite que você escolha onde a costura de cada esboço é colocada.Estão disponíveis várias opções que permitem controlar o local onde a costura é colocada para minimizar seu impacto ou permitir que você o remova mais facilmente durante o pós-processamento.

A costura é o lugar onde o contorno começa e termina a impressão.Mesmo que o caminho do bico seja um círculo fechado, há uma costura no local onde a extrusão começa e termina porque o processo de impressão nunca é completamente preciso.Com essa configuração, a visibilidade da costura pode ser minimizada escondendo -a em algum lugar ou distribuindo -a.

Usuário especificado
----
! [Especificado pelo usuário](../../Artigos/Images/Z_seam_type_user.png)

Esta opção permite que você escolha um lugar manualmente.A costura será colocada no canto mais próxima do local escolhido.Em geral, os cantos estão, portanto, muito próximos um do outro, o que permite cortar facilmente a costura.Isso também permite controlar com precisão o local onde a costura deve ser colocada.

Por padrão, um local na parte traseira da impressora é escolhido.A idéia é que os usuários geralmente deixem a parte frontal de seus modelos voltados para a frente da impressora, para que um local traseiro oculte melhor a costura.

Le Plus Court
----
! [Le Plus Court](../../../Artigos/Images/Z_seam_type_shorstest.png)

Essa opção simplesmente minimiza o comprimento dos movimentos na costura, sem fazer nenhum esforço para colocá -lo em um local específico.Como a jornada é mais curta, você economizará um pouco de tempo em viagens.A costura também será um pouco menor, porque menos escorrendo será colocada no local onde o bico pousa no contorno.

A preferência desejada do canto é sempre mantida escolhendo um canto próximo ao local onde está o bico.O canto mais próximo não é escolhido, mas uma preferência ponderada é usada para minimizar um pouco a viagem, mas também para usar um canto apropriado para o parâmetro [preferência da junta do ângulo](Z_seam_corner.md).

Aleatório
----
! [Random](../../../Artigos/Images/Z_seam_type_random.png)

Um local aleatório ao redor do perímetro é escolhido para costura.Esse local aleatório é modificado em cada camada, para que a costura se espalhe quase uniformemente ao redor do modelo.Como as costuras das diferentes camadas não estão alinhadas, a costura será quase visível.No entanto, a superfície parecerá um pouco suja em geral.

O canto mais agudo
----
! [O canto mais agudo](../../Artigos/Images/Z_seam_type_sharpest.png)

A costura será colocada no canto mais agudo de todo o contorno, dependendo da preferência da esquina escolhida no parâmetro [preferência pela junta de ângulo](Z_seam_corner.md).Isso pode levar a viagens mais longas, mas garante que a costura seja oculta ou exposta ao máximo, dependendo da preferência definida para os cantos.


