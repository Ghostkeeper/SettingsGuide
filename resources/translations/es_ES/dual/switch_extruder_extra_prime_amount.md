Cantidad extra de cebado en cambio de boquilla
====
Este ajuste permite configurar la impresora para que purgue un poco de material extra cada vez que se cambia de extrusor. Está pensado para restaurar la presión en la boquilla después de que haya estado rezumando mientras otros extrusores han estado imprimiendo o durante un cambio de extrusor.

Mientras otros extrusores están imprimiendo, este extrusor habrá estado en modo de espera. Durante este tiempo, sin embargo, rezuma material. Esa pérdida de material puede compensarse empujando algo de material extra. Esto devuelve la presión a la cámara de la boquilla. El material que fue rezumado seguirá estando en la punta de la boquilla, así que a menos que se utilice una [torre de purga](prime_tower_enable.md) o [escudo de exudado](ooze_shield_enabled.md), terminará en el lado de su impresión. 

**Este ajuste es configurable por extrusor. La cantidad configurada de material se purga al *comienzo* del plan de ese extrusor, antes de imprimir con el material.**