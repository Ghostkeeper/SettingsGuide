Patrón superior/inferior
====
Este ajuste le permite elegir cómo se rellenan las superficies superior e inferior con material. Hay varios patrones de impresión disponibles, pero los patrones aquí son más limitados que para el relleno. Sólo están disponibles los patrones que crean capas sólidas.

<!--screenshot {
"image_path": "top_bottom_pattern_lines.png",
"models": [{"script": "ring_5mm.scad"}],
"camera_position": [0, 0, 100],
"settings": {"top_bottom_pattern": "lines"},
"colours": 64
}-->
Lines
----
![Líneas](../images/top_bottom_pattern_lines.png)

El patrón de líneas básico dibuja líneas rectas a través de la superficie. Estas líneas están orientadas por defecto de forma que se apoyen bien en el relleno y el soporte. La dirección de las líneas se alterna entre las capas.
* Proporciona una calidad de superficie agradable.
* Muy rígido en las direcciones en que se dibujan las líneas.
* Se adhiere fuertemente a las paredes, creando partes relativamente fuertes.

<!--screenshot {
"image_path": "top_bottom_pattern_concentric.png",
"models": [{"script": "ring_5mm.scad"}],
"camera_position": [0, 0, 100],
"settings": {"top_bottom_pattern": "concentric"},
"colours": 64
}-->
Concéntrico
----
![Concéntrico](../images/top_bottom_pattern_concentric.png)

El patrón concéntrico continúa dibujando contornos hacia el interior del modelo.
* Igual de fuerte en todas las direcciones.
* Evita la creación de bolsas de aire y huecos. Es más fácil crear objetos herméticos con este patrón.
* Gran calidad de voladizo, porque las líneas tienden a hacer un buen puente.
* Si la pieza es circular, esto puede crear un punto desagradable en el centro donde convergen los contornos.
* La calidad de la superficie es menos que ideal.

<!--screenshot {
"image_path": "top_bottom_pattern_zigzag.png",
"models": [{"script": "ring_5mm.scad"}],
"camera_position": [0, 0, 100],
"settings": {"top_bottom_pattern": "zigzag"},
"colours": 64
}-->
Zigzag
----
![Zigzag](../images/top_bottom_pattern_zigzag.png)

El patrón en zigzag es muy similar al patrón de líneas, pero en lugar de terminar las líneas en las paredes, continuará extruyendo hacia la siguiente línea de forro.
* Proporciona una gran calidad de superficie.
* Muy rígido en las direcciones en que se dibujan las líneas.
* Mantiene la tasa de extrusión más constante, lo que mejora la consistencia de la superficie para los materiales que extruyen con más dificultad.
* No se adhiere tan bien a las paredes como el patrón de líneas. Se reduce el efecto de la [Superposición del forro](skin_overlap.md). Esto hace que la pieza sea más débil y reduce la calidad de los voladizos.