Topografía
====
El efecto "topografía" se produce cuando se imprime una cara superior o inferior inclinada con una pequeña cantidad de capas, de manera que los límites entre las capas están lo suficientemente separados como para que sean fáciles de ver. Recibe su nombre de los [mapas topográficos](https://en.wikipedia.org/wiki/Topographic_maps) en los que las diferencias de altitud suelen indicarse con líneas de contorno.

Se pueden ver claramente los bordes de las capas](../images/topography.jpg)

Este efecto es omnipresente en la impresión 3D, y una de las formas más fáciles de reconocer que un objeto ha sido impreso en 3D. Puede evitarse, pero evitarlo suele reducir la productividad de forma significativa.

Altura de las capas
----
Dado que el efecto de topografía se produce cuando los bordes entre las capas están muy separados, el efecto puede evitarse reduciendo la [altura de la capa] (../resolution/layer_height.md). Cuando se reduce la altura de la capa, los incrementos verticales más pequeños entre las capas también darán lugar a pasos horizontales más pequeños, lo que reduce el efecto de topografía. Sin embargo, la reducción de la altura de la capa aumenta en gran medida el tiempo de impresión.

En lugar de reducir la altura de la capa para toda la impresión, también puede reducir la altura de la capa sólo para las pendientes poco profundas de la impresión mediante el uso de [Adaptive Layer Height](../experimental/adaptive_layer_height_enabled.md). Esto reduce en gran medida el efecto de la topografía y tiene un impacto mínimo en el tiempo de impresión. Sin embargo, es más difícil ajustar la impresión para otras calidades, ya que el ajuste suele depender de la altura de la capa.

Ajustes del modelo
----
También se puede considerar la posibilidad de girar el modelo de manera que no haya más pendientes poco profundas en la impresión. Sin embargo, esto suele implicar la impresión de mucho más soporte para el modelo, lo que también reduce la productividad, y los voladizos pueden no quedar tan bien.