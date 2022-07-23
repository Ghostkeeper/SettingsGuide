Flujo del muro del puente
====
Esta configuración ajusta la cantidad de material que se extruye para imprimir paredes puente.

La reducción de la cantidad de material reducirá efectivamente el ancho de línea de las paredes que hacen de puente. Con un ancho de línea reducido, la relación superficie-masa de las líneas es mayor, lo que permite que se enfríen más rápido y esto evitará que se comben tanto.

Sin embargo, si se reduce demasiado el caudal, se producirá un gran cambio en el mismo, especialmente si se combina con una [velocidad de impresión más lenta] (bridge_wall_speed.md). En realidad, el material no podrá cambiar su caudal muy rápidamente, lo que hace que las líneas sean algo más gruesas de lo previsto cuando el caudal se ralentiza, y algo más finas de lo previsto cuando el caudal se acelera. El primero de estos efectos puede compensarse con un poco de [coasting] (bridge_wall_coast.md), pero esto requiere un ajuste cuidadoso.