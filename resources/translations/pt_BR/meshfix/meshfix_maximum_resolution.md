Resolução máxima
====
Embora a alta resolução possa parecer melhor no início, muitas vezes acontece que a impressora não gerencia muito bem o código G em alta resolução.É por isso que o Cura reduz a resolução básica durante o processo de corte.Este parâmetro determina a resolução de que o Cura manterá o máximo possível.

![Antes de reduzir a resolução](../../../articles/images/meshfix_maximum_resolution_0.05.png)

![Depois de reduzir a resolução (ad extremum)](../../../articles/images/meshfix_maximum_resolution_1.png)

A impressora deve tratar o código G enquanto for executado.Se o código G contiver muitos segmentos de pequenas linhas, a cabeça de impressão deverá fazer movimentos tão rapidamente que o processador de impressora 3D não poderá seguir.Isso tem o efeito de que a cabeça de impressão diminui esporadicamente para permitir que a unidade de pilotagem alcance o movimento ou simplesmente aguarde o próximo comando de movimento.A superfície se torna muito áspera, ou mesmo tem pequenas marcas, porque a saída fora do bico não corresponde perfeitamente ao movimento esporádico do bico.Às vezes, uma resolução mais baixa resulta em melhor qualidade de impressão.

Essa configuração indica um comprimento mínimo para segmentos de linha.Os segmentos de linha que são mais curtos que o comprimento especificado serão considerados como que podem ser anexados a outros segmentos de linha.Eles serão unidos se o novo caminho não se desviar de seu caminho original de mais do [Máximo Apart](Meshfix_Maximum_Deviional.md).

Observe que não é garantido que as mesmas alturas sejam removidas de cada camada se os cumes se alinharem.A redução na resolução é realizada em 2D, removendo os cumes das formas da camada, e não em 3D, removendo os cumes da malha.Consequentemente, uma redução excessiva na resolução geralmente leva a uma superfície irregular, em vez de uma superfície angular ajustada.

Recomenda -se reduzir a resolução do modelo para que a cabeça de impressão não diminua significativamente para dar tempo à CPU para recuperar o atraso.Se a resolução não for suficientemente reduzida, a superfície se tornará áspera porque a cabeça de impressão reduzirá sua velocidade enquanto a extrusão continuar.Se a resolução for muito pequena, a superfície também será feita pelo fato de as paredes não se alinharem exatamente em todos os lugares.

