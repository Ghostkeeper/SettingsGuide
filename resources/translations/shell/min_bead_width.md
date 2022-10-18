Ancho mínimo de la línea perimetral delgada
====
Este ajuste permite imprimir detalles muy pequeños con un ancho de línea que en realidad es demasiado grande para ellos. En lugar de imprimir líneas muy finas, imprime con un ancho de línea más razonable.

Si el [Tamaño mínimo de la característica](min_feature_size.md) es muy bajo, algunas partes muy finas podrían imprimirse. Esto no funciona bien. Es posible imprimir líneas más pequeñas que el tamaño de la boquilla, pero no por mucho. Imprimir líneas muy finas lleva a una extrusión inconsistente.

En su lugar, esas líneas muy finas se hacen más anchas para que se extruyan de forma más consistente. Cualquier parte del modelo que sea más delgada que el Ancho mínimo de línea perimetral delgada se imprimirá usando una sola línea del Ancho mínimo de línea perimetral delgada. Las líneas se vuelven entonces más anchas que el ancho original del modelo. Esto reduce la precisión dimensional, pero al menos se imprimirá de forma fiable.

El valor de este ajuste debe ser el ancho de línea más fino que la impresora pueda alcanzar de forma fiable antes de que empiece a crear superficies rugosas y una extrusión inconsistente. Este valor está normalmente entre el tamaño de la boquilla y la mitad del tamaño de la boquilla. Aumentar este valor hace que las piezas finas se impriman demasiado gordas, pero reduce la posibilidad de subextrusión por intentar imprimir líneas demasiado finas.