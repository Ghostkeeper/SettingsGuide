Exterior antes das paredes interiores
====
Este parâmetro determina quais paredes são impressas primeiro, as paredes externas ou as paredes interiores.

![A parede interna é impressa primeiro](../../../articles/images/outer_inset_first_disabled.gif)

![A parede externa é impressa primeiro](../../../articles/images/outer_inset_first_enabled.gif)

A ativação deste parâmetro tem um efeito baixo na qualidade e na precisão dimensional:
* Isso melhorará a precisão dimensional.As paredes adjacentes geralmente se repelem um pouco, especialmente se a largura da linha de parede for menor que o tamanho do bico.A parede impressa primeiro será solidificada e não será empurrada tanto.Portanto, primeiro imprimindo a parede externa, você obterá uma localização mais precisa da sua parede externa.
* Se o recheio for impresso antes das paredes, isso reduzirá a quantidade de enchimento que se reflete na superfície.Caso contrário, o recheio é impresso primeiro, depois as paredes interiores que são empurradas para o exterior enchendo e, finalmente, a parede externa que é empurrada para o exterior pelas paredes interiores.Um padrão pode, portanto, ser visível lá fora.Se a parede externa for impressa primeiro, a parede externa poderá solidificar antes que a parede interna possa empurrá -la.
* A impressão da parede externa primeiro é geralmente pior para saliência.A parede externa está mais distante da camada anterior do que a parede interna.Quando a parede externa é impressa primeiro, ela ainda não possui uma saída na parede interna.Quando a parede interna é impressa primeiro, a parede externa pode se conectar lateralmente à parede externa.