Pé de elefante
====
Às vezes, a parte inferior da impressão é um pouco mais larga que o restante da marca, que dá um pequeno lábio neste local.Isso é chamado de "pé de elefante" porque parece as pernas de um elefante cujos dedos dos pés são um pouco mais largos que o resto da pata.

Existem vários efeitos que as pessoas chamam de "pé de elefante", cujas causas inerentes são completamente diferentes.Esses efeitos também requerem soluções completamente diferentes.Este artigo ajudará você a encontrar a causa principal.

![Pés de elefante causados ​​pela força das camadas de pele](../../../articles/images/elephants_foot.jpg)

Fronteira
----
Às vezes, a pata do elefante é de fato apenas parte da fronteira que não foi removida corretamente.Se você arrancou a borda manualmente, poderá vê -la porque a linha da borda é completamente adjacente à linha normal da parede, e a linha normal da parede está diretamente sob o restante da parede.Para remover completamente a borda, é melhor usar uma faca afiada para surpreender o fundo da sua marca.

Se o modelo não tiver um lado inferior grande, considere definir o [tipo de adesão](../plataform_adhiction/adesion_type.md) em uma saia.Se isso representar muitos problemas de adesão à cama, você poderá tentar outros métodos para melhorar a adesão, por exemplo, ajustando o [método de adesão da camada inicial da parte inferior](../top_bottom/top_bottom_pattern_0. MD) em "Concêntrico ".

Deformação
----
A causa mais frequente da pata de um elefante é frequentemente deixada.Quando o material esfria, ele encolhe um pouco.O material das camadas inferiores às vezes não pode se retrair.Eles mantêm seu tamanho original, mas as camadas superiores se retraem um pouco.Várias razões podem explicar por que as camadas mais baixas não podem retrair:
* É colado à plataforma de impressão, que não encolhe.
* É aquecido pelo platô da Impressio, que impede que ele diminua.
* Há uma pele ao lado, que bloqueia o estreitamento.(Nas camadas superiores, pode haver preenchimento).

Para evitar a esquerda, dê uma olhada no [artigo de solução de problemas](Warping.md) sobre esse assunto.Para esse tipo de deformação, aqui estão alguns exemplos do que você pode tentar:
* Aumente a [espessura da parede](../Shell/Wall_thickness.md) para impedir as paredes ao lado do encolhimento.
* Reduza a [temperatura da bandeja de impressão](../material/material_bed_temperature.md) para permitir que a primeira camada se retire tanto quanto as outras camadas.Se a temperatura da cama era muito alta, também pode permitir que o material camba um pouco, o que a torna mais larga no fundo.Esse efeito é geralmente baixo, mas também será evitado reduzindo a temperatura do leito.
* Aumente a [espessura inferior](../top_bottom/bottom_thickness.md) para ir mais gradualmente para um tamanho menor.Você pode até considerar a impressão do modelo de maneira completamente sólida (de preferência, fixando a espessura do fundo para um nível extremamente alto) para eliminar completamente a diferença no estreitamento.

Ajuste da bandeja de impressão
----
A pata do elefante também pode ser causada pelo fato de a bandeja de impressão estar muito próxima do bico enquanto a primeira camada é impressa.Isso leva a uma superextrusão, que empurra a primeira camada para o exterior.

Para ajustar a bandeja de impressão, consulte o manual da sua impressora 3D.A maioria das impressoras está equipada com parafusos de ajuste para a bandeja de impressão ou no pórtico para ajustar a diferença na altura da bandeja de impressão durante a primeira camada.Ajuste a bandeja de impressão durante a impressão (de preferência durante a borda, saia ou jangada) até que a primeira camada seja muito suave e não mais fina que as outras.

Você também pode ajustar diretamente o [fluxo da primeira camada](../material/material_flow_layer_0.md) na cura para compensar qualquer superextrusão.Outra solução é reduzir a [largura da linha de camada inicial](../resolução/inicial_layer_line_width_factor.md) para normalizar a extrusão o suficiente para evitar a pata do elefante.

Deformação acima da transição vítrea
----
No caso de peças muito pequenas, é possível que a camada anterior ainda não tenha solidificado quando a próxima camada é impressa sobre ela.O material é expulso com força considerável pelo bico; portanto, se a camada anterior ainda não estiver solidificada, essa camada será esmagada e expandirá horizontalmente.Isso se manifesta na forma de uma perna de elefante.A solução é garantir que o material seja solidificado quando a próxima camada for empurrada sobre ela.Tente ajustar as seguintes configurações:

* Reduza a [camada inicial da temperatura de impressão](../material/material_print_temperature_layer_0.md), para que o material não precise esfriar tanto.
* Reduza a [temperatura da camada inicial](../material/material_bed_temperature_layer_0.md), de modo que a primeira camada esfria mais rapidamente, enviando mais calor para a parte superior da impressão.Os plásticos para a impressão 3D são projetados para solidificar muito rapidamente em um ponto de temperatura preciso, sua [temperatura da transição vítrea](https://en.wikipedia.org/wiki/glass_transition_transition_temperature_tg).Para evitar qualquer deformação, consulte a temperatura de transição vítrea do seu filamento em sua folha técnica e verifique se a temperatura da bandeja não excede muito essa temperatura de transição.
* Aumente a [velocidade inicial dos ventiladores](../resfriamento/cool_fan_speed_0.md), para esfriar o material mais rápido.Considere também aumentar o parâmetro [velocidade regular do ventilador na altura](../resfriamento/cool_fan_full_at_height.md), para continuar a esfriar as primeiras camadas.
* Reduza a [velocidade da camada inicial](../speed/speed_layer_0.md).Isso permite que você deixe mais tempo na primeira camada para esfriar após a impressão.
* Aumente a [duração mínima de uma camada](../resfriamento/cool_min_layer_time.md).O objetivo é garantir um certo tempo de resfriamento para cada camada antes que a próxima camada seja colocada na parte superior e usar a [velocidade máxima do ventilador](../resfriamento/cool_fan_speed_max.md).É de fato uma maneira mais simples de combinar ajustes na velocidade da camada inicial e a velocidade do ventilador listada acima.Lembre -se de que isso se aplica a toda a impressão, no entanto, e não apenas à primeira camada.

Soluções gerais
----
Aqui estão algumas soluções que você pode tentar se livrar de qualquer tipo de perna de elefante, seja qual for a causa:
* O uso de uma [jangada](../plataform_adhiction/adesion_type.md) torna possível mover toda a impressão da bandeja de impressão, o que evita os efeitos causados ​​pela bandeja de impressão, como sua temperatura e o fato de que ela permanece Muito para a plataforma de impressão e também evita ter que tirá -la.
* Reduza a [expansão horizontal da camada inicial](../shell/xy_offset_layer_0.md) (com um valor negativo).Isso torna possível compensar o pé do elefante na primeira camada.