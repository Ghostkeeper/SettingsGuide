Topografia ou escada
====
O efeito "topografia" é obtido quando uma face inclinada superior ou inferior é impressa com uma pequena quantidade de camadas, de modo que os limites entre as camadas sejam suficientemente espaçados para que se tornem facilmente visíveis.Ele tem o nome de [cartões topográficos](https://en.wikipedia.org/wiki/topográfico), onde as diferenças de altitude são geralmente indicadas por curvas de nível.

![Você pode ver claramente as bordas das fraldas](../../../articles/images/topography.jpg)

Esse efeito é onipresente na impressão 3D e é uma das maneiras mais fáceis de reconhecer que um objeto foi impresso em 3D.É possível evitá -lo, mas o fato de impedi -lo geralmente reduz significativamente a produtividade.

Altura da camada
----
Como o efeito da topografia ocorre quando os limites entre as camadas estão muito distantes um do outro, é possível evitar esse efeito reduzindo a [altura da camada](../resolução/camada_height.md).Quando a altura da camada é reduzida, os menores incrementos verticais entre as camadas também resultam em etapas horizontais menores, o que reduz o efeito da topografia.A redução na altura da camada, no entanto, aumenta consideravelmente o tempo de impressão.

Em vez de reduzir a altura da camada para toda a impressão, você também pode reduzir a altura da camada apenas para as inclinações de impressão baixa usando [use camadas adaptativas](../experimental/adaptive_layer_height_abled. MD).Isso possibilita reduzir consideravelmente o efeito da topografia e ter um impacto mínimo no tempo de impressão.No entanto, é mais difícil ajustar a impressão para outras qualidades do que as mencionadas acima, pois o ajuste geralmente depende da altura da camada.

Ajuste da posição do modelo
----
Você também pode considerar posicionar o modelo para que não haja mais inclinação baixa na impressão.Mas isso geralmente envolve imprimir muito mais suporte para o seu modelo, o que também reduz a produtividade, e as saliências podem não ser tão bonitas.