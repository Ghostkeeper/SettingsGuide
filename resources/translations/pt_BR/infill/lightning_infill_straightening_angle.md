Eclair preenchendo raiva
====
Este parâmetro determina a inclinação do padrão que pode ser tomado no preenchimento lateral da luz.

O enchimento do Eclair produz linhas em zigue -zague que lembram um raio, onde deve suportar a parte superior da impressão, mas essas linhas levam muito tempo para imprimir por causa de seus ângulos nítidos.Nas partes inferiores, o software tentará endireitar essas linhas de dente de serra, para reduzir o tempo de impressão.Essa recuperação leva a restos mortais.O parâmetro determina a quantidade de corpo lateral autorizado.

![A 40 °, as linhas de enchimento convergem rapidamente em linhas retas](../../../articles/images/lightning_infill_straightening_angle_40.png)

![A 10 °, não há mais saliências íngremes no preenchimento](../../../articles/images/lightning_infill_straightening_angle_10.png)

Recuperar -se rapidamente (aumento de restos) reduz um pouco o tempo de impressão, mas também reduz a confiabilidade da impressão, especialmente para linhas de baixa largura.Se o corpo for muito grande, o resultado é uma divisão da camada.A separação está dentro da impressão e geralmente não representa um problema, mas pode levar a uma falha completa de uma parte do recheio, o que significa que uma parte do lado superior não é sustentada.Isso será visível na forma de uma mancha ou subsidência no topo, ou mesmo uma pilha de plástico na pior das hipóteses.