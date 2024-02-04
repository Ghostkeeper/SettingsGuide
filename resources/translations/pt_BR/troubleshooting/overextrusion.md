Superextrusão
====
O excesso -expansion é um termo usado quando a impressora extrada é muito material em um só lugar.O material então flui nas laterais ou para cima, o que torna a superfície muito áspera e irregular.Isso também pode causar [threads](string.md) e muitas [gotas (blobs)](blobs.md).

![Uma superextrusão maciça ocorreu nesta impressão](../../../articles/images/overextrusion.jpg)

Controle de temperatura
----
A causa mais frequente de excesso de exposição está imprimindo a temperatura muito alta.Se a [temperatura de impressão](../material/material_print_temperature.md) for ajustada muito alta, o material terá uma viscosidade mais baixa, o que fará com que ele saia do bico sem controle.Isso geralmente resulta em uma superextrusão em certas áreas, como paredes externas, mas um subestimes em outras pessoas, como o preenchimento.

Para remediar isso, você deve reduzir gradualmente sua temperatura.Examine cuidadosamente a folha técnica do material com o qual você imprime, qual é a faixa de temperatura aceitável e reduza sua temperatura de impressão para a parte inferior desta praia.

Diâmetro do filamento
----
Existem vários padrões para o diâmetro dos filamentos.Os mais comuns são 1,75 mm e 2,85 mm, mas 3,00 mm também são sempre possíveis.Além disso, nem todos os fabricantes produzem seu filamento com um diâmetro constante.Se o seu filamento for mais largo que o Cura espera, você extratará muita matéria, porque o Cura dá à impressora para extrudar um certo comprimento de filamento que terá muito volume.

Para remediar esse problema, primeiro meça o diâmetro real do filamento usando um slide.É preferível medi -lo em vários lugares, caso varie e a diferentes ângulos ao redor da circunferência.Fazer a média dessas medidas.Essa média pode ser informada em Cura na página de gerenciamento de materiais, como de propriedade do material.Se o diâmetro não puder ser alterado porque é um material integrado, você poderá primeiro duplicar o material.Isso deve então permitir que você edite o diâmetro.

Calibração da extrusora
----
Às vezes, o problema está no fato de que o material não corresponde às expectativas do microprograma.Se o motor da extrusora for um mecanismo de etapa -passo (que é comum nas impressoras 3D), o microprograma deve saber quantas etapas do motor levarão ao movimento de uma certa distância.O microprograma possui um parâmetro para isso, medindo a precisão da fonte de alimentação por milímetro.Se esse parâmetro estiver mal configurado, o carregador poderá se mover muito rapidamente ou muito lentamente.É melhor ajustar esse parâmetro no microprograma, se puder.No entanto, se isso for impossível, o [fluxo](../MATEMCIAL/MATEMCIAL_FLOW.MD) na cura pode ser ajustado para compensar.Você também deve compensar todas as [distâncias de retração](../Travel/Retaction_amount.md) e [Speeds](../Travel/Retaction_speed.md).

Sobreposição das paredes
----
Cura normalmente apenas desenha os contornos de impressão com uma certa largura de linha.Se as paredes estiverem mais próximas de certos lugares na impressão, isso causará sobreposição das linhas.Essas linhas ficam grossas e produzem manchas, porque pode haver até o dobro do material necessário.Quando há muita sobreposição, a segunda linha não pode ser extinta e a pressão dentro da sala do bico aumenta até que seja expulsa e produza uma bolha.

Isso pode ser evitado ativando [compensação por paredes sobrepostas](../shell/Travel_compense_overlapping_walls_nabled.md).A extrusão da segunda linha será reduzida para extrudar o máximo de material necessário para preencher o espaço restante da parede, o que impede a superextrusão.

Se as paredes se sobrepor devido à [inserção de parede externa](../shell/wall_0_inset.md), você pode tentar reduzir esse atraso para evitar a superextrusão.Você também pode tentar imprimir a [parede externa primeiro](../shell/outer_inset_first.md).O excesso de material será empurrado em direção ao interior do modelo, onde é invisível.

Ajuste do fluxo direto
----
Se você não souber o que causa essa superextrusão, também pode ajustar diretamente o [débito](../material/material_flow.md).Reduza a vazão até que sua superfície pareça suave novamente.Isso pode compensar diretamente um fator desconhecido.