Apoio à arorescente
====
Os suportes da Arborescent oferecem uma abordagem alternativa ao apoio do modelo que a técnica de suporte comum.O suporte à arorescente gera uma estrutura ramificada que começa na bandeja de impressão com uma pequena base, mas que se desenvolve para as partes que precisam ser suportadas.

![Uma estrutura em forma de árvore suporta saliência](../../../articles/images/support_structure_tree.png)

Os suportes da arborescente possibilitam os obstáculos durante o crescimento em direção a áreas de saliência.Na medida do possível, a árvore empurrará da bandeja de impressão para cima para evitar cicatrizes na superfície em que o suporte repousa.Se isso não for possível, a árvore repousará na superfície do modelo o mais próximo possível de sobrecarregar para minimizar o tempo e o uso do material.Os galhos do apoio da árvore são limitados pelo [ângulo dos ramos do suporte da arvoridade](../support/support_tree_angle.md) para que eles não produzam um corpo muito íngreme para si.Isso limita a capacidade de crescimento em torno dos obstáculos e também determina a altura na qual os troncos começarão a ramificar.

O apoio da árvore é oco por padrão.No entanto, os parâmetros de suporte comuns sempre se aplicam à área demarcada pelos ramos da árvore.Em particular, a [densidade do suporte](../support/support_infill_rate.md) pode ser usada para dar ao suporte maior resistência estrutural.Como a natureza dos suportes do arborescente é muito irregular, eles normalmente têm grande rigidez para cumprir suas funções.

Os suportes da arorescente têm várias vantagens em comparação com um suporte normal, para citar apenas alguns:
* O suporte à arorescente geralmente usa muito menos material que o suporte comum.Entre 25 e 50 % do uso do material é típico.Isso economiza muito tempo e custos em termos de.
* Quando impresso com o mesmo material que a impressão, a saliência tende a ser mais estética com um suporte em forma de árvore.
* O suporte em forma de eixo é mais fácil de remover do que o suporte comum.
* O suporte em forma de eixo deixa menos cicatrizes na superfície do que o suporte normal, porque permite que a bandeja de impressão seja alcançada ao redor do modelo.

No entanto, isso também tem algumas desvantagens:
* O suporte em forma de árvore leva mais tempo para cortar.Paciência será necessária, especialmente com modelos grandes.
* Existem muitas interrupções no fluxo quando os maiores ramos são impressos, o que torna o suporte à arborescente impróprio para imprimir com materiais difíceis de extratar, como PVA ou materiais flexíveis.
* O suporte à arorescente não funciona muito bem para apoiar certos modelos mecânicos.Em particular, tende a colocar poucos ramos para apoiar saliências planas e inclinadas.

Embora o suporte à árvore possa ser ativado ao mesmo tempo que o suporte comum, geralmente não é desejável.Os dois tipos de suporte se reunirão e causarão uma superextrusão.