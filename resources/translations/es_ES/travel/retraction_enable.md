Habilitar retracción
====
Si una impresora 3D dejara de empujar material, el material no dejará de fluir inmediatamente desde el final de la boquilla. Hay algo de material residual en la boquilla y estará presurizado, por lo que sigue fluyendo durante un tiempo más. Para que el material deje de fluir, la impresora necesita retraer el material fuera de la abertura de la boquilla. Esto es necesario para realizar movimientos limpios de desplazamiento sin encordarse.

<!--screenshot {
"image_path": "retraction_enable_disabled.png",
"models": [{"script": "wire_mount.scad"}],
"camera_position": [0, -115, 68],
"structures": ["travels", "helpers", "shell", "infill", "starts"],
"settings": {"retraction_enable": false},
"minimum_layer": 2,
"colours": 64
}-->
<!--screenshot {
"image_path": "retraction_enable_enabled.png",
"models": [{"script": "wire_mount.scad"}],
"camera_position": [0, -115, 68],
"structures": ["travels", "helpers", "shell", "infill", "starts"],
"settings": {"retraction_enable": true},
"minimum_layer": 2,
"colours": 64
}-->
![Retracciones desactivadas](../images/retraction_enable_disabled.png)
![Los movimientos de desplazamiento retraídos se muestran en azul más claro](../images/retraction_enable_enabled.png)

Las retracciones se realizan cuando se realiza un movimiento de desplazamiento que es especialmente sensible al encordado. Los movimientos de desplazamiento que sólo pasan por el relleno o viajan de soporte a soporte normalmente no se retraen. También hay un límite en la frecuencia con la que se puede retraer el material, a través de los ajustes [Recuento máximo de retracciones](retraction_count_max.md) y [Ventana de distancia mínima de extrusión](retraction_extrusion_window.md).

La retracción tiene importantes ventajas, pero también algunas desventajas:
* Reducirá significativamente el encordado. No habrá más cableado entre las diferentes partes de la impresión.
* Reducirá significativamente la cantidad y el tamaño de las manchas en la superficie donde la boquilla entra en el perímetro de una pieza.
* Tarda un poco en retraerse.
* El flujo de material se interrumpe cuando se produce una retracción. Esto tiene consecuencias negativas para la precisión dimensional, el banding y la subextrusión.
* El filamento podría desgastarse cuando se producen demasiadas retracciones, impidiendo que el alimentador agarre el material.

**Los materiales flexibles son más difíciles de retraer, porque tirar del filamento hace que éste se estire en lugar de sacarlo de la boquilla. Activar la retracción con estos materiales puede llevar mucho tiempo y ser relativamente ineficaz.**