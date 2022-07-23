Apoyo al tamaño de los trozos
====
Si el soporte está [dividido en trozos](support_skip_some_zags.md), este ajuste determina el tamaño de cada uno de los trozos de soporte.

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
![Cada trozo tiene unos 20 mm de ancho](../images/support_skip_some_zags.png)

Los trozos más pequeños tienden a ser más fáciles de romper que los trozos más grandes. Hay menos superficie que se pegue al modelo, por lo que se necesitará menos fuerza para arrancar el soporte. Sin embargo, también habrá más trozos que arrancar, así que si arrancar el soporte no es normalmente difícil, esto puede hacer que arrancar el soporte sea más trabajoso. Cada pieza tiene que ser arrancada individualmente, en lugar de arrancar todo el soporte en un gran trozo.

Si los trozos son muy pequeños, la integridad estructural del soporte puede verse comprometida. El soporte se asemejará más al patrón de líneas entonces, lo que tiene más posibilidades de caerse. Esto daría lugar a un mayor encordado y a una peor calidad del voladizo en los lugares en los que el soporte se caiga.