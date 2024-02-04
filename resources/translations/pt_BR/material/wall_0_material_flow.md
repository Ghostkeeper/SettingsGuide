Taxa de parede externa
====
Esse ajuste ajusta o fluxo apenas para a parede externa.O fluxo da parede externa pode ser ajustado separadamente do fluxo das paredes internas.

Ajustar o fluxo de parede externa é um método de parada para resolver problemas de extrusão ou precisão dimensional.O mesmo efeito também pode ser obtido ajustando os parâmetros [largura da linha da parede externa
](../Resolução/Wall_line_width_0.md) e [Inserção de parede externa](../shell/wall_0_inset.md), mas esse parâmetro pode ser uma maneira mais intuitiva de prosseguir para o ajuste inicial.

Se houver um problema de velocidade de extrusão apenas na parede externa, é preferível examinar os parâmetros [velocidades de impressão](../speed/speed_wall_0.md) e [](material_print_temperature.md).Talvez o material não receba impulso suficiente do bico e que uma velocidade de impressão mais alta possa ajudar.Talvez as linhas sejam finas demais para serem extrudadas corretamente.Talvez o material esteja muito frio ou muito quente.

Se houver um problema de precisão dimensional, é preferível examinar [larguras de linha](../Resolução/Wall_line_width_0.md), [expansão horizontal](../shell/xy_offset.md) e l '[ordem de impressão](../shell/Outer_inset_first.md).