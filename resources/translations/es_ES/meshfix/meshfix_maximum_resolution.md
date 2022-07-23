Resolución máxima
====
Aunque la entrada de alta resolución puede parecer mejor al principio, muy a menudo la impresora no maneja muy bien el código g de alta resolución. Por lo tanto, Cura reducirá la resolución de su entrada durante el proceso de corte. Este ajuste determina la resolución que Cura mantendrá como máxima.

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

La impresora necesita procesar el g-code mientras se ejecuta. Si el código g contiene muchos segmentos de línea diminutos, el cabezal de impresión puede correr por el movimiento tan rápido que el procesador de la impresora 3D es incapaz de seguir el ritmo. Esto tiene el efecto de que el cabezal de impresión se ralentizará esporádicamente para permitir que la CPU se ponga al día o simplemente para esperar el siguiente comando de movimiento. Esto hace que la superficie se vuelva muy áspera o incluso muestre pequeñas manchas porque el flujo de salida de la boquilla no coincide perfectamente con el movimiento esporádico de la boquilla. A veces, una resolución más baja da como resultado una mejor calidad de impresión.

Este ajuste indica una longitud mínima para los segmentos de línea. Los segmentos de línea que son más cortos que la longitud especificada serán considerados para ser unidos con otros segmentos de línea. Se unirán si el nuevo trazado no se desvía de su trazado original más que la [Desviación Máxima](meshfix_maximum_deviation.md)<!--if cura_version>5.0--> y el área que cubre no se desvía más que la [Desviación Máxima del Área de Extrusión](meshfix_maximum_extrusion_area_deviation.md)<!--endif-->.

Ten en cuenta que no se garantiza que se eliminen los mismos vértices de cada capa si los vértices se alinean. La reducción de resolución se realiza en 2D eliminando vértices de las formas de la capa, no en 3D eliminando vértices de la malla. En consecuencia, si se reduce demasiado la resolución, a menudo se obtiene una superficie irregular, en lugar de una superficie angular.

Se recomienda reducir la resolución del modelo de forma que el cabezal de impresión no se ralentice significativamente para dejar que la CPU se ponga al día. Si la resolución no se reduce lo suficiente, la superficie se volverá rugosa porque el cabezal de impresión reducirá su velocidad mientras continúa la extrusión. Si la resolución se reduce demasiado, la superficie también se volverá áspera porque las paredes no se apilan exactamente en todas partes.