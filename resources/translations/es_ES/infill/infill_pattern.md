Patrón de relleno
====
El patrón de relleno define una estructura que se utiliza para rellenar el volumen del objeto. Hay varios patrones disponibles, cada uno de los cuales tiene sus propias ventajas. Algunos están especializados en aplicaciones muy específicas.

<!--screenshot {
"image_path": "infill_pattern_grid.png",
"models": [{"script": "hexagonal_prism.scad"}],
"camera_position": [0, 0, 180],
"settings": {
    "top_layers": 0,
    "infill_pattern": "grid"
},
"colours": 64
}-->
Rejilla
----
![Rejilla](../images/infill_pattern_grid.png)

El patrón de relleno de cuadrícula crea dos conjuntos de líneas perpendiculares. Juntos forman un patrón de cuadrados.
* El patrón más fuerte en la dirección vertical.
* Bastante fuerte en las dos direcciones de las líneas.
* No tan fuerte en la diagonal.
* Muy bueno en el soporte de la superficie superior. Su superficie se verá muy suave.

<!--screenshot {
"image_path": "infill_pattern_lines.png",
"models": [{"script": "hexagonal_prism.scad"}],
"camera_position": [0, 0, 180],
"settings": {
    "top_layers": 0,
    "infill_pattern": "lines"
},
"colours": 64
}-->
Líneas
----
![Líneas](../images/infill_pattern_lines.png)

El patrón de líneas crea líneas paralelas. Por defecto, el patrón de líneas alterna su dirección perpendicularmente de capa a capa, lo que hace que se parezca al patrón de rejilla a primera vista. Sin embargo, esto puede ser alterado con el ajuste [Infill Line Directions](infill_angles.md).
<!--si cura_version<4.12:* El mejor patrón para una superficie lisa junto con el zigzag, ya que la distancia entre las líneas es la más pequeña.-->
* Tiende a ser débil en la dirección vertical, porque las capas sólo tienen pequeños puntos en los que se unen.
* Será extremadamente débil en la dirección horizontal, excepto en la única dirección en la que están orientadas las líneas. Pero incluso en esa dirección, no es resistente al cizallamiento, por lo que fallará con bastante rapidez bajo carga.

<!--screenshot {
"image_path": "infill_pattern_triangles.png",
"models": [{"script": "hexagonal_prism.scad"}],
"camera_position": [0, 0, 180],
"settings": {
    "top_layers": 0,
    "infill_pattern": "triangles"
},
"colours": 64
}-->
Triángulos
----
![Triángulos](../images/infill_pattern_triangles.png)

El patrón de triángulos crea tres conjuntos de líneas en tres direcciones diferentes. Juntos forman un patrón de triángulos.
* Muy resistente al cizallamiento.
* Resistencia aproximadamente igual en todas las direcciones horizontales.
* Las líneas superiores tienen que hacer un puente bastante largo, lo que requiere muchas capas de piel superior para conseguir una superficie superior uniforme.
* El flujo se interrumpe significativamente en las intersecciones, lo que da lugar a una resistencia relativamente baja con altos índices de relleno.

<!--screenshot {
"image_path": "infill_pattern_trihexagon.png",
"models": [{"script": "hexagonal_prism.scad"}],
"camera_position": [0, 0, 180],
"settings": {
    "top_layers": 0,
    "infill_pattern": "trihexagon"
},
"colours": 64
}-->
Tri-hexágono
----
![Tri-hexágono](../images/infill_pattern_trihexagon.png)

El patrón tri-hexágono crea tres conjuntos de líneas en tres direcciones diferentes, al igual que el patrón de triángulos, pero desplazadas entre sí para que no se crucen todas en la misma posición.
* El patrón más fuerte en la dirección horizontal.
* Aproximadamente la misma fuerza en todas las direcciones horizontales.
* Muy resistente al cizallamiento.
* Las líneas superiores tienen que formar puentes muy largos, lo que requiere muchas capas de piel superior para conseguir una superficie superior uniforme.

<!--screenshot {
"image_path": "infill_pattern_cubic.png",
"models": [{"script": "hexagonal_prism.scad"}],
"camera_position": [0, 0, 180],
"settings": {
    "top_layers": 0,
    "infill_pattern": "cubic",
    "infill_sparse_density": 19
},
"colours": 64
}-->
Cúbico
----
![Cúbico](../images/infill_pattern_cubic.png)

El patrón cúbico crea cubos, un patrón tridimensional. Los cubos se orientan de pie sobre una esquina, lo que permite imprimirlos sin que sobresalgan las superficies internas.
* Fuerza aproximadamente igual en todas las direcciones, incluida la dirección vertical.
* Bastante resistencia en todas las direcciones.
* Menor efecto de almohadillado, ya que no produce largas bolsas verticales de aire caliente.

<!--screenshot {
"image_path": "infill_pattern_cubic_subdivision.png",
"models": [{"script": "hexagonal_prism.scad"}],
"camera_position": [0, 0, 180],
"settings": {
    "top_layers": 0,
    "infill_pattern": "cubicsubdiv",
    "infill_sparse_density": 50
},
"layer": 240,
"colours": 64
}-->
Subdivisión cúbica
----
![Subdivisión cúbica](../images/infill_pattern_cubic_subdivision.png)

El patrón de subdivisión cúbica crea cubos, un patrón tridimensional. Los cubos se orientan de pie en una esquina, lo que permite imprimirlos sin que sobresalgan las superficies internas. Sin embargo, este patrón producirá cubos más grandes hacia el interior del volumen, lo que ahorra material. Deja fuera las líneas de relleno en los lugares donde son menos útiles.

Este patrón puede producir densidades de relleno inferiores a las deseadas. Es aconsejable aumentar drásticamente la densidad de relleno cuando se utilice este patrón. La optimización funciona mejor con tasas de relleno altas.

Algorítmicamente, este patrón se genera creando un cubo gigante alrededor de todo el volumen, y luego subdividiendo este cubo en 8 subcubos cuando choca con alguna pared. A continuación se repite, de modo que los subcubos que chocan con cualquier pared se subdividen una y otra vez. Esto se repite hasta que se alcanza la distancia de la línea de relleno.
* Patrón más fuerte por peso y tiempo de impresión.
* Fuerza aproximadamente igual en todas las direcciones, incluyendo la dirección vertical.
* Concentra el relleno en piezas finas.
* Reduce el efecto de almohadillado, ya que no produce largas bolsas verticales de aire caliente.
* Si se utiliza una mayor densidad de relleno, el relleno no brilla mucho a través de las paredes, lo que produce una mejor calidad de la superficie a igualdad de tiempo de impresión.
* Introduce retracciones, lo que no funciona bien con materiales flexibles o líquidas.
* Tarda más en cortarse.

<!--screenshot {
"image_path": "infill_pattern_octet.png",
"models": [{"script": "hexagonal_prism.scad"}],
"camera_position": [0, 0, 180],
"settings": {
    "top_layers": 0,
    "infill_pattern": "tetrahedral",
    "infill_sparse_density": 21
},
"colours": 64
}-->
Octeto
----
![Octeto](../images/infill_pattern_octet.png)

El patrón octeto crea una combinación de tetraedros regulares y cubos, un patrón tridimensional. De vez en cuando, se colocan múltiples líneas de relleno adyacentes entre sí.
* Crea un fuerte marco interno donde se tocan múltiples líneas paralelas. La carga se disipa rápidamente hacia este marco interno.
* Fuerte en modelos con un grosor medio de aproximadamente un centímetro.
* Reduce el efecto de almohadillado, ya que no produce largas bolsas verticales de aire caliente.
* Da lugar a una distancia de puente muy larga para la piel superior, lo que reduce la calidad de la superficie superior.

<!--screenshot {
"image_path": "infill_pattern_quarter_cubic.png",
"models": [{"script": "hexagonal_prism.scad"}],
"camera_position": [0, 0, 180],
"settings": {
    "top_layers": 0,
    "infill_pattern": "quarter_cubic",
    "infill_sparse_density": 21
},
"colours": 64
}-->
Cuarto de cubo
----
![Cuarto de cubo](../images/infill_pattern_quarter_cubic.png)

El patrón de cuarto de cubo crea un teselado tridimensional formado por tetraedros y tetraedros truncados. De vez en cuando, se colocan múltiples líneas de relleno adyacentes entre sí.
* Crea dos tramas internas disjuntas, similares al octeto, donde se tocan múltiples líneas paralelas. La carga se disipa rápidamente hacia este marco interno. Los marcos están orientados en dos direcciones diferentes, haciéndolos más débiles individualmente pero reduciendo la distancia para distribuir la carga a estos marcos.
* Fuerte en los modelos con un grosor bajo de unos pocos milímetros.
* Reducción del efecto de almohadillado, ya que no produce largas bolsas verticales de aire caliente.
* Da lugar a una distancia de puente muy larga para la piel superior, lo que reduce la calidad de la superficie superior.

<!--screenshot {
"image_path": "infill_pattern_concentric.png",
"models": [{"script": "hexagonal_prism.scad"}],
"camera_position": [0, 0, 180],
"settings": {
    "top_layers": 0,
    "infill_pattern": "concentric"
},
"colours": 64
}-->
Concéntrico
----
![Concéntrico](../images/infill_pattern_concentric.png)

El patrón concéntrico crea anillos paralelos a las paredes.
* El patrón de relleno más fuerte cuando se utiliza el 100% de relleno, ya que no sólo no se cruzan las líneas, sino que las líneas están orientadas de manera que la fuerza no isotrópica de las líneas distribuirá la carga.
* Produce las impresiones más flexibles, con una resistencia muy débil y uniforme en todas las direcciones horizontales.
* Más fuerte en la dirección vertical que en la horizontal.
* Con una densidad de relleno del 100%, el material podría aglomerarse en el centro, reduciendo la fiabilidad de la impresión de formas redondas en las que los círculos concéntricos se unen en un punto.
* Con algunas formas, algunas de las líneas de relleno podrían colgar en el aire, sin añadir resistencia adicional por el coste del material y el tiempo de impresión.
* Cuando no se utiliza el 100% de relleno, este es el patrón de relleno más débil en la dirección horizontal. No añade ninguna resistencia.

<!--screenshot {
"image_path": "infill_pattern_zigzag.png",
"models": [{"script": "hexagonal_prism.scad"}],
"camera_position": [0, 0, 180],
"settings": {
    "top_layers": 0,
    "infill_pattern": "zigzag"
},
"colours": 64
}-->
Zigzag
----
![Zigzag](../images/infill_pattern_zigzag.png)

El patrón de relleno en zigzag hace que la boquilla dibuje líneas en forma de zigzag. Esto es como las líneas, pero las líneas están conectadas en una línea larga, lo que evita las interrupciones de flujo.
* Es el segundo patrón de relleno más fuerte cuando se utiliza el 100% de relleno. Sin embargo, se imprime de forma más fiable que el relleno concéntrico con formas redondas.
* El mejor patrón para una superficie superior lisa junto con el zigzag, ya que la distancia entre las líneas es mínima.
* Tiende a ser bastante débil en la dirección vertical, ya que las capas sólo tienen pequeños puntos en los que se unen.
* Será extremadamente débil en la dirección horizontal, excepto en la única dirección en la que están orientadas las líneas. Pero incluso en esa dirección, no es resistente al cizallamiento, por lo que fallará con bastante rapidez bajo carga. 

<!--screenshot {
"image_path": "infill_pattern_cross.png",
"models": [{"script": "hexagonal_prism.scad"}],
"camera_position": [0, 0, 180],
"settings": {
    "top_layers": 0,
    "infill_pattern": "cross"
},
"colours": 64
}-->
Cruz
----
![Cruz](../images/infill_pattern_cross.png)

El patrón de relleno en forma de cruz produce una curva de llenado de espacio que produce algo que parece una cruz a lo largo del interior del volumen.
* Es uniforme en todas las direcciones horizontales, lo que lo hace útil para imprimir objetos blandos y flexibles.
* No produce líneas rectas largas en la dirección horizontal, por lo que es uniformemente blanda a lo largo de todo el perímetro. No hay puntos fuertes.
* No produce ningún tipo de retracción, lo que facilita la impresión de materiales flexibles.
* Es más fuerte en la dirección vertical que en la horizontal.
* Tarda mucho tiempo en cortarse.
* Será muy débil en todas las direcciones horizontales.

<!--screenshot {
"image_path": "infill_pattern_cross_3d.png",
"models": [{"script": "hexagonal_prism.scad"}],
"camera_position": [0, 0, 180],
"settings": {
    "top_layers": 0,
    "infill_pattern": "cross_3d"
},
"colours": 64
}-->
Cruz 3D
----
![Cruz 3D](../images/infill_pattern_cross_3d.png)

El patrón de relleno 3D cruzado produce una curva de llenado de espacio que produce algo que parece cruces a lo largo del interior del volumen. Este patrón pulsa a lo largo del eje Z para hacerlo más débil en la dirección vertical.
* Es aproximadamente uniforme en todas las direcciones, horizontales y verticales, lo que lo convierte en el patrón más útil para imprimir objetos blandos y flexibles.
* No produce líneas rectas largas, por lo que es uniformemente blando en toda la superficie.
* No produce ningún tipo de retracción, lo que facilita la impresión de materiales flexibles.
* Tarda mucho en cortarse.
* Es muy débil en todas las direcciones. 

<!--screenshot {
"image_path": "infill_pattern_gyroid.png",
"models": [{"script": "hexagonal_prism.scad"}],
"camera_position": [0, 0, 180],
"settings": {
    "top_layers": 0,
    "infill_pattern": "gyroid"
},
"colours": 64
}-->
Giroide
----
![Giroide](../images/infill_pattern_gyroid.png)

El patrón de relleno giroscópico produce un patrón ondulado que alterna las direcciones.
* Produce un volumen que es completamente permeable a los fluidos, lo que lo convierte en un patrón útil para materiales solubles.
* Es igual de fuerte en todas las direcciones, pero no es muy rígido. Esto lo hace útil para materiales flexibles, pero el resultado será algo más duro, menos blando, que los patrones de relleno en cruz (3D).
* No hay líneas superpuestas en este patrón, lo que permite imprimir con materiales con mayor tensión superficial más fácilmente y hace que el relleno sea muy fiable y consistente.
* Resistente al cizallamiento.
* Tarda mucho en cortarse y produce grandes archivos de código g. Para algunas impresoras puede ser difícil seguir el ritmo de los muchos comandos de g-code por segundo, y puede ser difícil seguir el ritmo a través de la conexión en serie en bajas velocidades de baudios.

<!--screenshot {
"image_path": "infill_pattern_lightning.png",
"models": [{"script": "hexagonal_prism.scad"}],
"camera_position": [0, 0, 180],
"settings": {
    "top_layers": 0,
    "infill_pattern": "lightning"
},
"colours": 64
}-->
<!--screenshot {
"image_path": "infill_pattern_lightning_side.png",
"models": [{"script": "three_cylinders.scad"}],
"camera_position": [148, 23, 126],
"settings": {
    "top_layers": 0,
    "wall_line_count": 0,
    "infill_pattern": "lightning",
    "infill_sparse_density": 30
},
"colours": 32
}-->
<!--if cura_version>=4.12-->
Rayos
---- 
![Rayos]../images/infill_pattern_lightning.png)
El patrón de rayos se construye desde los lados](../images/infill_pattern_lightning_side.png)

El patrón de relleno de rayos es un patrón mínimo irregular que sólo pretende apoyar la superficie superior. La densidad de relleno especificada sólo se alcanzará justo debajo del lado superior del volumen de relleno.
* Ahorra una gran cantidad de tiempo y material al producir sólo el relleno por debajo de la superficie.
* El aumento de la densidad de relleno conduce a la mejor calidad de la superficie superior de todos los patrones, mientras que no toma más tiempo y material.
* Evita que el relleno brille a través de las paredes en muchos lugares, simplemente no teniendo relleno.
* No aumenta la resistencia de la pieza de forma significativa.
<!--endif-->