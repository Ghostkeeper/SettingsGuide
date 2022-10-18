Ancho de línea de relleno
====
El ancho de cada línea de relleno que se dibuja. El ancho de una línea puede ser diferente del tamaño de la boquilla simplemente extruyendo más o menos material del necesario. Si se extruye más material, el plástico fluirá hacia los lados, haciendo la línea más gruesa. Si se extruye menos material, la tensión superficial del material tiende a tirar del material hacia la línea central del recorrido de la boquilla.

<!--screenshot {
"image_path": "infill_line_width.png",
"models": [{"script": "material_calibration.scad"}],
"camera_position": [35, 92, 122],
"settings": {"infill_line_width": 1},
"layer": 111,
"colours": 64
}-->
![Las líneas de relleno son significativamente más anchas que el resto](../images/infill_line_width.png)

Hacer las líneas de relleno más anchas puede hacer su impresión más fuerte y reducir el tiempo de impresión también. Sin embargo, aumentarlo demasiado puede causar grandes fluctuaciones de extrusión. Esto causará subextrusión cuando se imprima el relleno y sobreextrusión cuando se imprima lo que viene después del relleno, porque el flujo a través de la boquilla no puede ajustarse lo suficientemente rápido.

**Las líneas de relleno pueden ser más anchas de lo que indica esta configuración, si ha ajustado la configuración [Grosor de la capa de relleno](../infill/infill_sparse_thickness.md).**