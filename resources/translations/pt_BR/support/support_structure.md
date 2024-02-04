Estrutura de suporte
====
Com este parâmetro, você pode escolher o algoritmo a ser usado para criar as estruturas de suporte.Essas construções têm propriedades muito diferentes; portanto, a escolha de um algoritmo terá uma grande influência no gerenciamento da sua impressão.Existem duas opções disponíveis.

Normal
----
! [Suporte normal](../../../Artigos/imagens/support_type_everywhere.png)

É uma estrutura de suporte tradicional, a que a maioria das pessoas está acostumada.A estrutura é gerada sob as áreas pendentes e geralmente preenchida com um padrão que suporta diretamente as áreas de excesso.A partir daí, ele é depositado diretamente até atingir a bandeja de construção ou parte do modelo que a suporta.

A construção de suporte normal foi o valor padrão para a maior parte do histórico de impressão 3D e funciona da mesma maneira em todos os segmentos.Esta é a norma dourada, e não sem razão:
* Devido à sua estrutura robusta, com grandes áreas de contato no modelo e na bandeja de impressão, é muito confiável.É muito perdoador com configurações ruins ou uma impressora mal ajustada.
* Como a forma é simples, é rápido decidir.
* A estrutura de suporte certa é fácil de personalizar para um usuário, porque fica imediatamente claro quais arestas serão suportadas e quais não serão.

As desvantagens mais importantes vêm das mesmas propriedades:
* Devido a grandes áreas de contato, o suporte geralmente é difícil de remover e pode deixar cicatrizes importantes na superfície onde foi afetado.
* Embora seja estável, ele pode usar muito material e levar muito tempo para imprimir.Isso pode ser frustrado até certo ponto usando [faça a saliência imprimível](../experimental/conical_overhang_enabled.md).

Como o suporte será geralmente importante e amplo, é necessário um [padrão de suporte](support_pattern.md) para apoiar adequadamente a superfície.O padrão de enchimento em zig-zag pode ser usado para imprimir o suporte amplamente em uma única linha e para permitir uma retirada mais fácil.Outros modelos podem ser combinados com um [número de linhas da parede do suporte](support_wall_count.md) para tornar o suporte mais robusto.

Arborrescência
----
! [Suporte arborescent](../../../Artigos/Images/Support_structure_tree.png)

Com o suporte à arorescente, a estrutura de suporte começará pequena na bandeja de impressão e criará ramificações para as peças de impressão que precisam ser suportadas.

O apoio à arorescente pode evitar obstáculos durante o crescimento nas áreas de excesso, pois o suporte não precisa diminuir diretamente.Na medida do possível, o suporte repousará apenas na bandeja de impressão, para evitar a cura da superfície na qual o suporte repousa.Se não houver maneira entre a plataforma de impressão e a saliência, ela repousará em uma superfície o mais próxima possível da saliência, a fim de minimizar o uso do material.Os ramos do suporte arorescente são limitados pelo [ângulo dos ramos de suporte da arborescente](support_tree_angle.md), para que eles próprios não produzam muita saliência.Isso limita a capacidade de desenvolver em torno de obstáculos e também determina a altura na qual os troncos começarão a ramificar.

A construção do suporte da árvore tem várias grandes vantagens em comparação com o suporte normal:
* O suporte à árvore geralmente usa muito menos material que o suporte comum.Entre 25% e 50% do uso do equipamento é comum.Isso economiza muito tempo e reduz o custo da impressão.
* Devido à sua pequena superfície de contato, a saliência tende a ter uma aparência melhor ao usar o suporte à árvore.
* Também devido à pequena zona de contato, o suporte será mais fácil de remover.
* Deixa menos cicatrizes na superfície do que o suporte normal, porque pode atingir o modelo de bandeja de impressão em direção a saliência.

As principais desvantagens são, no entanto,:
* O corte leva muito mais tempo do que o suporte normal.Paciência será necessária, especialmente com modelos altos.
* Existem muitas interrupções no fluxo quando os maiores ramos são impressos, o que torna o suporte à arborescente impróprio para imprimir com materiais difíceis de extratar, como PVA ou materiais flexíveis.
* O apoio da árvore não funciona bem para apoiar certos modelos mecânicos.Em particular, tende a colocar poucos ramos para apoiar saliências planas e inclinadas.

O suporte à arorescente é oco por padrão.Os ramos terão um ponto pequeno; portanto, um padrão de enchimento não fornece suporte adicional para a superfície pendente da parte impressa.Devido à sua forma serrilhada, o suporte à árvore é normalmente bastante robusto.No entanto, os parâmetros de suporte comuns sempre se aplicam à área demarcada pelos ramos da árvore.A [densidade de suporte](support_infill_rate.md) pode ser usada para fornecer o suporte mais resistência estrutural.