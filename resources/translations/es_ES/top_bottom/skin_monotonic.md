Orden monotónica superior/inferior
====
Normalmente, Cura ordena las líneas superiores/inferiores de forma que la distancia de recorrido entre ellas sea pequeña. Si esta opción está activada, ordenará las líneas superiores/inferiores de forma que las líneas adyacentes se impriman siempre solapadas en la misma dirección.

Cuando se imprimen líneas superiores/inferiores, las líneas suelen solaparse un poco con las líneas contiguas, porque la forma de una línea no es un rectángulo perfecto. Este solapamiento da a las líneas una ligera inclinación, lo que hace que reflejen la luz de forma diferente en distintas direcciones. Si las líneas adyacentes se superponen de forma diferente, este reflejo cambia. Esto se puede ver en el resultado final. Da a las distintas zonas de la superficie un brillo diferente. La impresión en un orden monotónico garantiza que el solapamiento sea el mismo en toda la superficie, por lo que no hay diferencias en la forma de reflejar la luz. Esto hace que la superficie tenga un aspecto más consistente y suave.

<!--screenshot {
"image_path": "skin_monotonic_disabled.gif",
"models": [
    {
        "script": "yen.scad",
        "transformation": ["scale(0.5)"]
    }
],
"camera_position": [0, 0, 130],
"settings": {
    "wall_line_count": 1,
    "skin_outline_count": 0,
    "travel_compensate_overlapping_walls_enabled": false,
    "skin_monotonic": false
},
"layer": 1,
"line": [48, 68, 88, 108, 128, 148, 168, 180, 200, 220, 232, 276, 302, 334, 354, 374, 394, 422, 442, 472, 492, 521, 541, 556],
"delay": 125,
"colours": 32
}-->
<!--screenshot {
"image_path": "skin_monotonic_enabled.gif",
"models": [
    {
        "script": "yen.scad",
        "transformation": ["scale(0.5)"]
    }
],
"camera_position": [0, 0, 130],
"settings": {
    "wall_line_count": 1,
    "skin_outline_count": 0,
    "travel_compensate_overlapping_walls_enabled": false,
    "skin_monotonic": true
},
"layer": 1,
"line": [51, 71, 100, 120, 141, 161, 192, 212, 233, 253, 281, 309, 339, 367, 386, 406, 426, 446, 466, 486, 506, 526, 546, 557],
"delay": 125,
"colours": 32
}-->
![Orden no monotónico](../images/skin_monotonic_disabled.gif)
![Orden monotónico, siempre desde la esquina inferior derecha](../images/skin_monotonic_enabled.gif)

El orden monotónico aumentará ligeramente la duración de los movimientos de desplazamiento, pero este efecto es muy mínimo. Sólo tiene un efecto visual en la impresión. No hay ventajas mecánicas en el ordenamiento monotónico.

Para conseguir una superficie lisa, considere la posibilidad de emparejar este ajuste con la configuración del [Modo de peinado](../travel/retraction_combing.md) para evitar la piel, y quizás habilitar [Z Hops](../travel/retraction_hop.md). Alternativamente, también podrías habilitar [planchado](ironing_enabled.md), pero eso anula completamente la utilidad de este ajuste. El planchado tiene su propia [opción monótona](ironing_monotonic.md).

![El brillo es diferente cuando las líneas se imprimen en orden inconsistente](../images/skin_monotonic_disabled.jpg)
![Con el orden monotónico, el brillo es el mismo en todas partes](../images/skin_monotonic_enabled.jpg)