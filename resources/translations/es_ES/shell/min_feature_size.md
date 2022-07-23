Tamaño mínimo de la característica
====
Este ajuste controla el ancho mínimo de los detalles del modelo que se imprimirán. Cualquier cosa más fina que esto no se imprimirá.

Los detalles que sean más pequeños que el tamaño de la boquilla no se imprimirán bien. Esta es una limitación de la impresora. Sin embargo, Cura puede intentar imprimirlos, aceptando que no tendrá una buena tasa de extrusión, o que los detalles acabarán siendo más gruesos de lo modelado.

Reducir el Tamaño mínimo de la característica hace que la impresora imprima detalles más pequeños de la impresión. Dependiendo del [Ancho mínimo de la línea perimetral delgada](min_bead_width.md), estos pequeños detalles pueden ser impresos extruyendo muy poco (causando [subextrusión](../troubleshooting/underextrusion.md)), o extruyendo anchos de línea más razonables pero imprimiéndolos sobredimensionados. Si se ajusta este valor a 0, la impresora llega hasta las puntas de todas las esquinas afiladas.

Aumentar el tamaño mínimo de la característica hace que la impresora no se moleste con los pequeños detalles que no saldrían bien de todos modos. Esto ahorra un poco de tiempo y puede hacer que la impresión salga más limpia.