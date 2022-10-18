Modificador de la velocidad de enfriamiento de la extrusión
====
Si se activa la opción [Temperatura automática](../experimental/material_flow_dependent_temperature.md), la temperatura de impresión se ajustará en función de la cantidad de material extruido.

Cuando el material se calienta dentro de la cámara de la boquilla, esto le quita calor a la boquilla. Extruir material más rápido tiende a quitarle más calor a la boquilla. Si la sonda de temperatura no está exactamente en la punta de la boquilla, esto hace que la boquilla tenga una temperatura ligeramente inferior mientras se extruye el material que cuando está en reposo, incluso con un buen controlador PID.

Este ajuste describe la cantidad de calor que se pierde en la boquilla durante la impresión. El calor extra perdido por la extrusión se compensará aumentando la temperatura de impresión deseada desde el g-code. El valor del ajuste depende del diseño de la boquilla, de la capacidad térmica del material impreso y de la velocidad de extrusión.