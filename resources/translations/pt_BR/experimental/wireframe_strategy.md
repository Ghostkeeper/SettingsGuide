Estratégia de impressão com fio
====
A preocupação mais importante para a confiabilidade de imprimir o fio diz respeito aos pontos de conexão em que as camadas do quadro se conectam.Existem várias estratégias para tornar essas conexões mais sólidas.Este parâmetro permite que você escolha a estratégia que a impressora usará.

Compensar por
----
Usando essa estratégia, o software tentará compensar os fatores de subsidência do material.À medida que o material sai do bico, ele cairá um pouco antes de solidificar e será acionado pelos movimentos do bico.Essa estratégia distorce o padrão de dente de serra que conecta as camadas do quadro para que termine, esperamos, por estar no lugar certo.

Dois fatores de compensação estão disponíveis: um deforma o jato da queda apenas verticalmente para [compensar a flacidez](Wireframe_fall_down.md), e o outro se deforma o jato do dente de serra em uma direção diagonal para [compensar o material treinado](Wireframe_drag_along.md) com o bico.

Nó
----
Quando essa estratégia for escolhida, um pequeno movimento para cima e para trás será feito no topo de cada serra para formar um "nó" da matéria.O objetivo deste nó é dar ao anel horizontal que o supera uma certa superfície para prender ao motivo do dente de serra.O nó varia um pouco de um lado para o outro, de modo que, se o anel horizontal não for colocado com precisão, haja ainda mais assim que eles estão presos um ao outro.Além disso, o nó garantirá que a linha ascendente se estenda um pouco mais para cima, o que fará com que o anel horizontal seja empurrado sobre ele.Finalmente, o nó também produzirá uma certa vazamento devido à falta de retração nesse movimento de movimento.Isso produz uma mancha na qual o anel horizontal pode ser melhor.

![Onde o nó é dado e qual é o seu tamanho](../../../articles/images/wireframe_top_jump.svg)

O movimento para este "nó" é uma série de movimentos de viagem:
1. Primeiro de tudo, o bico se move ligeiramente para cima e para trás.
2. Se houver um [atraso](Wireframe_top_delay.md) na parte superior, o bico para durante o atraso.Essa quebra é feita na ponta do movimento do nó.
3. 3. Terceiro, o bico desce para a altura usual.Ao mesmo tempo, o bico avança e se afasta da linha vertical.

Retração
----
Quando essa estratégia for escolhida, o material será retraído após cada movimento durante a impressão do jato de serra.A idéia é que, ao retrair o material, o fio está quebrado.Isso reduz o efeito de rascunho do material durante o movimento do bico, porque o encadeamento anterior não está mais conectado ao bico.Então o bico faz um pequeno salto de milímetro e continua seu movimento diagonal em direção à camada inferior.

Uma grande desvantagem dessa estratégia é que a linha diagonal descendente não está mais presa ao bico.Isso realmente torna a extrusão inútil durante essa linha.O material simplesmente acaba formando uma mancha na camada inferior.O material também é submetido a uma maior moagem porque é retraída da frente para trás sem que haja muita extrusão entre os dois.Tudo também leva muito tempo.