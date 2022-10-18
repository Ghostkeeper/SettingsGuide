Conectar líneas de soporte
====
Con algunos patrones de soporte, el soporte puede volverse muy inestable cuando se necesitan tiras finas de soporte. Este ajuste hará que los extremos de las líneas de soporte se conecten entre sí. Esto les da más estabilidad. También hace que el soporte se imprima con un flujo más continuo. Serán necesarios menos movimientos de desplazamiento.

<!--screenshot {
"image_path": "zig_zaggify_support_disabled.png",
"models": [{"script": "plug.scad"}],
"camera_position": [71, 71, 147],
"settings": {
    "support_enable": true,
    "support_pattern": "triangles",
    "support_wall_count": 0,
    "support_offset": 0.2,
    "zig_zaggify_support": false
},
"layer": 236,
"colours": 64
}-->
<!--screenshot {
"image_path": "zig_zaggify_support_enabled.png",
"models": [{"script": "plug.scad"}],
"camera_position": [71, 71, 147],
"settings": {
    "support_enable": true,
    "support_pattern": "triangles",
    "support_wall_count": 0,
    "support_offset": 0.2,
    "zig_zaggify_support": true
},
"layer": 236,
"colours": 64
}-->
![Líneas de soporte desconectadas](../images/zig_zaggify_support_disabled.png)
![Líneas de soporte conectadas](../images/zig_zaggify_support_enabled.png)

Cuando se dibuja una línea de soporte, en lugar de viajar a la siguiente línea, se dibujará una línea a lo largo del borde del área de soporte hacia la siguiente línea. Esto convierte todo el patrón de soporte en una sola o muy pocas líneas. Convertirlo en una sola línea no siempre es posible. El punto de partida de esta línea es arbitrario, por lo que muy a menudo habrá líneas colgando en el aire porque en una capa dos líneas pueden estar conectadas en un punto final, mientras que en la siguiente capa están conectadas en el otro lado. Esto hace que el soporte sea algo más débil, pero sigue siendo estable, y sigue evitando las interrupciones del flujo. El comportamiento de este ajuste es el mismo que el de [Conectar líneas de relleno](../infill/zig_zaggify_infill.md).

Conectar las líneas de soporte tiene un par de beneficios, pero también algunos inconvenientes:
* El soporte será más estable, menos probable que se vuelque durante la impresión.
* El flujo se mantendrá más constante, lo que le permitirá imprimir el soporte a mayor velocidad sin problemas de flujo. Esto es especialmente importante para los materiales de soporte que son difíciles de extruir correctamente.
* Si se realizan retracciones durante el soporte, serán necesarias muchas menos retracciones durante la impresión del soporte, lo que evita que el material se desbaste.
* Se necesita más material para imprimir el soporte.
* Normalmente se necesitará más tiempo para imprimir el soporte, ya que los movimientos de desplazamiento son normalmente más rápidos que la impresión de líneas de soporte.

El patrón de soporte en zigzag siempre se conecta (utilizando una técnica ligeramente diferente). Este ajuste no está disponible para el patrón en zigzag.