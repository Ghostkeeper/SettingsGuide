Flujo de la piel del puente
====
Esta configuración ajusta la cantidad de material que se extruye para imprimir las caras inferiores de los puentes.

<!--screenshot {
"image_path": "bridge_skin_density_100.png",
"models": [{"script": "bridge.scad"}],
"layer": 80,
"settings": {
    "bridge_settings_enabled": true,
    "bridge_skin_density": 100,
    "bridge_skin_material_flow": 100,
    "bridge_wall_material_flow": 100
},
"camera_position": [0, 18, 79],
"colours": 64
}-->
<!--screenshot {
"image_path": "bridge_skin_material_flow_50.png",
"models": [{"script": "bridge.scad"}],
"layer": 80,
"settings": {
    "bridge_settings_enabled": true,
    "bridge_skin_density": 100,
    "bridge_skin_material_flow": 50,
    "bridge_wall_material_flow": 100
},
"camera_position": [0, 18, 79],
"colours": 64
}-->
![Al 100% de flujo, las líneas se dibujan a su ancho normal](../images/bridge_skin_density_100.png)
![Al 50% de flujo, las líneas se hacen más finas](../images/bridge_skin_material_flow_50.png)

La reducción de la cantidad de material reducirá efectivamente el ancho de línea del lado inferior que está haciendo de puente. Con una anchura de línea reducida, la relación superficie-masa de las líneas es mayor, lo que permite que se enfríen más rápido y esto evitará que se comben tanto.

Sin embargo, si se reduce demasiado el caudal, se producirá un gran cambio en el mismo, sobre todo si se combina con una [velocidad de impresión más lenta] (bridge_skin_speed.md). En realidad, el material no podrá cambiar su caudal muy rápidamente, lo que hace que las líneas sean algo más gruesas de lo previsto cuando el caudal se ralentiza, y algo más finas de lo previsto cuando el caudal se acelera.