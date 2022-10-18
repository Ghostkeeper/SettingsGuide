Espacio intermedio de la balsa
====
Esta configuración ajusta el espacio entre las líneas adyacentes en el medio <!--if cura_version<5.0:layer--><!--if cura_version>=5.0-->layers<!--endif--> de la balsa. Esto es en cierto modo similar al ajuste [Distancia de línea de relleno](../infill/infill_line_distance.md). El propósito principal es ajustar la rigidez de la balsa y lo bien que se sostiene la capa superior.

![Dimensiones relacionadas con la balsa](../images/raft_dimensions.svg)

Tener las líneas muy separadas reduce el tiempo de impresión de la balsa. También hace que la balsa sea más fácil de doblar, lo que permite que se rompa más fácilmente. Sin embargo, si las líneas están muy separadas, las capas superiores de la balsa no se apoyan bien. Esto hace que la superficie de la balsa sea irregular, lo que reduce la adherencia entre la balsa y el modelo, pero también hace que la parte inferior del modelo sea más desordenada.