Desviación máxima
====
Aunque la entrada de alta resolución puede parecer mejor al principio, muy a menudo la impresora no maneja muy bien el código g de alta resolución. Por lo tanto, Cura reducirá la resolución de su entrada durante el proceso de corte. Este ajuste determina cuánto puede desviarse la trayectoria reducida de la trayectoria original para reducir la resolución.

<!--screenshot {
"image_path": "meshfix_maximum_resolution_0.05.png",
"models": [{"script": "cylinder.scad"}],
"camera_position": [40, -20, 116],
"settings": {
    "meshfix_maximum_resolution": 0.05
},
"colours": 64
}-->
<!--screenshot {
"image_path": "meshfix_maximum_resolution_1.png",
"models": [{"script": "cylinder.scad"}],
"camera_position": [40, -20, 116],
"settings": {
    "meshfix_maximum_resolution": 4,
    "meshfix_maximum_deviation": 0.5
},
"colours": 64
}-->
![Antes de reducir la resolución](../images/meshfix_maximum_resolution_0.05.png)
![Después de reducir la resolución (ad extremum)](../images/meshfix_maximum_resolution_1.png)

La impresora necesita procesar el g-code mientras se ejecuta. Si el g-code contiene muchos segmentos de línea diminutos, el cabezal de impresión puede correr por el movimiento tan rápido que el procesador de la impresora 3D es incapaz de seguir el ritmo. Esto tiene el efecto de que el cabezal de impresión se ralentizará esporádicamente para permitir que la CPU se ponga al día o simplemente para esperar el siguiente comando de movimiento. Esto hace que la superficie se vuelva muy áspera o incluso muestre pequeñas manchas porque el flujo de salida de la boquilla no coincide perfectamente con el movimiento esporádico de la boquilla. A veces una resolución más baja da como resultado una mejor calidad de impresión.

Este ajuste indica hasta qué punto se permite que el nuevo trazado de resolución reducida se desvíe del trazado original de alta resolución. Las líneas se consideran unidas con otros segmentos de línea si son más cortas que la [Resolución Máxima](meshfix_maximum_resolution.md), pero si este atajo provocara que la trayectoria se desviara más que la distancia indicada por este ajuste, las líneas no se unirán.

Ten en cuenta que no se garantiza que se eliminen los mismos vértices de cada capa si los vértices se alinean por casualidad. La reducción de resolución se realiza en 2D eliminando vértices de las formas de la capa, no en 3D eliminando vértices de la malla. En consecuencia, si se reduce demasiado la resolución, a menudo se obtiene una superficie irregular, en lugar de una superficie angular.

Por razones de integridad estructural, se recomienda encarecidamente no permitir que las trayectorias se desvíen más de medio ancho de línea. Sin embargo, si la superficie tiene que ser suave o tener un aspecto agradable, este ajuste indica básicamente la profundidad de las irregularidades en la superficie que se permite. La desviación máxima debe ser muy baja para que no se vea a simple vista.

Sin embargo, reducir demasiado la desviación máxima limita mucho la reducción de la resolución. El g-code resultante puede no imprimir bien entonces ya que la CPU no es capaz de ponerse al día con los comandos de movimiento cortos.