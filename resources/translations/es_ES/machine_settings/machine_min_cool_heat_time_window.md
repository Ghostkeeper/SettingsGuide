Temperatura mínima de espera
====
Este ajuste configura la duración mínima de una espera en la que se molestará en enfriar la boquilla hasta la temperatura de espera. Si la boquilla está configurada para estar en espera durante un tiempo inferior a éste, no se enfriará sino que permanecerá a la [Temperatura de impresión final](../material/material_final_print_temperature.md).

Su boquilla tiene un regulador PID, que regula la cantidad de energía que se utiliza para calentar su boquilla con el fin de alcanzar las temperaturas correctas. Cuando se ordena a la boquilla que se enfríe y se caliente con grandes diferencias de temperatura en rápida sucesión, el regulador PID tiende a calcular mal la cantidad de calor necesaria. Esto provoca grandes fluctuaciones en la temperatura real de la boquilla. Con esto, se puede evitar que pase a la [temperatura de espera](../material/material_standby_temperature.md) si la boquilla está inactiva durante un tiempo muy corto.

El valor óptimo de este ajuste depende de la sintonía de su regulador PID. Algunos reguladores manejan los cambios rápidos de temperatura objetivo mejor que otros, y esos pueden ser capaces de manejar un breve período de espera mejor. Bajar este ajuste ayudaría entonces a evitar que el material se degrade dentro de la boquilla.

**Dado que se trata de un ajuste de la máquina, este ajuste no suele ser visible en la lista de ajustes.**