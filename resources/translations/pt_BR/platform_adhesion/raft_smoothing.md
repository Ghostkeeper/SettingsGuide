Jangada
====
Esse ajuste possibilita tornar os ângulos internos da jangada mais suaves.A configuração especifica o raio de um arco.Todos os cantos interiores mais nítidos que o raio do ARC especificado serão suavizados para ter o raio de arco.

![Sem suavização](../../../articles/images/raft_smoothing_0mm.png)

![Raio de 5 mm](../../../articles/images/raft_smoothing_5mm.png)

O termo técnico para isso é uma [operação de fechamento morfológica](https://en.wikipedia.org/wiki/closing_ \ (morfologia \)).Todos os orifícios menores que o raio especificado serão fechados.Os ângulos internos mais agudos não serão mais claros.

A função dessa configuração é tornar a balsa mais rígida.Quando várias peças são conectadas por acessórios finos, a balsa pode se dobrar nesses locais.Isso os torna menos rígidos e menos resistentes à esquerda.Ao aumentar essa configuração, as peças separadas serão melhor conectadas, o que tornará a balsa mais sólida.A superfície da balsa será maior, para que a balsa grude melhor.Além disso, a jangada terá uma circunferência total menor, que reduzirá os locais onde o que a esquerda pode começar.No total, deve haver menos deformação.

No entanto, o volume total da jangada também será aumentado.Isso usa mais material e leva mais tempo para imprimir, especialmente porque a balsa é normalmente impressa muito lentamente.