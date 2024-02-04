Ative a aceleração do movimento
====
Se esse parâmetro for ativado, a viagem terá sua própria taxa de aceleração.O parâmetro [de aceleração em movimento](aceleração_travel.md) controla a taxa de aceleração durante a viagem.

O valor da aceleração durante o deslocamento levará o valor da linha que será impresso no destino do movimento.Por exemplo, quando se move para o preenchimento, a aceleração durante o movimento é [preencher a aceleração](access_infill.md).Quando vai em direção à parede externa, a aceleração será [aceleração da parede externa](aceleração_wall_0.md).Dessa maneira, ele realmente se aproximará de estruturas mais sensíveis com um pouco mais de precaução do que outras estruturas.

Este parâmetro é ativado por padrão, o que possibilita o controle da aceleração durante a viagem.É uma coisa boa na maioria das situações, porque o aumento da aceleração da viagem pode economizar tempo, enquanto uma aceleração tão alta causaria [ondas](../distúrbios/ringing.md) quando é usado para se imprimir.

No entanto, há duas razões pelas quais você pode desativá -lo:

* Para modificar a taxa de aceleração para viagens, a cura altera a aceleração em ambas as direções com muita frequência.Freqüentemente passa de extrusão ao movimento, em particular com certos padrões de enchimento e com os pequenos detalhes das paredes.O controlador deve processar esses pedidos e pode não ser capaz de seguir os cálculos necessários.Desativar esse problema está desativado esse problema.
* O aumento nas acelerações de movimento faz com que a impressora vibre muito.Essas vibrações ainda não foram completamente interrompidas no final da viagem quando a impressão precisa começar.Isso também pode levar a uma ondulação no final de uma viagem.Ao desativar a aceleração do deslocamento, o bico abordará estruturas de impressão sensíveis (como a parede externa) com mais precaução do que estruturas menos sensíveis (como enchimento).


