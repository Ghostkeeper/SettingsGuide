Factor de movimiento sin carga
====
Este ajuste expresa la diferencia en la longitud del filamento cuando está siendo comprimido entre el alimentador y la cámara de la boquilla.

Si el filamento está siendo empujado fuera de la boquilla, hay una contrapresión aplicada por la propia boquilla (debido a la menor apertura de la boquilla) y por el material debajo de la boquilla, ya sea la pieza impresa o la cama. Mientras tanto, el alimentador empuja desde el otro extremo. Esto comprime el filamento en la longitud del camino entre el alimentador y la boquilla, haciendo que el filamento sea efectivamente más corto. Como resultado, llevar el filamento desde el alimentador hasta la punta de la boquilla requiere menos movimiento que llevar el filamento a una posición de impresión adecuada.

Este ajuste indica a la impresora la distancia que hay que mover para llevar el filamento a la boquilla, dado que sabe la longitud de la pista desde el alimentador hasta la boquilla. Esto también puede ayudar a determinar la cantidad de material que hay que cebar para que la boquilla alcance una presión adecuada para la impresión.

Los materiales que se comprimen más fácilmente, como el TPU o el Polipropileno, tendrán un factor más bajo que los materiales rígidos como el PLA.

**Este ajuste no es visible actualmente en la interfaz de Cura. Sólo se puede establecer mediante los perfiles. Tampoco es utilizado por Cura durante el corte. Sin embargo, las impresoras que entienden el formato de archivo de material de Cura pueden utilizarlo para determinar cómo mover el filamento entre el alimentador y la boquilla.**