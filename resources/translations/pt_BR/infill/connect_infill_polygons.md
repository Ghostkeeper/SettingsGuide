Conecte os polígonos de enchimento
====
Quando o recheio consiste em loops fechados, esses loops fechados podem ser mesclados para formar um único loop.Isso torna possível estabelecer pequenas conexões onde os polígonos são adjacentes.

Este parâmetro está disponível apenas quando o preenchimento consiste em loops adjacentes.Isso significa que um ou outro:
* O [motivo de enchimento](Infill_pattern.md) está definido para cruzar ou cruzar 3D.
* As linhas de enchimento são [multiplicadas](Infill_multiplier.md) por um número de pares.
* Existem pelo menos 2 [paredes adicionais ao redor do enchimento](Infill_wall_line_count.md).

![Com linhas de enchimento multiplicadas, existem muitos loops neste modelo de preenchimento](../../../articles/images/connect_infill_polygons_disabled.png)

![Ativando este parâmetro para mesclar os cachos](../../../articles/images/connect_infill_polygons_enabled.png)

O objetivo desta função é evitar viagens.A linha final será um único loop para cada parte conectada do recheio, para que não haja movimento de movimento.Portanto, é mais fácil trabalhar com filamentos flexíveis, porque eles são mais difíceis de se retrair e funcionar melhor se puderem continuar circulando no bico.

A conexão desses loops também pode fortalecer o material de enchimento, melhorando a conexão interna entre os loops.No entanto, quando os polígonos estão conectados, a cabeça de impressão deve fazer 180 graus pouco antes de uma articulação.Essas voltas às vezes impedem que a junta seja completamente conectada.Em alguns casos, isso também pode enfraquecer o preenchimento.Tudo depende de como os cachos se envolvem na forma do seu modelo.