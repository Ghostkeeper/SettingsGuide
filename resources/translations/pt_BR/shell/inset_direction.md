Paredes
====
Este parâmetro determina quais paredes são impressas primeiro, de fora para dentro ou de dentro para o exterior.

![A parede interna é impressa primeiro](../../../articles/images/outer_inset_first_disabled.gif)

![A parede externa é impressa primeiro](../../../articles/images/outer_inset_first_enabled.gif)

Este parâmetro tem um pequeno efeito na qualidade e na precisão dimensional:
* A impressão de fora para o interior melhora a precisão dimensional.As paredes adjacentes geralmente empurram um pouco, especialmente se a largura da linha de parede for menor que o tamanho do bico.A parede impressa primeiro será solidificada e, portanto, não será empurrada.Portanto, ao imprimir a parede externa primeiro, você obterá uma localização mais precisa da parede externa.
* Se o recheio for impresso antes das paredes, a impressão de fora para dentro para dentro reduzirá a quantidade de enchimento que se reflete na superfície.Caso contrário, o recheio é impresso primeiro, depois as paredes internas que são empurradas para o exterior pelo recheio e, finalmente, a parede externa que é empurrada para o exterior pelas paredes interiores.Portanto, um padrão pode ser visível lá fora.Se a parede externa for impressa primeiro, poderá solidificar antes que a parede interna possa empurrá -la.
* A impressão de dentro para fora é melhor para a criação de saliências.A parede externa está mais distante da camada anterior do que a parede interna.Quando a parede externa é impressa primeiro, ela ainda não tem nada para aguentar.Quando a parede interna é impressa primeiro, a parede externa pode ser fixada lateralmente na parede externa.

Quando houver um número ímpar de paredes, a parede central sempre será impressa por último.