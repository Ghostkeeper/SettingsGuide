Prioridade da distância para suportes
====
A [distância x/y](support_xy_distance.md) e a [distância z](support_z_distance.md) do suporte devem ser respeitadas exatamente;nem mais nem menos.Esse método é muito restritivo, portanto deve haver uma preferência entre os dois.Este parâmetro determina essa preferência.

X/Y prioridade em z
----
! [X/y prioridade em z](../imagens/support_xy_overrides_z.svg)

Se a distância x/y for maior que a distância z, a distância x/y é sempre mantida constante, mesmo que isso signifique que a distância z é maior do que a desejada.A distância z é sempre mantida como uma distância mínima, de modo que, se a saliência é muito horizontal, a distância z sempre se aplica, tornando a distância x/y maior do que o desejado.

Z prioridade em x/y
----
! [Z prioridade em x/y](../imagens/support_z_overrides_xy.svg)

Se a distância z for maior que a distância x/y, a distância z é sempre mantida constante, mesmo que isso signifique que a distância x/y é menor do que o desejado.A distância x/y então tem alguma influência na impressão de que em lugares onde a distância Z não entra em jogo; portanto, não no topo das estruturas de suporte, mas apenas nas laterais.

Uma distância mínima x/y é sempre respeitada.Se a saliência for muito vertical, a distância x/y se tornaria tão pequena que o suporte poderia se fundir com os lados do modelo.A distância [mínima x/y](support_xy_distance_overhang.md) evita isso.