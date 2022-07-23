Expansión horizontal
====
Este ajuste hace que todo el modelo sea ligeramente más ancho o más delgado. Es una medida de compensación para las imprecisiones dimensionales del proceso de impresión.

<!--screenshot {
"image_path": "xy_offset_neutral.png",
"models": [{"script": "flipper_grip.scad"}],
"camera_position": [62, -91, 176],
"settings": {"xy_offset": 0},
"colours": 32
}-->
<!--screenshot {
"image_path": "xy_offset_wider.png",
"models": [{"script": "flipper_grip.scad"}],
"camera_position": [62, -91, 176],
"settings": {"xy_offset": 1},
"colours": 32
}-->
<!--screenshot {
"image_path": "xy_offset_slimmer.png",
"models": [{"script": "flipper_grip.scad"}],
"camera_position": [62, -91, 176],
"settings": {"xy_offset": -1},
"colours": 32
}-->
![El modelo original](../images/xy_offset_neutral.png)
![Expandido horizontalmente, los orificios de los tornillos son más pequeños ahora](../images/xy_offset_wider.png)
![Un valor negativo encoge el modelo, haciendo que los orificios de los tornillos sean más anchos](../images/xy_offset_slimmer.png)

Un valor positivo hace que la impresión sea más gorda. Esto reduce el tamaño de las cavidades. Un valor negativo hará la impresión más delgada y aumenta el tamaño de las cavidades.

Si la tolerancia de una impresión es importante, este ajuste puede ser muy útil. Debido a una ligera deformación de los plásticos, las dimensiones reales de la impresión pueden no corresponder completamente con las dimensiones del modelo digital. Los errores de ganancia se pueden compensar simplemente escalando el modelo en la placa de construcción con la herramienta de escala, pero los errores de desplazamiento debidos al método de impresión se pueden compensar con este ajuste.

Si sabes que tu impresora siempre imprime demasiado ancho debido a alguna sobreextrusión o inexactitud en su movimiento, también puedes compensarlo con este ajuste.