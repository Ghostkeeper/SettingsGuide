Temperatura automática
====
Cuando se imprime más rápido, es mejor imprimir a una temperatura ligeramente superior. Esto hace que el termoplástico sea más fluido, permitiendo que fluya más rápidamente fuera de la abertura de la boquilla. Esta configuración ajusta la temperatura automáticamente en función del flujo medio de material que sale de la boquilla.

Para saber cuánto debe ajustarse la temperatura, se hace referencia al [Gráfico de temperatura de flujo](material_flow_temp_graph.md). El caudal se calcula en milímetros cúbicos por segundo. Poniendo eso en la relación de temperatura de flujo se obtiene una temperatura determinada. Esta temperatura se utilizará como temperatura de impresión. Cuando se activa este ajuste, el ajuste ordinario [temperatura de impresión](../material/material_print_temperature.md) dejará de utilizarse en favor de la temperatura calculada a partir del caudal.

El objetivo de este ajuste es conseguir una mejor calidad de impresión, reduciendo la sobreextrusión y la subextrusión, si hay grandes cambios de flujo dentro de una impresión. Un caso común para esto es la frontera entre la piel y el relleno. Debido a que la piel se imprime normalmente mucho más lento que el relleno, las capas en las que hay mucho relleno deben imprimirse a una temperatura ligeramente superior para que el material pueda ser extruido correctamente durante la impresión de ese relleno.

En muchas impresoras, el regulador PID que regula las temperaturas en la boquilla de la impresora tiende a reaccionar de forma exagerada cuando hay muchos cambios de temperatura en un corto periodo de tiempo. Esto puede causar que la temperatura de impresión sea muy inexacta cuando se utiliza este ajuste.

**Este ajuste no es visible actualmente en la interfaz de Cura y no puede ser activado.