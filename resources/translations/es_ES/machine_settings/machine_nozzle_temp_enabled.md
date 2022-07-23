Activar el control de la temperatura de la boquilla
====
Si este ajuste está desactivado, Cura no enviará ningún comando de temperatura al g-code. En su lugar, Cura dejará que el firmware de la impresora caliente las boquillas antes de la impresión.

Esto es similar a [Tiene placa de construcción calefactada](machine_heated_bed.md) en su funcionamiento. Si este ajuste está deshabilitado, los ajustes de control de temperatura como [Temperatura de impresión](../material/material_print_temperature.md) no se mostrarán al usuario.

Desactivar esto temporalmente podría ser utilizado para realizar una prueba de impresión. Para ello, también tendría que [desactivar la placa de construcción](machine_heated_bed.md), el [calentamiento del volumen de construcción](machine_heated_build_volume.md) y establecer el [caudal](../material/material_flow.md) al 0%.

**Como este es un ajuste de la máquina, este ajuste no es normalmente visible en la lista de ajustes.**