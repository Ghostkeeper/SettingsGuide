Ondulações
====
As ondulações (às vezes chamadas de "fantasma") são um efeito em que as ondulações também aparecem em superfícies planas, perto de pequenos detalhes dessa superfície.As ondulações estão começando a ocorrer logo após a impressão dos pequenos detalhes.

![Ondulações na superfície](../../../articles/images/ringing.jpg)

Causas
----
As ondulações são causadas pelas vibrações da sua impressora 3D.Tentar evitar ondulações é reduzir essas vibrações.Eles são particularmente pronunciados se a cabeça de impressão se mover para uma das frequências de ressonância do quadro da sua impressora.

Essa é uma das coisas que impressoras 3D mais caras geralmente tentam evitar com uma estrutura mais rígida que vibra menos.Eles têm um pórtico mais forte com barras tocadas e hastes de aço ou fornecem uma estrutura totalmente fechada feita de material muito rígido.Mas, como é caro, os modelos de impressoras 3D baratos não podem pagar as vibrações.As impressoras equipadas com um tubo Bowden não apresentam tantas ondulações, porque a cabeça de impressão é muito mais leve que a de uma cabeça de impressão direta de acionamento (já que o motor de energia pesada é baseado na cabeça de impressão).

Embora as ondulações se manifestem horizontalmente, as vibrações nem sempre são horizontais.A vibração da bandeja de impressão de cima para baixo em comparação com o bico também é um efeito muito importante, porque a gota de plástico é esmagada e se torna mais larga quando a bandeja de impressão vibra mais próxima ou mais fina quando vibra ainda mais.

Soluções de materiais
----
Antes de ajustar suas configurações no Cura, é bom ver primeiro se você pode melhorar seu equipamento para evitar ondulações.Isso pode possibilitar melhorar os resultados gerais da impressão sem precisar sacrificar outras qualidades de impressão, como resistência ou produtividade.Aqui estão alguns elementos a serem levados em consideração:
* Adicione os amortecedores sob sua impressora.Você pode usar pés de borracha ou simplesmente colocar a impressora em um bloco de espuma macia.Isso impedirá as vibrações se a tabela vibrar e também impedirá que a impressora vibre a tabela.Isso reduzirá o retorno das informações que a impressora vibrante recebe da tabela, o que contribui para reduzir vibrações de alta frequência.
* Aperte as tiras de treinamento do pórtico.Se esses cintos não estiverem tensos, a elasticidade de sua borracha permite que a cabeça da impressão vibre.
* Se a sua cabeça de impressão estiver equipada com fixadores flexíveis, como um tubo Bowden, lembre -se de corrigi -los para que eles não possam mais oscilar.Os prendedores funcionam bem para os tubos de Bowden, se você puder anexá -los a alguma coisa.
* Adicione mais massa ao quadro da sua impressora 3D.Portanto, será mais difícil mover o quadro devido ao seu aumento de inércia, e, portanto, será mais difícil torná -lo vibrar.
* Aumente a rigidez da estrutura da sua impressora 3D com reforços adicionais ou barras transversais.Você pode fabricá -los com materiais duradouros, como aço, mas se não for possível, poderá encontrar em uma loja de ferragens que se adapte com um mínimo de ajustes.Você também pode considerar imprimir esses reforços e peças cruzadas em 3D, mas saiba que a maioria dos plásticos não apóia a aplicação de uma força sustentada.

Soluções Cura
----
Se as soluções do material não forem possíveis, você também poderá reduzir o efeito da ondulação, graças a certos ajustes dos parâmetros da cura.

Como as vibrações são causadas pela aceleração da cabeça de impressão, as melhorias mais importantes visam reduzir essas acelerações.
* Redução da [velocidade de impressão](../speed/speed_print.md) reduz o máximo da duração da aceleração.
* A redução na [velocidade de aceleração](../velocidade/aceleração_print.md) reduz diretamente a aceleração e diminui a força das vibrações.
* Na impressão 3D, [The Jerk ou Jerk](../Speed/jerk_print.md) é um termo industrial que designa mudanças de velocidade instantânea durante os cantos.Isso significa que é essencialmente tentar acelerar infinitamente para evitar ter que diminuir muito a cada turno.Isso causa aceleração muito alta por curtos períodos em cada turno.A redução do choque também pode ajudar a reduzir as vibrações.Em vez de uma aceleração breve e forte, acelera mais lenta e mais, o que reduz vibrações de alta frequência, mas aumenta as vibrações de baixa frequência.

Esses ajustes farão sua impressão levar mais tempo.Mas você também pode evitar ondas de outras maneiras, impedindo o tipo de movimentos que lhes causam:
* Desative a técnica de [preencher os espaços](../shell/FILL_PERIMETER_GAPS.MD) e N '[Imprima paredes finas](../Shell/Fill_Outline_GAPS.MD), porque essas técnicas às vezes usam linhas de segmentos muito pequenos e adicionais viagens.Se uma parede for impressa posteriormente, a impressora vibrará um pouco.
* Se a sua impressora mover a bandeja de impressão de cima para baixo, em vez da cabeça de impressão, não use [com z](../Travel/Retaction_hop_abled.md).Ele vibra a bandeja de impressão de cima para baixo, muito tempo depois que o salto foi feito.

Você também pode imprimir [paredes interiores antes da parede externa](../shell/outer_inset_first.md).Como a impressão das paredes geralmente não causa tantas vibrações quanto as outras partes, isso permite que a impressora pare de vibrar diante da parede externa, tão importante, é impressa.

Finalmente, de acordo com a geometria do seu pórtico, as vibrações às vezes são absorvidas de maneira diferente em direções diferentes.Uma rotação de 45 graus do seu quarto também pode ajudá -lo.