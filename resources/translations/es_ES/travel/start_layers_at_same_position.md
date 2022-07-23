Iniciar capas con la misma parte
====
Originalmente, este ajuste hacía que la impresora iniciara cada capa con el objeto más cercano a la posición especificada en los ajustes [Inicio de capa X](layer_start_x.md) y [Inicio de capa Y](layer_start_y.md), en lugar de con el objeto que se imprimió en último lugar en la capa anterior.

**El ajuste se ocultó en Cura 2.4, pero no se eliminó correctamente, por lo que este ajuste todavía existe en esta lista. Sin embargo, no tiene ningún efecto en la impresión.**

El comportamiento alternativo ya no era posible después de que se implementara el corte multihilo, por lo que el ajuste se ocultó.

La impresión de cada capa en el mismo orden evita que se apilen dos capas inmediatamente después de la otra, si hay varias partes para imprimir. Esto permite que la capa anterior se enfríe más tiempo mientras la boquilla está ocupada imprimiendo las otras partes. Esto mejora el voladizo y reduce la formación de bandas y el hundimiento. Por otro lado, hace que la impresora se desplace un poco más, aumentando ligeramente el tiempo de impresión.