Problemas de aderência de platô
====
Uma das falhas mais comuns para as impressões 3D é que a peça decola da placa quando ainda estava sendo impressa.Este artigo analisa certos ajustes que você pode fazer para impedir que isso aconteça.

Se a impressão decolar da bandeja, você geralmente verá muitos fios espalhados na bandeja.Se você é mais provável, ele também pode se manifestar por uma simples [mudança de camada](layer_shift.md) (e haverá menos para limpar).De qualquer forma, a impressão é estragada.

Métodos de aderência de platô
----
O Cura oferece vários métodos para melhorar a adesão no quadro.Você pode escolher entre esses métodos com o parâmetro [tipo de adesão da bandeja](../plataform_adhiction/adhelion_type.md).As seguintes opções estão disponíveis.
* A borda, a técnica mais comum, adiciona uma borda ao redor da parte inferior da impressão, o que aumenta a superfície da impressão para que ela adere melhor à bandeja de impressão.
* Uma jangada é uma placa localizada sob a impressão inteira.Esta placa também ocupa uma área maior, de modo que adere bem.Se a jangada for impressa com um material que adere bem à impressão (ou com o mesmo material), a impressão permanecerá dessa maneira.
* Uma saia não está presa à impressão, mas simplesmente a circunda.Essa linha garante que o material flua antes do início da impressão, para que não haja subestusão na primeira camada que possa arruinar a adesão.
* Você também pode não ter aderência selecionando "nenhum".Isso economiza tempo e matéria e evite os outros efeitos negativos dos métodos acima.Use apenas esta opção se a sua impressora tiver outra técnica de impressão, por exemplo, um pacote de sangramento.

A borda e a balsa são as técnicas mais eficazes para aumentar a adesão, porque são expressamente projetadas para esse fim.As impressões de tamanho mais razoável precisarão de qualquer uma dessas técnicas.

Se uma borda for usada, você poderá aumentar ainda mais a adesão aumentando a [largura da borda](../plataform_adhiction/Brim_width.md).Você também pode adicionar uma borda a [o interior dos suportes](../supports/support_bim_enable.md) e à [Torre iniciante](../dual/prime_tower_brim_enable.md), bem como entre o [modelo e o suporte ](../Platform_adhiction/BRIM_Replaces_support.md) e [buracos interiores](../plataform_adhiction/Brim_outside_only.md) do modelo.

Da mesma forma, se uma jangada for usada, você poderá aumentar a adesão aumentando a [largura da jangada](../plataform_adhiction/raft_margin.md).A jangada sempre será impressa abaixo de tudo, porque as camadas devem corresponder.Se a adesão entre o modelo e a jangada for problemática, lembre -se de reduzir a [lâmina aérea](../plataform_adhiction/raft_airgap.md) entre a jangada e o modelo.Além disso, você pode considerar aumentar a [largura da linha básica da jangada](../plataform_adhiction/raft_base_line_width.md).

Prevenção da esquerda
----
Se sua impressão sofre de deformação, a área de contato entre a impressão e a bandeja será fortemente reduzida.Para evitar isso, consulte o artigo sobre [Decolics](Warping.md).Em resumo, aqui estão alguns ajustes a serem feitos para evitar a esquerda.
* Ajuste a [camada inicial do motivo abaixo](../top_bottom/top_bottom_pattern_0.md) no concêntrico.
* Reduza a [temperatura do platô](../material/material_bed_temperature.md) e aumente a [temperatura do volume de construção](../material/build_volume_temperature.md).
* Ajuste o modelo para que haja menos cantos externos nítidos na primeira camada.

Ajuste da bandeja de impressão
----
Outra fonte frequente de problemas de adesão é que a placa de impressão não está nivelada.Cura assume que o bico toca a bandeja durante a viagem à coordenada Z 0, mas esse raramente é o caso.As bandejas de impressão se inclinam, são movidas para cima e para baixo e podem até dobrar.Se a bandeja de impressão não estiver em toda parte na coordenada 0, a cura extrudará mais material do que o espaço entre o bico e a bandeja, e você receberá um reforço ou uma subestusão.Quando a bandeja está muito próxima, a superextrusão pode levar à formação de bolhas, o que pode levar o bico para rasgar a impressão da bandeja de impressão durante uma viagem.Quando a bandeja está muito longe, a subestimação impede que o material seja empurrado na bandeja de impressão, o que o impede de grudar corretamente.Nos dois casos, a impressão não é confiável.

Algumas impressoras estão equipadas com sensores capazes de medir a posição da bandeja de impressão e compensar o firmware.Para essas impressoras, mova o bico para a coordenada Z 0 fará com que o bico toque o platô.No entanto, isso tem a desvantagem de distorcer o modelo.Para compensar uma bandeja de impressão inclinada, você terá um lado inferior inclinado, ou a impressão inteira pode ser curvada, girada ou deformada.

Se sua impressora não puder compensar uma bandeja que não está nivelada, também poderão ser feitas configurações do lado da cura:
* Aumente a [altura inicial da primeira camada](../Resolução/Layer_Height_0.md).Isso oferece um pouco mais de margem de erro.Isso também aumenta a força com que o material é empurrado para fora do bico e na bandeja de impressão.
* Reduza a [velocidade da camada inicial](../speed/speed_layer_0.md).Você evitará que um deslocamento não leve às linhas já impressas no conjunto de impressão.
* Da mesma forma, lembre -se de ajustar [a aceleração da camada inicial](../speed/aceleração_layer_0.md) e [sacadas da camada inicial](../speed/jerk_layer_0.md).Isso reduz as vibrações, o que pode causar subestimação e superextrusão periódica.
* Aumente o [número lento de camadas](../speed/speed_slowdown_layers.md).Isso reduz o risco de que movimentos rápidos não rasgam as camadas anteriores.

Vários ajustes
----
Esses parâmetros também podem ser ajustados se os métodos normais de associação de adesão não forem suficientes.
* Aumente a [altura da camada inicial](../Resolução/Layer_Height_0.md).Isso oferece um pouco mais de margem de erro, se a bandeja não estiver perfeitamente nivelada.Isso também aumenta a força com que o material é empurrado para fora do bico e no conjunto.
* Aumente a [largura da linha da camada inicial](../Resolução/Initial_Layer_line_width_factor.md).Da mesma forma, ele empurra o material com mais força, apertando -o bem no tabuleiro.
* O aumento da [camada inicial da temperatura da impressão](../material/material_print_temperature_layer_0.md) permite que o material flua mais na bandeja de impressão, o que aumenta a superfície de contato.
* Quanto ao aumento da temperatura, você também pode reduzir a [velocidade do ventilador da camada inicial](../resfriamento/cool_fan_speed_0.md) para manter o material do fluido por mais tempo.
* Da mesma forma, reduza a [velocidade da camada inicial](../speed/speed_print_layer_0.md).A redução na [velocidade de impressão da camada inicial](../speed/speed_print_layer_0.md) permite que o material flua novamente, porque o material é mantido fluido por mais tempo pelo bico quente.A redução da [velocidade de movimento da camada inicial](../speed/speed_travel_layer_0.md) reduz o risco de que um movimento de deslocamento rasgue as linhas impressas anteriormente da bandeja.Da mesma forma, considere ajustar os parâmetros [aceleração da camada inicial](../speed/aceleração_layer_0.md) e [Jerk da camada inicial](../speed/jerk_layer_0.md).
* Aumente [número de fraldas mais lentas](../speed/speed_slowdown_layers.md).Isso reduz os riscos de que movimentos rápidos não rasgam as camadas anteriores.

Bandeja de impressão
----
Além de uma boa impressão, uma boa bandeja de impressão também é importante para a aderência.Uma boa bandeja de impressão deve ser:
* ...ter !É muito importante que a bandeja não contenha gordura (como a dos dedos) e sem poeira.É muito eficaz limpá -lo sob uma torneira quente.O ideal é usar álcool isopropílico e um pano de microfibra.
* ...nível !Se a bandeja estiver muito próxima, o fluxo que sai do bico será irregular, o que causará inchaços que o bico rasgará durante seu próximo uso.Se a bandeja estiver muito longe, o material não estará bem colocado na bandeja, o que reduz consideravelmente a superfície.A maioria das impressoras possibilita ajustar a bandeja de impressão usando alguns parafusos de roda, portanto, você deve garantir que ela esteja perfeitamente nivelada e corretamente espaçada no bico.
* ... Rogeux!Com uma bandeja levemente áspera, a superfície de contato na bandeja e a impressão aumentam consideravelmente, diferentemente de uma bandeja perfeitamente lisa.Por esse motivo, algumas impressoras estão equipadas com vidro fosco ou metal anodizado.

O material da bandeja de impressão também tem um impacto significativo nas propriedades adesivas.Isso pode variar consideravelmente, dependendo dos materiais impressos.Os materiais mais comuns são vidro, acrílico, alumínio, aço ou alumínio anodizado.Cada um deles adere a diferentes materiais.As bandejas de impressão de plástico podem aderir quimicamente ao seu material.Outros materiais são caracterizados por uma superfície áspera que aumenta a superfície de contato.

Também existem métodos de adesão por camada adicional que você pode aplicar a qualquer bandeja de impressão:
* Os palitos de cola genéricos funcionam muito bem.Embora a cola seque rapidamente, ela produz uma superfície áspera com uma superfície aumentada para que a impressão adere.
* A fita adesiva tem um efeito semelhante, pois possui uma superfície áspera feita de papel, mas, diferentemente do papel, ela permanece perfeitamente plana no prato de impressão.Os tipos de fitas de mascaramento mais espessas, projetadas para uso externo, são as mais eficazes.
* A laca de cabelo funciona da mesma maneira que a cola, na medida em que deixa uma superfície áspera com um grão fino na bandeja.É muito fácil aplicá -lo uniformemente.
* Use a lixa na bandeja de impressão para torná -la mais áspera e aumentar a superfície de contato.Não o torne muito áspero; caso contrário, você terá uma superfície irregular para imprimir.Para fazer isso, use uma lixa de grão muito fina, como um grão de 500 ou mais.
* As "folhas de aderência" especializadas são vendidas por muitos vendedores de impressoras 3D, que podem ser esticadas no set.Eles funcionam da mesma maneira que a fita adesiva, mas são projetados para durar mais tempo.Alguns são feitos de um plástico que também adere quimicamente ao material impresso.