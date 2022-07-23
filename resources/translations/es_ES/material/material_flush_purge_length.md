Longitud de la purga de lavado
====
Si la impresora necesita cambiar el filamento que pasa por una determinada boquilla, necesita purgar el material sobrante que todavía estaba en la cámara de la boquilla. Este ajuste determina la cantidad de material que se utiliza para expulsar el material anterior.

Esto sólo se aplica al momento después de cambiar a un tipo de material diferente. Si se vuelve a cargar el mismo tipo de material (por ejemplo, porque la bobina anterior estaba vacía), se utiliza una [longitud diferente](material_end_of_filament_purge_length.md).

**Este ajuste no es visible actualmente en la interfaz de Cura. Sólo puede ser establecido por los perfiles. Tampoco es utilizado por Cura durante el corte. Sin embargo, las impresoras que entienden el formato de archivo de material de Cura pueden utilizarlo para configurar correctamente su procedimiento de cambio de filamento.** A través de un script de post-procesamiento se puede insertar el comando `M600` en la impresión, lo que desencadenará un cambio de filamento.