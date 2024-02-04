Rotação alternativa nas camadas externas
====
Quando a parte superior e a parte inferior são impressas com linhas ou padrões em [Zigzag](../top_bottom/top_bottom_pattern.md), as linhas são normalmente orientadas nas direções diagonais, alternando as duas direções cada vez que possível.Se esse parâmetro for ativado, ele alternará em quatro direções: duas direções diagonais, verticais e horizontais.

![Alternando quatro direções](../../../articles/images/skin_alternate_rotation.gif)

Este parâmetro substituirá o parâmetro [sens da linha superior/abaixo](../top_bottom/skin_angles.md).O comportamento é o mesmo, no entanto.De fato, esse parâmetro pode ser completamente emulado ao inserir os ângulos `[45, 135, 0, 90]`.

Em geral, sua impressão será a mais rígida na direção do comprimento das linhas.Se esse parâmetro não for ativado, ele estará nas duas direções diagonais, o que o tornará mais baixo nas direções de ortografia.Essas direções diagonais são escolhidas porque os mecanismos de portão mais comuns para impressoras 3D usam mais motores para o movimento diagonal, o que lhes permite acelerar mais rapidamente nessas direções.

Se esse parâmetro for ativado, as instruções das linhas serão distribuídas de maneira mais uniforme.A força do objeto é assim distribuída de maneira mais uniforme.Isso fortalece o objeto nas direções vertical e horizontal, mas ligeiramente mais baixa nas direções diagonais.Também leva um pouco mais de tempo para imprimir o objeto.