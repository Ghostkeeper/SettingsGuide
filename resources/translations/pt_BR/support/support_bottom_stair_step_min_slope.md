Suporte mínimo de ângulo de inclinação
====
Com essa configuração, você pode desativar o fato de criar macres na parte inferior dos suportes, até que a inclinação do modelo tenha um certo ângulo.

![Escada desativada até que a inclinação seja 10 °](../../../articles/images/support_bottom_stair_step_min_slope_10.png)

![Escada desativada até que a inclinação seja 30 °](../../../articles/images/support_bottom_stair_step_min_slope_30.png)

No caso de uma inclinação baixa, as etapas da escada inferior podem ser muito amplas.Eles nunca podem ser mais amplos do que a [largura máxima](support_bottom_stair_step_width.md)), mas como essa distância é mantida de todos os lados, as etapas podem se tornar tão grandes que há uma distância importante que o suporte terá que cruzar.Se o suporte repousar em uma pequena cavidade, ele poderá soprar todo o fundo da escada, o que significa que todo o suporte é baseado apenas nos cantos das etapas.

Nesse caso, você pode limitar as etapas da escada a apenas inclinações mais íngremes.Esse cenário determina o que constitui uma inclinação "íngreme" a esse respeito.

Aumentar esse parâmetro impedirá que a cura gere etapas de escadas em superfícies rasas.Isso tornará o suporte mais sólido, mas mais difícil de remover.Seu apoio deixará mais cicatrizes na superfície.Ao reduzi -lo, o suporte será mais fácil de remover e deixará uma superfície mais bonita onde o suporte repousava, mas em alguns casos, o suporte pode ter que percorrer longas distâncias ou até parecer completamente suspenso no ar.

Para obter uma superfície bonita, é preferível deixar esse ajuste em um ângulo baixo, de aproximadamente 5 ° ou 10 °.Se o suporte for baseado em uma superfície superficial, mas não completamente plana, inspecione a visão da camada e aumente o ângulo se achar que o suporte parecerá muito precário.