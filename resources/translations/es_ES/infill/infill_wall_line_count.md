Recuento de líneas de pared adicional
====
Este ajuste añade un número de contornos alrededor de las áreas de relleno. Esto es similar a aumentar el [número de paredes](../shell/wall_line_count.md), pero los contornos no van alrededor de la piel y las paredes estarán también entre la piel y el relleno. También es similar a añadir [paredes extra de la piel] (../top_bottom/skin_outline_count.md), pero alrededor del relleno en lugar de alrededor de la piel.

Estas paredes se imprimen con la configuración del relleno.

<!--screenshot {
"image_path": "infill_wall_line_count.png",
"models": [{"script": "hexasphericon.scad"}],
"camera_position": [0, 40, 136],
"settings": {
    "infill_wall_line_count": 2,
    "skin_outline_count": 0
},
"layer": 546,
"colours": 64
}-->
![Dos paredes adicionales alrededor del relleno](../images/infill_wall_line_count.png)

En comparación con la adición de paredes adicionales alrededor de la piel, este ajuste aumenta en gran medida la fuerza del modelo y reduce la visibilidad del relleno a través de la piel, pero también aumenta el tiempo de impresión y el uso de material. Mientras que las paredes adicionales de la piel reemplazarán el material que se habría impreso como piel de todos modos, este ajuste realmente añade material a menos que la densidad de relleno ya sea del 100%.

Esto es muy similar a añadir paredes extra alrededor de toda la impresión. Sin embargo, es una buena idea añadir al menos una pared extra alrededor del relleno o de la piel, porque evita que las líneas de la piel terminen en el aire.