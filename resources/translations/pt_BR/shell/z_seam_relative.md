Relacionado ao zenture em z
====
Quando a costura é colocada em um local especificado pelo usuário de acordo com o parâmetro [alinhamento do Z -Z](Z_seam_type.md), você pode inserir as coordenadas do local onde a costura deve ser colocada.Normalmente, essas coordenadas indicam um local na bandeja de impressão, por exemplo, na parte traseira da impressora.Se esse parâmetro for ativado, essas coordenadas serão retiradas da posição do modelo.

![Desativado: as coordenadas indicam uma posição absoluta no centro da bandeja de impressão, de modo que todas as tiras brancas apontam para o meio](../../../articles/images/z_seam_relative_disabled.png)

![Ativado: as coordenadas se relacionam com o modelo, para que cada modelo tenha as tiras brancas no mesmo canto](../../../articles/images/z_seam_relative_enabled.png)

Quando uma rede é duplicada na bandeja de impressão, esse ajuste significa que a costura está posicionada exatamente no mesmo local para cada uma das duplicatas, em vez de fazê -las apontar para o mesmo ponto no conjunto.Isso permite imprimir cada cópia exatamente da mesma maneira, qualquer que seja a posição deles no conjunto de impressão.