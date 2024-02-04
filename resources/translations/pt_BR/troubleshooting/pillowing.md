Colchão
====
O efeito do colchão é um efeito em que pequenos protuberâncias ou orifícios aparecem entre as linhas de enchimento na parte superior do modelo.É mais frequentemente observado em superfícies superiores planas durante a impressão de alta velocidade.

![Bombas fortes e pequenos orifícios na superfície](../../../articles/images/pillowing.jpg)

Causas
----
O MateLassing é uma combinação de vários efeitos que se combinam para causar um efeito abaulador na face superior da impressão.

O bombardeio reconhecível da pele superior é na verdade uma forma de [de esquerda](Warping.md), onde a pele superior é comprimida pelas paredes circundantes e pelo recheio subjacente.À medida que as paredes e o recheio são impressos primeiro nas camadas inferiores, elas se refrescarão e se retraem enquanto a pele ainda está sendo impressa.Durante o estreitamento, as paredes e o recheio empurram as linhas da pele para dentro para o ponto em que estão abobadadas.

Outro fator importante no colchão é a flacidez das linhas de pele entre as linhas de enchimento.Dependendo da distância entre as linhas de enchimento, as linhas da pele devem cobrir uma certa distância.Se o resfriamento for insuficiente, o plástico cederá um pouco.As linhas da pele então aderem menos bem uma com a outra, deixando espaços entre eles.São necessárias algumas camadas de pele para reparar isso.

O efeito do colchão tende a inchar em vez de descer.Embora possa haver um abaulamento para cima e para baixo, o abaulamento é mais comum, porque o bico puxa na parte superior do plástico quando cruza a pele, o que exerce uma força de cisalhamento em direção ao topo por um curto período de tempo.Uma vez que as linhas são curvadas para cima, o efeito de deformação as mantém para cima.

Prevenção
----
Existem vários métodos para impedir o colchão em Cura:
* Aumentar a [espessura do topo](../top_bottom/top_thickness.md) é a maneira mais eficaz de impedir o colchão.Com mais [camadas superiores](../top_bottom/top_layers.md), as camadas superiores podem repousar nos espaços parcialmente fechados das camadas anteriores.Isso lhes dá uma chance melhor de fechar os espaços e formar uma camada superior sólida que não depende dessas rodadas.Em geral, quanto mais fina suas fraldas, mais você precisará até as camadas superiores, porque essas camadas não são tão sólidas.
* Aumente a [densidade do enchimento](../Infillon/Infill_Sparse_Dension.md) reduz o tamanho dos espaços que devem ser preenchidos pela pele superior.Portanto, é mais fácil preencher essas deficiências.Se você combinar isso com os [estágios progressivos de enchimento](../preenchimento/gradual_infill_steps.md), a maioria das densidades de preenchimento pode permanecer a mesma.Somente a parte superior terá uma densidade maior para evitar o efeito do colchão.
* Impressão a uma [temperatura de impressão padrão](../material/material_print_temperature.md) Melhora a punção e a esquerda em geral, também com a pele superior, o que reduz o efeito do colchão.
* Da mesma forma, deve -se tomar cuidado para aumentar a velocidade do [resfriamento](../resfriamento/cool_fan_speed.md) para melhorar a ponte.
* Redução da [velocidade de impressão acima/abaixo](../speed/speed_topbottom.md) melhorará diretamente a ponte.Isso também tornará possível empurrar melhor as camadas superiores da pele nas camadas inferiores.Também permite que você feche os buracos mais rapidamente.

