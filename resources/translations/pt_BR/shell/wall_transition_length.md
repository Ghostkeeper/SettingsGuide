Comprimento de transição da parede
====
Em salas finas, nem todas as paredes entram na forma.Se a sala for mais fina em certos lugares do que outros, o Cura deve usar um número diferente de cabos em certos lugares.Este parâmetro controla a largura da área de transição onde um dos cordões é adicionado ou remove.

![Uma transição muito curta](../../../articles/images/wall_transition_length_0_2.png)

![Uma transição mais longa](../../../articles/images/wall_transition_length_1_5.png)

A zona de transição entre diferentes números de cabos sempre tem pequenos problemas.É o mais visível quando uma única linha nas extremidades centrais e os dois cabos circundantes devem preencher o vazio.Eles não preenchem imediatamente o espaço, e um vazio é deixado.Isso resulta em pequenos orifícios na parte superior e inferior das impressões.O oposto ocorre quando dois cordões se combinam em um, o que os faz andar por um tempo até que se encontrem.A superextrusão pode levar à imprecisão dimensional, especialmente quando ocorre na parede externa.Tudo isso pode ser evitado, tornando a transição o mais curta possível.

No entanto, uma transição curta também obriga o bico a fazer curvas muito apertadas para preencher rapidamente esse espaço.O resultado é um aumento nas vibrações, especialmente se isso acontecer para a impressão da parede externa.Se a transição for mais longa, as acelerações no bico serão reduzidas, em particular se forem inferiores ao limite de [sacada](../speed/jerk_print.md).

Corrigir esse comprimento a uma ou duas vezes a largura da linha é um ponto de partida razoável.As impressoras cujos quadros são mais leves ou mais pesados ​​podem precisar aumentá -lo, enquanto as impressoras que podem acelerar rapidamente sem vibrar podem se contentar para reduzir a transição para melhorar a qualidade visual.

** Este parâmetro não se aplica apenas às paredes normais, mas também a paredes de contorno adicionais, paredes de suporte, paredes de enchimento e padrões concêntricos. **