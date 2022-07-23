Patrón del soporte
====
Con este ajuste puede elegir el patrón que se utilizará para rellenar el volumen de la estructura de soporte. Los diferentes patrones tienen diferentes puntos fuertes y débiles.

<!--screenshot {
"image_path": "support_pattern_lines.png",
"models": [
    {
        "script": "calendar_holder.scad",
        "transformation": ["rotateX(90)"]
    }
],
"camera_position": [0, 0, 135],
"settings": {
    "support_enable": true,
    "support_pattern": "lines"
},
"structures": ["helpers"],
"colours": 16
}-->
Líneas
----
![Líneas](../images/support_pattern_lines.png)

El patrón de líneas dibuja líneas rectas. Las líneas están orientadas de tal manera que nunca son perpendiculares a las líneas de la piel que debe soportar (por defecto).
* Es el más fácil de eliminar del modelo de todos los patrones. Esto es muy útil si hay un área de voladizo que está cerca de la placa de impresión. Se puede utilizar un cuchillo para cortar los restos si es necesario.
* Proporciona la mejor calidad de voladizo de todos los patrones junto con Zigzag. Las líneas están muy juntas y orientadas de forma que no son perpendiculares a la piel.
* Tiende a ser inestable, ya que las líneas son propensas a volcarse.

<!--screenshot {
"image_path": "support_pattern_grid.png",
"models": [
    {
        "script": "calendar_holder.scad",
        "transformation": ["rotateX(90)"]
    }
],
"camera_position": [0, 0, 135],
"settings": {
    "support_enable": true,
    "support_pattern": "grid"
},
"structures": ["helpers"],
"colours": 16
}-->
Rejilla
----
![Rejilla](../images/support_pattern_grid.png)

El patrón de cuadrícula dibuja dos conjuntos de líneas rectas perpendiculares entre sí. Se superponen, formando un patrón de cuadrados. Por defecto, se dibuja un perímetro alrededor de este patrón.
* Muy resistente, aumenta de forma fiable.
* Proporciona una calidad de voladizo mediocre, ya que las líneas están bastante separadas.
* Puede ser difícil de quitar, ya que el soporte no se flexiona mucho.

<!--screenshot {
"image_path": "support_pattern_triangles.png",
"models": [
    {
        "script": "calendar_holder.scad",
        "transformation": ["rotateX(90)"]
    }
],
"camera_position": [0, 0, 135],
"settings": {
    "support_enable": true,
    "support_pattern": "triangles"
},
"structures": ["helpers"],
"colours": 16
}-->
Triángulos
----
![Triángulos](../images/support_pattern_triangles.png)

El patrón de triángulos dibuja tres conjuntos de líneas rectas en ángulos de 60 grados entre sí, formando un patrón de triángulos equiláteros. Por defecto, se dibuja un perímetro alrededor de este patrón.
* Es el más robusto de todos los patrones de soporte.
* Proporciona una mala calidad de voladizo, ya que las líneas están muy separadas.
* Puede ser difícil de eliminar, ya que el soporte no se flexiona en ninguna dirección.

<!--screenshot {
"image_path": "support_pattern_concentric.png",
"models": [
    {
        "script": "calendar_holder.scad",
        "transformation": ["rotateX(90)"]
    }
],
"camera_position": [0, 0, 135],
"settings": {
    "support_enable": true,
    "support_pattern": "concentric"
},
"structures": ["helpers"],
"colours": 16
}-->
Concéntrico
----
![Concéntrico](../images/support_pattern_concentric.png)

El patrón concéntrico hace que el soporte esté formado por anillos concéntricos espaciados uniformemente desde el exterior hacia el interior.
* Las líneas están muy juntas, lo que proporciona un buen soporte de las zonas salientes para una superficie lisa, si las líneas se orientan perpendicularmente.
* Bastante resistente, ya que los bucles tienen individualmente una gran anchura para apoyarse.
* Fácil de quitar, ya que la estructura de soporte se dobla hacia dentro con facilidad.
* A menudo acaba en paralelo a las paredes que debe soportar. Esto lleva a una peor calidad del voladizo, ya que algunas paredes no reciben ningún soporte.
* A veces el soporte queda suspendido en el aire.

<!--screenshot {
"image_path": "support_pattern_zigzag.png",
"models": [
    {
        "script": "calendar_holder.scad",
        "transformation": ["rotateX(90)"]
    }
],
"camera_position": [0, 0, 135],
"settings": {
    "support_enable": true,
    "support_pattern": "zigzag"
},
"structures": ["helpers"],
"colours": 16
}-->
Zigzag
----
![Zigzag](../images/support_pattern_zigzag.png)

El patrón en zigzag es como el patrón de líneas, pero las líneas están conectadas en los extremos.
* Es bastante resistente, lo que aumenta en gran medida la fiabilidad.
* Proporciona la mejor calidad de voladizo de todos los patrones junto con Lines. Las líneas están muy juntas y orientadas de forma que no son perpendiculares a la piel.
* Fácil de retirar. La estructura de soporte se dobla hacia dentro y, al tirar de ella, el soporte se desprende en tiras.
* Casi siempre dibuja el soporte en una sola línea, minimizando la necesidad de retracciones o movimientos de desplazamiento.

<!--screenshot {
"image_path": "support_pattern_cross.png",
"models": [
    {
        "script": "calendar_holder.scad",
        "transformation": ["rotateX(90)"]
    }
],
"camera_position": [0, 0, 135],
"settings": {
    "support_enable": true,
    "support_pattern": "cross"
},
"structures": ["helpers"],
"colours": 16
}-->
Cruz
----
![Cruz](../images/support_pattern_cross.png)

El patrón cruzado dibuja un patrón fraccionado en todo el volumen con formas parecidas a una cruz.
* Es el más fácil de doblar de todos los patrones, ya que no hay líneas rectas largas en este patrón.
* Casi siempre dibuja el soporte en una sola línea, minimizando la necesidad de retracciones o movimientos de desplazamiento.

<!--screenshot {
"image_path": "support_pattern_gyroid.png",
"models": [
    {
        "script": "calendar_holder.scad",
        "transformation": ["rotateX(90)"]
    }
],
"camera_position": [0, 0, 135],
"settings": {
    "support_enable": true,
    "support_pattern": "gyroid"
},
"structures": ["helpers"],
"colours": 16
}-->
<!--if cura_version >= 4.1-->
Giroide
----
[Giroide](../images/support_pattern_gyroid.png)

El patrón giroide es ondulado, con una curva que se mueve hacia adelante y hacia atrás. La curva varía a través de las capas.
* Patrón bastante robusto, lo que aumenta la fiabilidad.
* El aire entre el soporte es un volumen único. Cuando se imprime con materiales de soporte solubles, esto permite que el disolvente (agua, etanol u otro) sobresalga a todas las entrañas de la estructura del soporte, incluso si hay un borde debajo. Esto permite disolver el soporte más rápidamente.
* Soporta todas las líneas del voladizo de manera uniforme, independientemente de su dirección.
<!--endif-->