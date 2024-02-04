Tamanho mínimo de entidades
====
Este parâmetro controla a largura mínima dos detalhes do modelo que será impresso.Tudo o que é mais fino do que não será impresso.

Detalhes menores que o tamanho do bico provavelmente não serão impressos corretamente.Esta é uma limitação da impressora.No entanto, o Cura sempre pode tentar imprimi -los, concordando em não ter uma boa velocidade de extrusão, ou que os detalhes acabam sendo mais grossos do que o modelado.

Reduzir o tamanho mínimo do item permite que a impressora imprima detalhes menores da impressão.Dependendo da [largura mínima da linha de parede fina](min_bead_width.md), esses pequenos detalhes podem ser impressos extrudando muito pouco (o que causa [subestrião](../solucionando problemas/subenextrusion.md), ou extrudindo mais larguras de linha razoáveis, mas imprimindo -as grandes.Ao colocar esse valor em 0, a impressora vai para o final de cada ângulo brilhante.

Ao aumentar o tamanho mínimo das entidades, a impressora não se preocupa com pequenos detalhes que, de qualquer forma, não seriam bem devolvidos.Isso economiza um pouco de tempo e torna a impressão mais limpa.