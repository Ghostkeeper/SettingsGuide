Conecte os polígonos superiores/inferiores
====
Quando você usa um padrão concêntrico alto/baixo (um padrão composto por contornos fechados, também chamados de polígonos), conecta todos os contornos entre eles para que eles formem um único caminho.

![Modelo ingênuo concêntrico](../../../articles/images/connect_skin_polygons_original.png)

![Todos os contornos estão conectados para formar uma curva](../../../articles/images/connect_skin_polygons_enabled.png)

Isso impede a maioria dos movimentos.No entanto, isso cria novos ângulos animados, onde o bico terá que acelerar e desacelerar muito, o que compensará o ganho no tempo de impressão.O padrão ondulado também será visível lá fora, o que proporciona um efeito visual interessante.

Os contornos criados por [número adicional de paredes externas](Skin_Outline_Count.MD) não estão conectados.