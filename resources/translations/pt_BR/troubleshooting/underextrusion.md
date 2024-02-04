Subestamento
====
Um dos problemas de impressão 3D mais comuns é que a impressora não extrai material suficiente para produzir um belo objeto sólido.Quando isso acontece, falamos de "subestruição": o bico de extrude menos material do que o esperado.

![Um caso extremo de subestusão, onde se pode até ver o interior do objeto](../../../articles/images/underextrusion.jpg)

A parte inferior também pode se manifestar de várias maneiras.No caso mais extremo, o objeto é muito frágil e suas partes interiores são visíveis através da superfície.Às vezes, vemos isso por causa da largura muito baixa das linhas, para que elas não se conectem às linhas adjacentes.Às vezes, ele se manifesta apenas por pequenos orifícios na superfície superior ou pequenas fraturas nas paredes.

Há uma infinidade de possíveis causas de subestusão, o que dificulta a solução de problemas.O restante deste artigo descreve algumas das causas mais prováveis ​​e como remedi -lo.

Corporativo
----
Se a sua impressora impressa anteriormente muito bem e de repente apresenta uma subestimação sem modificação significativa do objeto ou parâmetros impressos, é provável que o problema esteja em algum lugar do trem da extrusora.Em geral, o link mais fraco é o bico.

Os bicos bloqueados são um fenômeno comum com qualquer impressora 3D.Isso pode acontecer quando o filamento é contaminado por elementos que não derretem bem e são empurrados para o bico.Isso também pode acontecer quando o filamento em si é queimado no bico.Isso pode acontecer quando o plástico é aquecido muito forte ou mantido em alta temperatura por muito tempo.O material degrada, os polímeros cristalizam e você acaba com um pedaço de plástico rígido que não derrete no bico.Para remediar isso, você deve remover os detritos do bico.

Existem várias técnicas para extrair detritos do bico.Se você tiver uma agulha de acupuntura ou outro eixo de metal fino, poderá empurrá -la de baixo.No entanto, a técnica mais comum é conhecida como "atração atômica".Para executar essa técnica, pegue um pedaço de filamento com pelo menos 50 cm de comprimento, de preferência em um material de ponto de fusão alto.Aqueça o bico no ponto de fusão deste filamento (por exemplo, 190 ° C para o PLA) e depois empurre o filamento para dentro com um alicate até que um certo tipo de material do bico.Em seguida, deixe o bico esfriar com sua temperatura de transição vítrea (por exemplo, 60 ° C para PLA), enquanto empurra o filamento para baixo no bico.Pouco antes da atingida a temperatura da transição vítrea, puxe o filamento rapidamente para tirá -lo.Se o final do filamento estiver sujo com plástico enegrecido, corte a extremidade e tente novamente até que esteja limpo.Tente imprimir algo novamente e, com um pouco de sorte, ele está melhorando agora.

Mudança de extrusora
----
Às vezes, a extrusora não tem o suficiente para levar o filamento para empurrá -lo forte o suficiente para baixo através do bico.Durante a impressão, podemos ouvir o filamento deslizar periodicamente, com um leve estalo a cada poucos segundos.É o dispositivo de energia que tenta empurrar o filamento para dentro, mas o filamento desliza novamente de tempos em tempos.

A maioria das fontes de alimentação possui pontos de ajuste para ajustar a força que se exercitam no filamento.Tente ajustar o distribuidor um pouco mais apertado no filamento.Se a indústria de alimentos crescer demais no filamento, ela pode quebrá -lo ou causar muito atrito e começar a cortá -lo.Se estiver muito solto, muitas vezes você verá um subestimado.

Diâmetro do filamento não uniforme
----
Se a maioria dos filamentos estiver bem, às vezes acontece que muito é produzido enquanto o filamento é um pouco bom demais.Isso pode ter grandes consequências na quantidade de extrusão na sua impressão.Os filamentos mais baratos têm maior probabilidade de apresentar esse problema.Você pode usar um slide para medir o diâmetro real do seu filamento.Certifique -se de medir em vários lugares diferentes longitudinalmente e não meça onde o sistema de energia cruzou o filamento.

Se o diâmetro do filamento estiver muito distante (uma diferença de 50μm começar a ser visível na impressão), você poderá ajustar o diâmetro do seu filamento no gerente de material.Se você usar um material de cura padrão, precisará duplicar este material antes de modificá -lo.Cura então compensará o novo diâmetro ajustando a velocidade do sistema de energia.

Fusão de material
----
Além do fato de que sua impressora 3D está em perfeitas condições, as configurações que você usa para imprimir também devem corresponder às propriedades do material que você usa.O mais importante é a temperatura de impressão.

Se a [temperatura de impressão](../material/MATTER_PRINT_TEMPERATURA.MD) estiver muito baixa, você verá rapidamente um subestimado.Se o material estiver muito frio, será muito viscoso, o que tornará mais difícil sair do bico corretamente.Combinado com uma alta velocidade de impressão, o material não tem tempo para derreter corretamente e não tem tempo para fluir em posição.Alguns materiais, como PVA ou nylon, tendem a absorver a umidade do ar.Essa umidade evapora quando o material é impresso, o que esfria o plástico.Para compensar o efeito da umidade do ar, é necessário usar materiais de reposição.

Circular
----
Sempre há um certo tempo de latência entre o momento em que a impressora avança o material e o que ele realmente começa a extrudar.Essa latência pode levar a uma subestimação se não for levada em consideração.Quando a impressora empurra o material para a frente, a pressão na sala do bico aumenta gradualmente até que seja suficiente para empurrar o material derretido para a outra extremidade.Pode fluir até um segundo antes que o material atinja seu fluxo normal.Se a impressora estiver equipada com um tubo de Bowden entre o carregador e o bico, esse período poderá até ser muito mais importante, em um intervalo de aproximadamente 10 segundos.

Quando a impressora deve começar a extrudar mais material do que antes, ela alimenta o material mais rapidamente, mas levará um tempo até chegar ao final do bico.Enquanto isso, o bico tentará rastrear uma linha, mas essa linha será desfilada.Especialmente quando a impressão é muito detalhada, isso pode causar uma considerável subestusão.

Existem duas configurações que você pode fazer para remediar isso: Primar e ajuste de velocidade.

A impressão consiste em empurrar um pouco de material antes que a parte importante da impressão comece.Muitas vezes, isso é feito no início de uma impressão em uma rotina separada, imprimindo uma pequena linha ou uma gota de plástico em um canto da bandeja de impressão.Você também pode usar uma [saia ou borda](../plataform_adhiction/adesion_type.md), que imprimirá um certo número de linhas ao redor da própria impressão.Quando o material flui corretamente e todo o ar saía da sala dos bicos, será mais uniforme.

Quando o material é retraído, o fluxo do material é interrompido.Quando o material é empurrado de volta para o bico, ele pode fluir um certo tempo antes de retomar seu fluxo.A redução na [velocidade em que é empurrada](../Travel/Retaction_prime_speed.md) permite que o material derreta melhor antes de ser extrudado, o que ajuda um pouco.Caso contrário, você também pode tentar empurrar o material um pouco mais do que antes da retração [iniciando um pouco mais](../Travel/Retaction_ Extra_prime_amount.md) para compensar a subestruição.A configuração é, no entanto, muito delicada.

Equilíbrio
----
Se você vir uma subestimação apenas em determinadas estruturas de impressão, como preenchimento e suporte, procure equalizar mais o fluxo na sua impressão.Sempre há um atraso entre o momento em que o marusime alimenta o material e que quando esse material realmente sai do bico.Se a velocidade de impressão for aumentada durante parte da impressão, a cabeça de impressão acelera relativamente rapidamente, mas o fluxo de material permanece atrasado até que a pressão na sala dos bicos seja aumentada para enfrentar a maior velocidade de extrusão.Isso também leva a uma subestimação.Da mesma forma, ao desacelerar a velocidade de extrusão, sempre há uma superextrusão.

Alguns microprogramas são capazes de compensar esse efeito.Marlin tem uma função chamada [Linear Advance](http://marlinfw.org/docs/features/lin_advance.html) que está começando a aumentar a pressão dentro da sala de bicos com antecedência para que possa sair do bico anteriormente.Sailfish tem uma [função semelhante](https://www.sailfishfirmware.com/doc/tuning-jkn-advance.html), que ele chama de JKN Advance.Para ajustar os parâmetros dessas funções, consulte qual código G você deve escrever no código G de partida.

Se essas funções estiverem indisponíveis ou ineficazes, você precisará garantir que não haja alterações repentinas e importantes no fluxo na impressão.[Reduza a espessura da camada de enchimento](../preenchimento/refill_sparse_thickness.md) e [a espessura da camada de suporte](../support/support_infill_sparse_thickness.md).Esses parâmetros multiplicam a taxa de extrusão para obter uma altura de camada maior.

Mais importante, você deve garantir que o preenchimento, as paredes interiores, a parede externa, a pele e o suporte sejam impressos com uma taxa de extrusão semelhante.A taxa de extrusão de uma linha é o produto de sua largura, a altura da camada, fluxo e velocidade (média).Multiplique esses quatro valores juntos e verifique se o resultado é aproximadamente o mesmo para encher ([altura da camada](../prelocill_sparse_thickness.md), [largura da linha](../Resolução/Infill_line_width .md), [Fluxo de preenchimento](../material/infill_material_flow.md) e [velocidade de preenchimento](../speed/speed_infill.md)), pele ([largura da linha](../resolução/skin_line_width.md), [fluxo de acima/abaixo](../material/skin_material_flow.md) e [speed](../speed/speedtopbottom.md)), parede externa ([largura da linha](../resolução/wall_line_width_0.md), [ Fluxo de parede externo](../material/parede_0_material_flow.md) e [speed](../speed/speed_wall_0.md)), parede interna ([[largura da linha da) parede interna (s)](../resolução/Wall_line_width_x.md), [fluxo](../material/wall_x_material_flow.md) e [speed](../speed/speed_wall_x.md)) e suporte ([altura da camada](../support/support_infill_sparse_thickness .md), [largura da linha](../resolução/support_line_width.md), [fluxo](../material/support_material_flow.md) e [speed](../speed/speed_support.md)).Se [compensação por sobreposição das paredes](../shell/Travel_complensate_overlapping_walls_enabled.md), certifique -se de ativar [equalize o fluxo dos filamentos
](../speed/speed_equalize_flow_enabled.md) para que a velocidade seja ajustada em vez do fluxo.

Limites do bico
----
A extrusão de muito material através de um pequeno bico também pode causar uma subestimação.Durante a impressão em alta altura da camada, largura de linha ou velocidade usando um pequeno bico, o material não poderá fluir fisicamente para fora do bico no tempo.O aumento da temperatura pode ajudar a tornar o material mais fluido até um certo ponto, mas sempre há limites que um bico pode extrudar.Além desse limite, você deve considerar comprar um bico maior.

Por outro lado, a extrusão de material muito baixo também pode levar a uma subestimação.Se a pressão na sala do bico estiver muito baixa, a tensão superficial do plástico líquido poderá manter o material na sala do bico.Às vezes, será empurrado para fora por uma gota grande, deixando o ar em outros lugares.Isso pode dar um efeito semelhante ao subestrião.

Ajustar o fluxo diretamente
----
Se tudo o mais falhar, o Cura também possui um ajuste, permitindo ajustar o fluxo diretamente: [débito](../material/material_flow.md).Esse método de ajuste pode compensar um defeito desconhecido em algum lugar do sistema.

Não funcionará se impedirmos fisicamente que o material flua mais rápido (por exemplo, devido a um bico bloqueado).Em outros casos, provavelmente causará uma superextrusão em certos lugares.No entanto, é uma maneira simples de ajustar a impressão de acordo com as necessidades.