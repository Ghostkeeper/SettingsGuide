División de capas
====
La adhesión entre capas suele ser el mayor punto débil de la estructura de los objetos impresos en 3D. Si la adhesión entre las capas falla durante o poco después de la impresión, esto se denomina división de capas, separación de capas o delaminación.

Las capas se separan en el lado de este contenedor](../images/layer_splitting.jpg)

Las divisiones de capas pueden ser difíciles de tratar, porque la impresión siempre se dividirá en el eslabón más débil. Las sugerencias siguientes están orientadas a hacer la impresión más consistente y la extrusión más fiable, para eliminar los eslabones débiles en la adhesión de las capas.

Alabeo ('Warping')
----
La mayoría de las divisiones de capas son causadas por el [warping](warping.md). Esto es especialmente frecuente en los polímeros semicristalinos. Éstos forman estructuras cristalinas microscópicas al enfriarse, y se encogen mucho para formar esas estructuras. La forma más común de alabeo es que la parte inferior de la impresión se alabee hacia arriba, lo que no causa divisiones de capas. Sin embargo, si el alabeo se produce en la parte superior de la impresión, hace que las capas se separen de las adyacentes y se dividan.

Para evitar el alabeo en las capas superiores, se puede hacer una serie de cosas específicamente para reducir la posibilidad de división de las capas:
* Utilizar un patrón concéntrico [Top/Bottom Pattern] (../top_bottom/top_bottom_pattern.md). Un patrón lineal tiene líneas que se encogen todas en la misma dirección, lo que tirará de esas capas hacia arriba en la misma dirección. El patrón concéntrico difunde esa fuerza.
* Aumentar la [temperatura del volumen de construcción](../material/build_volume_temperature.md) reduce el alabeo mediante el [recocido](https://en.wikipedia.org/wiki/Annealing_%28glass%29) del plástico. Para hacer esto, la impresora necesita un volumen de construcción cerrado, manteniendo el calor.
* Del mismo modo, el uso de un [escudo contra corrientes de aire](../experimental/draft_shield_enabled.md) mantiene parte del calor, aunque con menos eficacia que un volumen de construcción cerrado.
* Evite las esquinas afiladas en el modelo 3D. Añadir un filete a una esquina afilada evita que las líneas de piel tiren directamente de las paredes subyacentes. Este suele ser un punto en el que se producirá la división de la capa.
* Utilice un material que no se encoja tanto. Por ejemplo, el PLA se deforma menos que el polipropileno. Sin embargo, la mayoría de la gente elegiría su material por requisitos específicos, por lo que esto no es una opción para ellos.

Presión insuficiente
----
Para que las capas se adhieran bien entre sí, ayuda empujar el plástico con fuerza sobre la capa anterior. Si la boquilla no extruye suficiente material, o el material no se empuja con suficiente fuerza contra la capa anterior, esto reduce la fuerza de adhesión entre las capas, permitiendo que se separen más fácilmente. Aunque esto no provoque la rotura inmediata de una capa, también reduce la resistencia de la pieza final.

Esto es principalmente un problema para las paredes. La piel tiene tanta superficie que no es propensa a partirse. Entre el relleno y las paredes, las paredes proporcionan la mayor parte de la adherencia de la capa, ya que el relleno suele imprimirse muy rápido, utilizando líneas poco distribuidas y a menudo no apiladas verticalmente.

Para garantizar una presión suficiente, es importante asegurarse de que no haya [subextrusión](underextrusion.md). Todas las causas de la subextrusión son aplicables, pero un par de ellas son de particular preocupación para la división de capas:
* Al pausar la impresión a mitad de camino, se tarda un tiempo en volver a acelerar la extrusión. El script Pause at Height tiene una opción para <!--if cura_version >= 4.7-->rehacer una capa<!--endif--><!--if cura_version < 4.7:rehacer las últimas capas-->. Esto cebará el material antes de continuar hacia arriba, evitando una capa débil con insuficiente presión de la boquilla.
* Reducir la [Velocidad de Impresión de Paredes](../speed/speed_wall.md) hace que las paredes se impriman de forma más consistente. Esto reduce la posibilidad de desarrollar puntos débiles, a la vez que reduce la subextrusión en las paredes.
* Reduzca la [Altura de la capa](../resolution/layer_height.md) o el [Ancho de la línea de la pared](../resolution/wall_line_width.md). Los caudales elevados necesitan una mayor presión. Si la impresora no puede proporcionarla, no se extruirá suficiente material para llenar las capas gruesas o las líneas anchas. Esto hace que la impresión sea más débil.
* Aumente la [Temperatura de impresión](../material/material_print_temperature.md) para asegurar que el material fluye más ampliamente, aprovechando al máximo el área de contacto, en lugar de quedarse concentrado en el centro de la línea.
* Reduce la [longitud de las retracciones] (../travel/retraction_amount.md). Las retracciones largas permiten que se filtre más material durante la retracción, provocando una subextrusión posterior. También interrumpen más el flujo. El flujo tardará más tiempo en estabilizarse después. La reducción de la longitud de retracción reduce la posibilidad de que se desarrolle un eslabón débil a lo largo de la altura de la impresión debido a un flujo inconsistente.

Superficie insuficiente
----
La adhesión entre las capas es una función de la fuerza de la unión entre los materiales multiplicada por la cantidad de superficie a la que se une. Aumentar el área de superficie ayuda a reducir la posibilidad de que las capas se dividan.

El parámetro más importante para esto es el [Espesor de la pared](../shell/wall_thickness.md). Más paredes aumenta drásticamente la superficie. Las paredes se imprimen más lentamente y se sitúan en el punto en el que se empezará a dividir, por lo que son una forma muy efectiva de aumentar la adherencia de las capas. Sin embargo, imprimir más paredes también aumenta drásticamente el tiempo de impresión y el uso de material.

Una superficie insuficiente suele ser un problema cuando se imprimen impresiones de gran tamaño, donde el alabeo es fuerte, con una sola pared y sin relleno. La pared empezará a doblarse debido al alabeo y no hay nada que lo detenga. Esto podría ser una razón para desactivar el uso del [modo espiralizar](../blackmagic/magic_spiralize.md), ya que imprime sólo una pared y evita que se genere el relleno. En su lugar, es posible que tenga que imprimir con dos paredes y establecer manualmente la densidad de relleno al 0% para lograr un efecto similar.

Materiales incompatibles
----
En las impresiones con diferentes tipos de plástico, asegúrese de que los plásticos se adhieren entre sí. Normalmente, los plásticos con relaciones de contracción muy diferentes no podrán adherirse entre sí. Los diferentes efectos químicos también harán que los plásticos se repelan entre sí, impidiendo que se peguen. Si esto ocurre en una gran zona plana en el centro de la impresión, lo más probable es que la impresión se deshaga allí.

Para evitar que esto ocurra, puede ser necesario diseñar una junta mecánica de enclavamiento entre las dos superficies. Trate los diferentes materiales como si se imprimieran por separado, salvo que no será necesario ensamblarlos después.