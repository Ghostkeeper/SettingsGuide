Velocidade da camada inicial de pequena estrutura
====
Os contornos mais curtos que o [comprimento máximo dos pequenos elementos](small_feature_max_length.md) podem ser impressos a uma velocidade reduzida.Este parâmetro permite que você indique a velocidade na qual esses contornos devem ser impressos na primeira camada, como um fator em sua [velocidade normal de impressão](../speed/speed_wall.md).Essa velocidade pode ser configurada separadamente da velocidade de impressão dos pequenos elementos no [restante das camadas](small_feature_speed_factor.md).

Pequenos contornos não têm muita superfície para grudar no conjunto de impressão.Em particular quando [imprimindo as paredes antes de encher](../preenchimento/refill_before_walls.md), as paredes para pequenos orifícios geralmente são apenas pequenos círculos colocados na bandeja de impressão.Se o bico os exceder durante um deslocamento subsequente, eles poderão ser arrancados da bandeja de impressão.Por esse motivo, a velocidade de impressão desses pequenos contornos pode ser reduzida em comparação com outros contornos.Isso permite que o material flua cada vez melhor com a bandeja de impressão, o que reduz as chances de arrancá -las da bandeja de impressão.

A redução na velocidade de impressão desses pequenos contornos tem um impacto negativo muito menor na velocidade de impressão.Felizmente, como esses contornos são pequenos por definição e isso diz respeito apenas à primeira camada, o tempo total de impressão adicionado não é significativo.