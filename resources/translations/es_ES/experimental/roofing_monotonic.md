Orden de la superficie superior monótona
====
Normalmente, Cura ordena las líneas de forma que la distancia de recorrido entre ellas sea pequeña. Si esta opción está activada, ordenará las líneas de la superficie superior de forma que las líneas adyacentes se impriman siempre solapadas en la misma dirección.

Cuando se imprimen las líneas de la superficie superior, las líneas suelen solaparse un poco con las líneas contiguas, porque la forma de una línea no es un rectángulo perfecto. Este solapamiento da a las líneas una ligera inclinación, lo que hace que reflejen la luz de forma diferente en distintas direcciones. Si las líneas adyacentes se superponen de forma diferente, este reflejo cambia. Esto se puede ver en el resultado final. Da a las distintas zonas de la superficie un brillo diferente. La impresión en un orden monótono garantiza que el solapamiento sea el mismo en toda la superficie, por lo que no hay diferencias en la forma de reflejar la luz. Esto hace que la superficie tenga un aspecto más consistente y suave.

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
    "skin_monotonic": false
},
"layer": 1,
"line": [29, 45, 61, 77, 93, 109, 125, 141, 157, 161, 177, 193, 199, 211, 231, 246, 262, 280, 296, 312, 326, 342, 358, 374, 397, 417, 433, 449, 464, 480, 499],
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
    "skin_monotonic": true
},
"layer": 1,
"line": [31, 47, 63, 77, 93, 109, 115, 131, 147, 163, 181, 197, 213, 229, 244, 263, 281, 296, 319, 340, 356, 372, 379, 395, 411, 427, 443, 459, 475, 491, 507, 511],
"delay": 125,
"colours": 32
}-->
![Orden no monotónico](../images/skin_monotonic_disabled.gif)
![Orden monotónico, siempre desde la esquina inferior derecha](../images/skin_monotonic_enabled.gif)

El orden monotónico aumentará ligeramente la longitud de los movimientos de desplazamiento, pero este efecto es muy mínimo. Sólo tiene un efecto visual en la impresión. No hay ventajas mecánicas en el ordenamiento monotónico.

Para conseguir una superficie lisa, considere la posibilidad de emparejar este ajuste con la configuración del [Modo de peinado](../travel/retraction_combing.md) para evitar la piel, y quizás habilitar [Z Hops](../travel/retraction_hop.md). También se puede activar [planchado](../top_bottom/ironing_enabled.md), pero eso anula por completo la utilidad de este ajuste. El planchado tiene su propia [opción monótona](../top_bottom/ironing_monotonic.md).