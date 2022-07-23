Eliminar las primeras capas vacías
====
Cuando se activa, cualquier capa vacía en la parte inferior de la impresión será eliminada. Toda la impresión se moverá hacia abajo hasta que se apoye en la placa de impresión. En lugar de tener capas vacías que hacen que la impresión falle, la impresión será ligeramente más baja.

Si la preferencia de Cura de "Dejar caer automáticamente los modelos en la placa de impresión" está activada, este ajuste probablemente tendrá muy poco efecto. Sin embargo, puede tener un efecto. Cuando los modelos se colocan automáticamente en la placa de impresión, los modelos se alinean exactamente con la placa de impresión. Sin embargo, si la(s) primera(s) capa(s) contiene(n) sólo características demasiado pequeñas para imprimir (quizás debido a que el fondo no es completamente liso) la primera capa puede seguir estando vacía en la impresión final. Este ajuste evitará eso moviendo el resto de las capas una hacia abajo.

Después de mover la impresión hacia abajo, los ajustes que se aplican a la primera capa se siguen aplicando. Así que aunque se elimine la primera capa original, la [Temperatura de impresión de la capa inicial](../material/material_print_temperature_layer_0.md) y otros ajustes similares se siguen aplicando a la nueva primera capa.

Normalmente esta configuración debería estar siempre activada para evitar que las impresiones fallen debido a que no son totalmente lisas en la parte inferior o están mal alineadas con la placa de impresión. Sin embargo, puede optar por desactivar este ajuste si está haciendo un trabajo de impresión con múltiples etapas que necesita comenzar en el aire.

Si [el soporte está habilitado](../support/support_enable.md), ese soporte se extenderá hasta la placa de impresión, haciendo que las primeras capas ya no estén vacías. No se eliminará ninguna capa y la impresión no se moverá hacia abajo.

Si el ajuste [Slicing Tolerance](../experimental/slicing_tolerance.md) se establece en "Exclusive", la primera capa siempre estará vacía. Si este ajuste no está activado, la primera capa estará realmente vacía y su impresión probablemente fallará.