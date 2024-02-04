Ative empurrões de viagem
====
Se esse parâmetro for ativado, os movimentos de movimento terão sua própria taxa de empurrão.O parâmetro [Jerk em movimento](jerk_travel.md) controla a velocidade na qual a viagem pode se revezar.

O valor do jerk durante o deslocamento levará o valor da linha que será impresso no destino do deslocamento.Por exemplo, quando se move em direção ao enchimento, o idiota durante o movimento é [preenchendo o idiota](jerk_infill.md).Quando se mover para a parede externa, o idiota será o [empurrão da parede externo](jerk_wall_0.md).Dessa maneira, ele realmente se aproximará de estruturas mais sensíveis com um pouco mais de precaução do que outras estruturas.

Este parâmetro é ativado por padrão, o que permite controlar o idiota durante a viagem.É uma coisa boa na maioria das situações, porque um aumento na velocidade do movimento pode economizar tempo, enquanto essas velocidades altas de turno causariam [ondas](../Solução de problemas/ringing.md) quando usado para impressão.

No entanto, há duas razões pelas quais você pode desativá -lo:

* Para modificar a taxa de aceleração da viagem, o Cura muitas vezes modifica a taxa de empurrão em ambas as direções.Freqüentemente passa de extrusão ao movimento, em particular com certos padrões de enchimento e com os pequenos detalhes das paredes.O controlador deve processar esses pedidos e pode não ser capaz de seguir os cálculos necessários.Desativando esse problema é desativado.
* O aumento dos solavancos de viagem faz com que a impressora vibre muito.Essas vibrações ainda não foram completamente interrompidas no final da viagem quando a impressão precisa começar.Isso também pode levar a uma ondulação no final de uma viagem.Se você desativar a função "Jerk em movimento", o bico abordará estruturas de impressão sensíveis (como a parede externa) com mais precaução do que estruturas menos sensíveis (como enchimento).


