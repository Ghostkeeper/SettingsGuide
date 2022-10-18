Gráfico de temperatura de flujo
====
Cuando se imprime más rápido, es mejor imprimir a una temperatura ligeramente superior. Esto hace que el termoplástico sea más fluido, permitiendo que fluya más rápidamente fuera de la abertura de la boquilla. Cuando se activa [Auto Temperature](material_flow_dependent_temperature.md), este ajuste especifica para cada caudal a qué temperatura debe imprimirse el material. El caudal se promedia para cada capa para determinar una temperatura para esa capa.

El caudal se calcula en milímetros cúbicos por segundo, promediado para toda una capa. La temperatura está en grados Celsius. El valor de este ajuste debe ser una lista de coordenadas separadas por comas. Cada coordenada tiene la forma `[<caudal>, <temperatura>]`.

El objetivo de este ajuste es conseguir una mejor calidad de impresión, reduciendo la sobreextrusión y la subextrusión, si hay grandes cambios de flujo dentro de una impresión. Un caso común para esto es la frontera entre la piel y el relleno. Debido a que la piel se imprime normalmente mucho más lento que el relleno, las capas en las que hay mucho relleno deben imprimirse a una temperatura ligeramente superior para que el material pueda ser extruido correctamente durante la impresión de ese relleno.

En muchas impresoras, el regulador PID que regula las temperaturas en la boquilla de la impresora tiende a reaccionar de forma exagerada cuando hay muchos cambios de temperatura en un corto periodo de tiempo. Esto puede causar que la temperatura de impresión sea muy inexacta cuando se utiliza este ajuste.

**Este ajuste no es visible actualmente en la interfaz de Cura y no puede ser activado.