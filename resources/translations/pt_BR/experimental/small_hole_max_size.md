Tamanho máximo de pequenos orifícios
====
Os pequenos detalhes da impressão geralmente são muito críticos à dimensional.Essa configuração significa que os pequenos orifícios na impressão são impressos mais lentamente, a fim de obter maior precisão.

Se um orifício circular tiver um diâmetro menor que o valor desse parâmetro, a velocidade na qual o perímetro deste furo é impresso será multiplicado por um fator da [pequena velocidade da estrutura](small_feature_speed_factor.md) (reduzido, normalmente).Para orifícios que não são circulares, eles serão impressos em uma velocidade diferente se a circunferência for menor que um círculo com o diâmetro especificado aqui.Veja também [comprimento máximo da estrutura pequena](small_feature_max_length.md);É a configuração que realmente será usada para cortar.

Um caso de uso comum desta função é a impressão de orifícios de parafuso com dimensões muito precisas.Ao imprimir pequenos orifícios, o cordão tende a ser disparado com o bico na área.Se o canto for muito nítido, como é o caso de pequenos orifícios, ele tem o efeito de tornar o buraco menor.Quando a impressão é mais lenta, essa tração é reduzida porque o material tem mais tempo para se acalmar e porque a tração mecânica é simplesmente menor.

Ao aumentar esse ajuste, mais contornos são obtidos como "pequenos elementos".Uma parte maior dos orifícios de impressão será impressa mais lentamente.Portanto, esses orifícios serão impressos com mais precisão, mas o tempo de impressão será mais longo.