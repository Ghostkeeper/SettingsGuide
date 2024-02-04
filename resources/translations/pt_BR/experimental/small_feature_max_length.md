Comprimento máximo de pequena estrutura
====
Os pequenos detalhes da impressão geralmente são muito críticos à dimensional.Essa configuração significa que os pequenos orifícios na impressão são impressos mais lentamente, a fim de obter maior precisão.

Se um orifício tiver uma circunferência mais baixa do que a indicada por esse parâmetro, a velocidade na qual o perímetro deste furo é impresso será multiplicado por uma [pequena velocidade da estrutura](small_feature_speed_factor.md) (reduzido, normalmente).Este parâmetro é uma maneira diferente de abordar o parâmetro [tamanho máximo de pequenos orifícios](small_hole_max_size.md), que é mais genérico do que para orifícios circulares.

Um caso de uso comum desta função é a impressão de orifícios de parafuso com dimensões muito precisas.Ao imprimir pequenos orifícios, a bola tende a ser puxada com o bico na área.Se o canto for muito nítido, como é o caso de pequenos orifícios, ele tem o efeito de tornar o buraco menor.Quando a impressão é mais lenta, essa tração é reduzida porque o material tem mais tempo para se acalmar e porque a tração mecânica é simplesmente menor.

Ao aumentar esse ajuste, mais contornos são obtidos como "pequenos elementos".Uma parte maior dos orifícios de impressão será impressa mais lentamente.Portanto, esses orifícios serão impressos com mais precisão, mas o tempo de impressão será mais longo.