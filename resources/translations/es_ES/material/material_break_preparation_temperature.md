Temperatura de preparación de la pausa
====
En algunas impresoras, cuando se retrae el material para cambiar el filamento, es necesario romperlo limpiamente para poder moverlo por el alimentador sin que se enrede. Este ajuste configura parte del procedimiento para romperlo limpiamente.

Esta configuración ajusta la temperatura de la boquilla mientras el material se retrae hacia la segunda posición para estirar el material hasta conseguir un hilo fino. Este hilo fino se estira fuera de la zona calentada de la boquilla, permitiendo que se enfríe y se solidifique. El hilo fino y duro del material puede entonces romperse en la siguiente etapa de la retracción.

![En primer lugar, el material se retrae para detener la exudación](../images/filament_switch_anti_ooze.svg)
![En segundo lugar, el filamento se retrae lentamente para dibujar un hilo fino que sea fácil de romper y dejar que este hilo se solidifique](../images/filament_switch_break_preparation.svg)
![En tercer lugar, el filamento se retrae rápidamente para romperlo](../images/filament_switch_break.svg)

**Este ajuste no es visible actualmente en la interfaz de Cura. Sólo puede ser establecido por los perfiles. Tampoco es utilizado por Cura durante el corte. Sin embargo, las impresoras que entienden el formato de archivo de material de Cura pueden utilizarlo para configurar su procedimiento de cambio de filamento correctamente.** A través de un script de post-procesamiento se puede insertar el comando `M600` en la impresión, lo que desencadenará un cambio de filamento.