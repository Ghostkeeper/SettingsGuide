Use camadas adaptativas
====
As camadas adaptativas possibilitam ajustar localmente a espessura da sua impressão para otimizar o tempo e a qualidade da impressão de acordo com as características da superfície do modelo.As camadas serão mais finas quando as encostas estiverem baixas ou mais espessas quando as paredes são íngremes.O objetivo é imprimir rapidamente quando possível, continuando a imprimir em detalhes quando necessário.

![Com a "espessura da camada" diagrama de cores, você pode ver que coloca as camadas mais finas em azul e as camadas mais grossas em amarelo](../../../articles/images/adaptive_layer_height_enabled.png)

A altura das camadas é ajustada para que a distância horizontal entre as bordas das camadas permaneça constante.As superfícies rasas causam um grande deslocamento horizontal com um pequeno movimento vertical; portanto, é feito um pequeno movimento vertical para manter a constante do movimento horizontal.As superfícies íngremes causam uma pequena viagem horizontal com um grande movimento vertical, de modo que um grande deslocamento vertical seja feito para manter o movimento horizontal constante.Assim, o [efeito topográfico](../distúrbios/topografia.md) das camadas é mantido constante.A distância máxima entre duas camadas adjacentes é mantida a uma distância constante do parâmetro [tamanho da topografia das camadas adaptativas](Adaptive_Layer_Height_threshold.md).

Se o modelo possui superfícies rasas e superfícies íngremes na mesma altura, a espessura da camada será considerada a menor das espessuras da camada.Às vezes, isso torna a altura da camada desnecessariamente pequena, porque há uma superfície horizontal ao lado dela.Pode ser visto na captura de tela acima, bem como no meio da altura do silo à esquerda.

O uso de camadas adaptativas é altamente limitado para melhorar a qualidade da impressão.A altura da camada não deve se desviar de mais de uma [altura máxima autorizada em relação à camada base, em mm](Adaptive_Layer_Height_Variation.md) especificado em relação ao parâmetro original [altura da camada](./resolution/camada_height.md).Entre duas camadas adjacentes, a diferença na altura da camada não pode exceder um certo [tamanho dos estágios de variação das camadas adaptativas](Adaptive_Layer_Height_Variation_Step.md).A espessura da camada passa gradualmente de uma camada para outra, em vez de cortá -la repentinamente ao meio.

Camadas adaptativas podem reduzir consideravelmente o tempo de impressão sem sofrer de perda de qualidade de impressão ou mesmo melhorar a qualidade em alguns casos.O efeito de ajustar a espessura da camada é imenso.Na maioria dos casos, o tempo de impressão será consideravelmente reduzido, graças ao uso de camadas mais espessas quando o modelo é vertical.L '[efeito topográfico](../solucionamento de problemas/topografia.md) também é reduzido porque as camadas estão mais próximas horizontalmente.

No entanto, essa característica também pode introduzir vários problemas.
* Alterando a altura das camadas, outros parâmetros geralmente devem ser ajustados, como a temperatura do bico.As camadas adaptativas não ajustam automaticamente esses outros parâmetros.Isso pode causar a impressão abaixo do ideal, por exemplo, para saliências que seriam mais eficientes a uma temperatura de impressão mais baixa.
* Se a altura da camada for modificada em toda a camada para um pequeno elemento em algum lugar de uma pequena parte da camada, as bandas serão visíveis no restante da camada.
* As distâncias verticais também são involuntariamente ajustadas neste caso.Isso pode ter um efeito negativo na qualidade da impressão.Por exemplo, a espessura da [espessura da parte superior/abaixo](../top_bottom/top_bottom_thickness.md) geralmente será menor porque o Cura mantenha o parâmetro [camadas superiores](../top_bottom/top_layers.md) como sendo verdadeiro, e as fraldas se tornarão mais finas.Isso pode causar um efeito de travesseiro.Entre os parâmetros afetados que não podem mais estar corretos, podemos citar
  * [Espessura do topo](../top_bottom/top_thickness.md)
  * [Espessura abaixo](../top_bottom/bottom_thickness.md)
  * [Ângulo máximo da camada externa para expansão](../top_bottom/max_skin_angle_for_expass.md)
  * [Altura do estágio de enchimento progressivo](../preenchimento/gradual_infill_step_height.md)
  * [Barraca de suporte gradual do suporte](../suporte/gradual_support_infill_step_height.md)
  * [Espessura da camada de preenchimento](../preenchimento/refill_sparse_thickness.md)
  * [Espessura da camada de preenchimento de suporte](../support/support_infill_sparse_thickness.md)
  * [Distância z dos suportes](../support/support_z_distance.md)
  * [Espessura do teto de suporte](../Support/Support_Roof_Height.MD)
  * [Espessura da parte inferior do suporte](../Support/Support_Bottom_Height.MD)
  * [Ângulo de suporte de suporte](../support/support_angle.md)
  * [Altura da etapa de suporte](../Support/Support_Bottom_Stair_Step_Height.MD)
  * [Ângulo do telhado da torre](../support/support_tower_roof_angle.md)
  * [Ângulo do escudo de processamento](../dual/ooze_shield_angle.md)
  * [Ângulo máximo do modelo](../experimental/conical_overhang_angle.md)