Alabeo ('Warping')
====
El alabeo es un problema de la impresión final en el que la impresión se curva después de la impresión, dejando el objeto final deformado. Normalmente, las esquinas de la parte inferior de la impresión se curvan hacia arriba, o las partes finas de la impresión se vuelven onduladas.

![Las puntas se curvan](../images/warping.jpg)

Causa
----
El alabeo es causado por una combinación de efectos, pero principalmente por la tensión interna debida a la boquilla que tira del plástico fundido. Mientras está en la transición vítrea, el plástico se comporta un poco como la goma o el chicle. Si se tira de él, el material se estira, pero si se deja de tirar vuelve a su forma original. Lo mismo ocurre durante la impresión. Al imprimir una línea larga, la boquilla tira de la línea de plástico, que se estira a lo largo de la misma. Cuando la boquilla se aleja y deja de tirar, la línea de plástico se contrae. Esta contracción provoca un tirón en todo lo que está unido a ella. Cuando suficientes líneas de plástico tiran al unísono, pueden deformar la impresión. Esto es especialmente común cuando muchas líneas son paralelas, como en el forro.

Un segundo efecto que causa la deformación es la contracción del material cuando se enfría. La mayoría de los materiales tienden a encogerse cuando se enfrían. Si el objeto se enfría de forma no uniforme, algunas partes de la impresión se encogen más que otras, lo que deforma el objeto. A medida que el objeto sigue enfriándose, se solidifica aún más, fijando esa deformación de forma permanente.

Algunos materiales son más susceptibles de encogerse que otros debido a su cristalinidad inherente. A continuación se muestran algunos coeficientes de contracción de los materiales de impresión 3D más comunes. Esto es aproximadamente lo que cada tipo de material se encoge cuando se enfría desde su temperatura de transición vítrea hasta la temperatura ambiente. Se producirán algunas variaciones entre las mezclas. Una mayor contracción causará más deformación.
* PLA: 0,21%.
* ABS: 0,70%.
* TPU: 0,63%.
* HIPS: 0.64%
* PETG y CPE: 0,45%.
* Nylon 0.62%
* PC: 0,70%.
* PP: 1,2%.

Además, el alabeo puede evitarse si hay otro material en el camino. Si una parte de la impresión es completamente densa, el material circundante puede encogerse menos o nada. Si otras partes no son completamente densas, terminará con una impresión que está parcialmente encogida. La parte encogida de la impresión tirará del resto, lo que también puede provocar deformaciones. Esto es común en la frontera entre el forro y el relleno, ya que el forro es completamente denso pero el relleno no lo es.

El alabeo es más común en la parte inferior de la impresión. Aquí el gradiente de temperatura es mayor, ya que la parte inferior de la impresión suele estar calentada por una cama caliente y el resto de la impresión no. La parte inferior también suele estar formada por muchas líneas de forro largas. Si el [patrón inferior](../top_bottom/top_bottom_pattern.md) está configurado como Líneas o Zigzag, estas líneas son largas, rectas y paralelas, lo que les permite tirar al unísono en la misma dirección para deformar el objeto.

Prevención
----
* Si el alabeo se produce en la parte inferior de la impresión, configure el [patrón de fondo para la capa inicial](../top_bottom/top_bottom_pattern_0.md) como concéntrico. De este modo, la contracción de las líneas de forro inferiores ya no tirará al unísono. La tensión interna se distribuirá uniformemente en el interior de la capa inferior. Si esto no es suficiente para evitar el alabeo, entonces también podría establecer el [patrón superior/inferior] ordinario(../top_bottom/top_bottom_pattern.md) a Concéntrico.
<!--if cura_version>=5.0-->* [Alternar las direcciones de las paredes](../experimental/material_alternate_walls.md) para reducir las tensiones internas en el modelo.<! --endif-->
* Para reducir los gradientes de temperatura dentro de la impresión, reduzca la [temperatura de la placa de impresión](../material/material_bed_temperature.md). El objeto debería enfriarse más uniformemente entonces.
* Dependiendo del hardware de su impresora, la impresión en una cámara calentada cerrada también puede evitar el alabeo. Por un lado, reducirá la diferencia de temperatura entre el volumen de impresión y la placa de impresión, y la diferencia entre el volumen de impresión y la boquilla. También permitirá que el plástico se [recupere](https://en.wikipedia.org/wiki/Annealing_%28glass%29) durante más tiempo, reduciendo las tensiones internas y, por tanto, el tirón de las líneas impresas que provoca el alabeo. Si su impresora lo soporta, considere aumentar la [temperatura del volumen de construcción](../material/build_volume_temperature.md).
* Para evitar que la parte inferior se deforme, una buena adhesión de la placa de impresión ayuda. Esto aumenta la fuerza necesaria para que el material se deforme. Por ejemplo, aumente el [ancho del borde](../platform_adhesion/brim_width.md) o el [ancho de la balsa](../platform_adhesion/raft_margin.md).
* El uso de [falda en lugar de borde](../platform_adhesion/adhesion_type.md) aleja la impresión de la placa de impresión y coloca una pieza robusta de plástico en medio que está diseñada para ser resistente a la deformación de alabeo.
* Intenta imprimir con un [parabrisas] (../experimental/draft_shield_enabled.md). Esto construye una cámara alrededor de su impresión, lo que evita que las corrientes de aire externas enfríen su impresión antes de que esté terminada. Sin embargo, ten en cuenta que el propio protector contra corrientes de aire también puede encogerse. Si el protector contra corrientes de aire falla, podrías ver un montón de hilos o espaguetis en tu impresión.
* Imprima en un material que se encoja menos, como el PLA.
* Si tiene la libertad de hacer ajustes en el modelo impreso, trate de evitar colocar esquinas exteriores muy afiladas en la placa de impresión. Puede optar por redondear algunas esquinas exteriores. Esto evita que toda la fuerza de la tensión interna se concentre en un punto, reduciendo la probabilidad de alabeo.