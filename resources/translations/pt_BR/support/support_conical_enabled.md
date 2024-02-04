Ativar suportes cônicos
====
Se esse parâmetro for ativado, a estrutura de suporte não será mais completamente vertical nas laterais.O suporte terá uma forma cônica, tornando -se menor ou maior.

![O apoio se torna menor para baixo](../../../articles/images/support_conical_enabled.png)

![O apoio está crescendo para baixo](../../../articles/images/support_conical_angle_neg10.png)

O suporte em si será inclinado por um certo [ângulo](support_conical_angle.md).No caso de um ângulo negativo, o suporte aumenta para baixo, o que o torna muito mais estável.Com ângulos positivos, ele diminuirá.Isso economiza muito material e tempo de impressão.Para impedir que o suporte se torne instável, uma [largura mínima](support_conical_min_width.md) também pode ser definida para o suporte.

O suporte cônico é o parâmetro mais poderoso para ponderar entre o tempo de impressão e a estabilidade do suporte.Existem dois casos principais de uso de suporte cônico:
* Para salvar o material e o tempo de impressão.O suporte cônico pode economizar facilmente metade do material necessário para o suporte e, por extensão, metade do tempo gasto na impressão.Esta solução é particularmente eficaz no caso de grandes volumes de suporte, para impressões grandes.
* Para tornar o suporte mais estável usando um ângulo negativo.Se a sua impressão tiver pequenas características de altura que exijam suporte, normalmente produzirá [Tours] muito alto (support_use_towers.md) que tendem a cair durante a impressão.Com um suporte cônico, essas estruturas de suporte alto e fino podem ser estendidas na parte inferior.Isso lhes dá alguma estabilidade adicional.No entanto, a impressão desse suporte levará mais tempo porque requer mais material.

Quando o [suporte do suporte](support_type.md) está definido para colocar o suporte apenas na bandeja de impressão, o suporte cônico permite estender -se ao redor do modelo para continuar apoiando o modelo nos locais que estão em outras partes do modelo.O suporte sempre descansará apenas na bandeja de impressão, mas, devido à sua forma, agora pode atingir as áreas salientes nos cantos que não seriam apoiados de outra forma.

Esse recurso é uma versão um pouco mais simples e menos intrusiva de <!-se Cura_version> = 4.7-> [suporte arborente](support_structure.md) <!-endif-> <!-se Cura_version <4.7: [suporte arborescente](. ./Experimental/support_tree_enable.md)->.Os suportes da arborescente têm as mesmas vantagens que o apoio cônico.No entanto, os suportes da árvore usam um algoritmo completamente diferente e se beneficiam de maior liberdade na maneira como o suporte é construído, enquanto o apoio cônico permanece mais fiel ao algoritmo da geração de apoio comum.Isso significa que os parâmetros de suporte comuns tendem a funcionar melhor quando usados ​​com suporte cônico, mas que eles terão que ser ajustados significativamente para os suportes de árvores.As estruturas das árvores tendem a economizar mais material e tempo de impressão, mantendo a confiabilidade da impressão.