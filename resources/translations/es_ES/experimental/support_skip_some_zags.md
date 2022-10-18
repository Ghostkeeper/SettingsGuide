Apoyo a la ruptura en trozos
====
Si se utiliza el [patrón] en zigzag(../soporte/support_pattern.md) para el soporte, éste puede arrugarse como una forma fácil de eliminar el soporte. Esto resulta más difícil si el soporte es muy ancho. Con esta configuración, el soporte en zigzag se rompe en trozos que son más fáciles de romper individualmente pero que siguen siendo lo suficientemente anchos como para mantener su estabilidad.

<!--screenshot {
"image_path": "support_skip_some_zags.png",
"models": [{"script": "rack.scad"}],
"camera_position": [0, 184, 10],
"settings": {
    "support_enable": true,
    "support_pattern": "zigzag",
    "support_skip_some_zags": true,
    "support_skip_zag_per_mm": 20
},
"colours": 32
}-->
![Cada 8 líneas se deja una línea de conexión, rompiendo el soporte en trozos](../images/support_skip_some_zags.png)

Romper el soporte en trozos hace que sea más fácil romper el soporte, porque se puede romper el soporte una pieza a la vez. Sin embargo, esto reduce ligeramente la fuerza y la rigidez del soporte, especialmente si el [tamaño de los trozos] (support_skip_zag_per_mm.md) se establece como muy pequeño. Como resultado, hay una posibilidad ligeramente mayor de que el soporte se caiga, lo que resulta en muchas cuerdas y malos voladizos.

Este ajuste también evita que se tire todo el soporte en una sola pieza. Si hay muchas piezas de soporte, hay que quitarlas individualmente. Si el soporte se desprende fácilmente, este ajuste puede hacer que sea más difícil quitar el soporte (aunque puede ser más fácil).

Este ajuste no se combina bien con [Support Wall Line Count](../support/support_wall_count.md). Si el soporte tiene una pared extra alrededor, esa pared conectará los trozos de nuevo, haciendo más difícil arrancarlos.