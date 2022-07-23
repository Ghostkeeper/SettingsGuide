Velocidad de retracción de rotura
====
En algunas impresoras, cuando se retrae un material para un cambio de filamento, el material debe romperse limpiamente para poder moverlo a través del alimentador sin que se enrede. Este ajuste configura parte del procedimiento para romperlo limpiamente.

Esta configuración ajusta la velocidad a la que se retrae el material para finalmente romper el filamento de la mancha que inevitablemente queda en la boquilla. Mientras que la mancha en la boquilla no puede ser extraída debido a su estado fundido, la parte que se extrae no debe tener un hilo fino en su punta, ya que podría quedar atrapado en el alimentador. Esta retracción final rompe el filamento, pero es de esperar que se rompa limpiamente gracias a las dos etapas anteriores.

![En primer lugar, el material se retrae para que deje de rezumar](../images/filament_switch_anti_ooze.svg)
![En segundo lugar, el filamento se retrae lentamente para dibujar un hilo fino que sea fácil de romper y dejar que este hilo se solidifique](../images/filament_switch_break_preparation.svg)
![En tercer lugar, el filamento se retrae rápidamente para romperlo](../images/filament_switch_break.svg)

**Este ajuste no es visible actualmente en la interfaz de Cura. Sólo se puede establecer mediante los perfiles. Tampoco es utilizado por Cura durante el corte. Sin embargo, las impresoras que entienden el formato de archivo de material de Cura pueden utilizarlo para configurar su procedimiento de cambio de filamento correctamente.** A través de un script de post-procesamiento se puede insertar el comando `M600` en la impresión, lo que desencadenará un cambio de filamento.