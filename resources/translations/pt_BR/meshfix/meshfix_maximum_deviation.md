Desvio máximo
====
Embora a alta precisão possa parecer melhor no início, muitas vezes acontece que a impressora não gerencia muito bem o código-g obtido em alta precisão.É por isso que o Cura reduzirá a resolução durante o processo de corte.Este parâmetro determina até que ponto o caminho suavizado pode se desviar do caminho original para reduzir a precisão.

![Antes de reduzir a resolução](../../../articles/images/meshfix_maximum_resolution_0.05.png)

![Depois de reduzir a resolução (ao extremo)](../../../articles/images/meshfix_maximum_resolution_1.png)

A impressora deve processar o código-g enquanto for executado.Se o Code-G contiver muitos segmentos de pequenas linhas, a cabeça de impressão para manter uma alta velocidade deve processar tantos dados que o processador de impressora 3D não poderá seguir.Isso tem o efeito de que a cabeça de impressão diminui esporadicamente para permitir que a calculadora acompanhe o movimento ou simplesmente aguarde o próximo comando de movimento.A superfície então se torna muito áspera, ou mesmo tem pequenas gotas ou marcas, porque a saída fora do bico não corresponde perfeitamente ao movimento esporádico do bico.Às vezes, uma resolução mais baixa resulta em melhor qualidade de impressão.

Esse ajuste indica em que medida a nova trajetória suavizada pode se desviar da trajetória original de alta resolução.Consideramos que as linhas são unidas a outros segmentos de linha se forem mais curtos que a [resolução máxima](Meshfix_maximum_resolution.md), mas se esse atalho levar a um desvio do caminho maior que a distância indicada por este parâmetro, as linhas irão não estar anexado.

Observe que não é garantido que as mesmas alturas sejam removidas de cada camada se os cumes se alinharem.A redução na resolução é realizada em 2D, removendo os cumes das formas da camada, e não em 3D, removendo os cumes da malha.Consequentemente, uma redução excessiva na resolução geralmente leva a uma superfície irregular, em vez de uma superfície angular ajustada.

Por razões de integridade estrutural, é fortemente recomendável não deixar as trajetórias se desviarem de mais de uma metade da metade da linha.No entanto, se a superfície deve ser suave ou ter uma aparência bonita, essa configuração indica essencialmente a profundidade das irregularidades da superfície.O desvio máximo deve ser muito baixo para não ser visível a olho nu.

No entanto, uma redução excessiva na diferença máxima limita consideravelmente a redução na resolução.O Code-G resultante não pode ser impresso corretamente porque a unidade central não consegue processar controles de movimento curto.