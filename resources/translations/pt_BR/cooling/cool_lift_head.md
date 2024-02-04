Olhando pra cima
====
Quando a [duração mínima de uma camada](cool_min_layer_time.md) é atingida, a cabeça de impressão diminui para evitar a impressão mais rápida que o tempo mínimo da camada.Dessa forma, a camada anterior tem tempo para esfriar e solidificar antes que a próxima camada seja colocada nela.A cabeça de impressão pode desacelerar até que a [velocidade mínima](cool_min_speed.md) seja atingida.

Se esse parâmetro for ativado e a cabeça de impressão deverá se mover mais lentamente do que a velocidade mínima para manter o tempo mínimo da camada, a cabeça de impressão se moverá ligeiramente para cima após a impressão da camada.Ela então esperará um pouco até que o tempo mínimo da camada seja alcançado, antes de começar com a próxima camada.

Se esse parâmetro estiver desativado, a cabeça de impressão será esperada no final da camada, o bico que afeta a impressão.

![Quando o tempo mínimo da camada é atingido, a cabeça pode subir](../images/cool_fan_speed.svg)

A cabeça de impressão sempre se move 3 mm para cima.Não há ajuste para configurar isso no momento.

Compromisso
----
Há um compromisso a ser feito quando você diminui o bico para permitir que a camada esfrie melhor.O tempo mínimo da camada visa dar o material por um tempo para esfriar, desacelerando o movimento da cabeça da impressão.Enquanto isso, os ventiladores sopram com seu poder máximo para esfriá -lo mais rapidamente, mas o bico quente também está sempre em plástico.Para peças muito pequenas, o bico quente pode transferir mais calor com a impressão de que o que os fãs podem evacuar.Ele derrete o plástico ainda mais do que se você não tivesse um tempo mínimo da camada.

Ao levantar a cabeça, esse problema é resolvido.Você sempre pode desacelerar até um certo ponto, mas para as camadas muito pequenas, o bico quente se afasta, para que não transfira mais calor na sala.A cabeça é mantida perto o suficiente para os fãs da cabeça continuarem soprando na impressão.

L'inconvénient de cette méthode est qu'elle effectue un [Hauteur du décalage en Z](../travel/retraction_hop.md), ce qui entraîne de la [Filasse](../troubleshooting/stringing.md). Bien que le fait de soulever la tête puisse améliorer l'affaissement et le ballonnement, cela provoquera un autre type de désordre. Un peu de post-traitement manuel à l'aide d'un couteau peut nettoyer la filasse qu'il provoque.
