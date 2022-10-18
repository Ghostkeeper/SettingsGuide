Ancho de línea superior/inferior
====
El ancho de cada línea de la parte superior e inferior que se dibuja. El ancho de una línea puede ser diferente del tamaño de la boquilla simplemente extruyendo más o menos material del necesario. Si se extruye más material, el plástico fluirá hacia los lados, haciendo la línea más gruesa. Si se extruye menos material, la tensión superficial del material tiende a tirar del material hacia la línea central del recorrido de la boquilla.

<!--screenshot {
"image_path": "skin_line_width.png",
"models": [
    {
        "script": "flipper_grip.scad",
        "transformation": ["scale(0.6)"]
    }
],
"camera_position": [0, 37, 107],
"settings": {"skin_line_width": 0.8},
"layer": 300,
"colours": 64
}-->
![Las líneas del forro son significativamente más anchas que el resto](../images/skin_line_width.png)

Hacer las líneas del forro más anchas es una forma fácil de reducir el tiempo de impresión, porque serán necesarias menos líneas para imprimir los lados superior e inferior del objeto. Sin embargo, aumentarlo demasiado puede causar grandes fluctuaciones de extrusión. Esto provocará una subextrusión al imprimir la piel y una sobreextrusión al imprimir lo que venga después, porque el flujo a través de la boquilla no puede ajustarse lo suficientemente rápido. Aumentar el ancho de línea del forro también aumentará la posibilidad de que aparezcan agujeros en la superficie, lo que no es bonito e impide que sea impermeable.

Reducir la anchura de las líneas del forro tiende a producir una superficie superior más bonita, pero a un gran coste de tiempo de impresión. A menudo es más eficaz utilizar una técnica diferente, como [Alisado](../top_bottom/ironing_enabled.md) o sólo ajustar las [Ancho de línea de la superficie superior del forro](../experimental/roofing_line_width.md).