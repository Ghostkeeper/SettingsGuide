Esperar el calentamiento de la boquilla
====
La capa inicial puede tener una [temperatura de la boquilla](../material/material_print_temperature_layer_0.md) diferente a la [temperatura de la boquilla del resto de la impresión](../material/material_print_temperature.md). Si este ajuste está activado, la impresora esperará hasta que se alcance esa temperatura antes de continuar la impresión.

Esperará hasta que la temperatura se caliente o se enfríe a la temperatura adecuada. Aunque la etiqueta de este ajuste dice que esperará a que se caliente, también se enfriará. El inyector no esperará a otros cambios de temperatura, como a la [Temperatura de impresión inicial](../material/material_initial_print_temperature.md), a la [Temperatura de impresión final](../material/material_final_print_temperature.md) o a la [Temperatura de espera](../material/material_standby_temperature.md). Si se imprime en [modo uno a uno](../blackmagic/print_sequence.md), la boquilla también esperará hasta que se alcance la temperatura de la capa inicial cuando tenga que volver a la primera capa para los siguientes objetos.

**Puesto que se trata de un ajuste de la máquina, este ajuste no suele ser visible en la lista de ajustes.**