Esperar a que se caliente la placa de construcción
====
Si este ajuste está activado, la impresora esperará hasta que se alcance la temperatura de la placa de impresión cada vez que se cambie la temperatura de la placa de impresión.

Normalmente, la temperatura de la placa de impresión sólo se cambia después de la primera capa, si la [Temperatura de la placa de impresión capa inicial](../material/material_bed_temperature_layer_0.md) es diferente de la [Temperatura de la placa de impresión] normal(../material/material_bed_temperature.md). Si se imprime en [modo uno a uno](../blackmagic/print_sequence.md), la placa de construcción también se cambia cuando se comienza con la capa inicial de nuevo para el siguiente modelo. En estos casos, la impresora esperará hasta que se alcance la nueva temperatura antes de continuar la impresión.

**Puesto que se trata de un ajuste de la máquina, este ajuste no suele ser visible en la lista de ajustes.**