Circunferencia mínima de polígono
====
Cura normalmente elimina los detalles del modelo que son más pequeños de lo que la boquilla puede imprimir. Con esta configuración, puede ajustar ese umbral para eliminar más o menos detalles. Este ajuste mide la circunferencia de cada forma en cada capa y si es menor que el valor de este ajuste, esa forma no se imprimirá.

Eliminar los detalles que son más pequeños que el ancho de una línea es una buena idea. Esto acelera el corte ligeramente. Sin embargo, esto no siempre se mantiene con las piezas que son más pequeñas que el [Ancho de línea de la pared exterior](../resolución/ancho_de_línea_de_pared_0.md) cuando las características de [Imprimir paredes finas](../shell/fill_outline_gaps.md) están activadas. Si todavía hay que intentar imprimir piezas muy pequeñas, puede reducir este ajuste.

Aumentar este ajuste también puede ayudar a eliminar pequeños detalles y conseguir una impresión más rápida. Si no necesita imprimir estos pequeños detalles puede ahorrar algunos movimientos de desplazamiento para llegar a ellos.