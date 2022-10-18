Molde
====
En lugar de imprimir el modelo en sí, esta función hace que la impresora cree un negativo del modelo, un molde, en el que se puede fundir un material diferente para crear el modelo. Este molde tiene varias propiedades específicas que hacen que se pueda fundir con él y que se pueda imprimir con la impresión FFF. Esto permite el proceso de [Rapid Casting](https://en.wikipedia.org/wiki/Rapid_casting).

<!--screenshot {
"image_path": "mold_enabled_shell.png",
"models": [{"script": "stature.scad"}],
"camera_position": [-78, 160, 228],
"layer": -1
}-->
<!--screenshot {
"image_path": "mold_enabled_mould.png",
"models": [{"script": "stature.scad"}],
"camera_position": [-78, 160, 228],
"settings": {
    "mold_enabled": "True"
},
"colours": 32
}-->
![Un modelo que quieras fundir](../images/mold_enabled_shell.png)
![El molde para ese modelo](../images/mold_enabled_mould.png)

La generación de moldes de Cura creará un hueco con la forma exacta que se desea moldear. Alrededor de este hueco, se generará un caparazón con una determinada anchura, configurable a través del ajuste [Anchura mínima del molde](mold_width.md). Por encima y por debajo del molde, se generará una piel con una altura determinada, configurable a través del ajuste [Altura del techo del molde](mold_roof_height.md). Sin embargo, esta piel no se generará en la parte superior del modelo para que pueda verter el material de fundición allí. Tampoco se generará en la parte inferior del modelo. Se supone que la mantendrá en la placa de construcción mientras se está fundiendo.

Diseñar un molde
----
La generación de moldes de Cura no es perfecta. Faltan un par de cosas. Aquí hay algunos consejos para solucionarlos.
* Cura no crea bebederos para todos los máximos locales de su modelo. Es necesario añadir barras verticales a su modelo donde se necesita un bebedero.
* Cura no permite fundir material extra en caso de que su material se encoja al enfriarse. Necesitarías añadir bebederos adicionales incluso en el punto más alto de tu modelo si estás usando un material que se encoge mucho.
* El molde de Cura es siempre de una sola pieza. Para muchas formas, esto significa que es necesario destruir el molde para poder extraerlo. Los moldes pueden ser destruidos de varias maneras; simplemente por la fuerza o calentándolo si el material interior lo permite, o utilizando un material como el PVA que se disuelve en agua.
* Cura no permite poner barras o alambres para reforzar el molde. Para permitirlo, pon barras adicionales en tu modelo para que Cura deje cavidades para ellas, e inserta la varilla o el alambre después.
* Los socavones en su molde se generan sin previo aviso. Si tu molde necesita muchos socavones, necesitarás algunos bebederos u otros canales para que el material fluya correctamente allí y para que salga el aire. Además, ten en cuenta que es posible que haya que destruir el molde para sacarlo una vez solidificado.

Materiales para imprimir el molde
----
El molde ideal es:
* muy rígido
* resistente a las altas temperaturas
* químicamente inerte para que no se adhiera a su material de fundición
* hecho de un material que no se encoge

Además, algunos moldes deben destruirse para poder sacar el modelo. Para ello, puede elegir un material frágil o un material que pueda disolverse con agua u otros productos químicos, como el PVA.

Materiales para moldear
----
Hay muchos tipos de materiales para fundir un molde. Algunos son más compatibles con los moldes impresos en 3D que otros. Estos son algunos ejemplos de materiales que pueden funcionar:
* **Silicona**. La silicona no se adhiere a los plásticos, por lo que es fácil de desmoldar. La silicona también es muy flexible y esto hace que sea indulgente con los recortes. Además, las siliconas son termoestables y resistentes al calor, por lo que también se puede considerar la posibilidad de fundir el molde una vez fraguado. Sin embargo, se necesitan algunas herramientas especiales para moldear la silicona. En particular, necesitarás una cámara de vacío para bombear las burbujas de gas de la silicona.
* **Arena**. La arena es un estándar de la industria para hacer un negativo de algo, ya que es muy resistente al calor pero no necesita ser calentada para ser fundida. Después de fundirla, puedes unirla con hormigón o pegamento para evitar que se deshaga. Luego puedes utilizarlo para hacer otro negativo de un material más resistente al calor.
* **Estuco**. Es similar a la arena, pero generalmente de grano más fino. Tiene la ventaja de que el aglutinante ya está incluido en el material, por lo que no es necesario aglutinarlo. Sin embargo, el resultado final puede ser más frágil.
* **Cera**. Para hacer velas o figuras personalizadas, puedes fundir un modelo en cera. La cera tiene una temperatura de fusión baja, por lo que no fundirá el molde. Además, no se adhiere a los plásticos, por lo que es más fácil de desmoldar. La cera es muy maleable y fácil de modificar una vez desmoldada. Si haces una vela personalizada con ella, no olvides insertar una mecha antes de que se cuaje.
* **Chocolate**, como un regalo especial personalizado. Para fundir el chocolate, hay que derretirlo por encima de su punto de fusión, verterlo en el molde, vibrarlo un poco para que salgan las burbujas de aire y meterlo inmediatamente en el congelador. Incluso puede poner el molde en un baño de agua fría dentro del congelador para restarle calor más rápidamente. Después de cinco minutos, saca el chocolate con cuidado del molde.

La impresión FFF sólo puede funcionar con termoplásticos. Los termoplásticos son plásticos que intrínsecamente se ablandan a altas temperaturas. Esto no es compatible con los materiales de fundición que se calientan al fundir. Algunos materiales que generalmente son incompatibles con los moldes impresos en 3D:
* **Metales**, que necesitan ser calentados por encima del punto de fusión de los plásticos para ser lo suficientemente líquidos para fundir. La masa de calor del metal hará que su molde se derrita.
* **Los plásticos que se unen** al plástico del que está hecho el molde. No podrías separar el molde del modelo después de la fundición. Puedes pulverizar un poco de desmoldeante, pero si el material es demasiado parecido, se seguirá adhiriendo permanentemente al molde.
* **Materiales que encogen** demasiado después de solidificarse. Los materiales que se encogen antes de solidificarse están bien, siempre y cuando se disponga de bebederos suficientemente largos para que el nuevo material rellene la cavidad cuando esto ocurra.
* **La resina epoxi** no es apropiada porque mientras la resina está fría mientras se funde, la reacción química de los dos componentes libera suficiente calor para fundir el plástico. Además, el epoxi tiende a pegarse muy bien a los plásticos.

Si necesita crear un objeto en un material que no es directamente compatible con la impresión 3D, debe trabajar en múltiples etapas de fundición. Cada etapa crea un negativo de la etapa anterior. Por ejemplo, puedes imprimir la forma de tu objeto normalmente (con esta configuración desactivada), y luego crear un negativo de eso poniendo el molde en un baño de estuco. Dado que el estuco es mucho más resistente al calor, puede utilizar materiales que necesitan calentarse más para fundirse, como el bronce, o materiales que se unen a los plásticos, como el epoxi.

El proceso de fundición
----
La fundición con un molde impreso en 3D es, en gran medida, igual que con cualquier otro molde y dependerá en gran medida de los materiales utilizados. Sin embargo, hay algunos puntos a los que hay que prestar especial atención cuando se trata de moldes impresos en 3D.

El termoplástico con el que ha impreso su molde tiene una baja capacidad térmica y puede tener una temperatura de transición vítrea razonablemente baja. Esto significa que el tiempo es esencial una vez fundido el molde. Si el material se enfría con demasiada lentitud, el molde podría ablandarse. Esto puede hacer que el molde se deforme y que sea más difícil desmoldarlo. Para acelerar el fraguado del molde, puede, por ejemplo, sumergirlo en un baño de hielo.

Los moldes impresos en 3D también tienen más crestas a lo largo de sus lados debido a los límites entre las capas. Esto hace que sea más difícil desmoldar el molde. Si utiliza un agente de desmoldeo entre el molde y la pieza de fundición, utilice algo que pueda rellenar estos huecos. Los lubricantes finos no son suficientes. Las capas de interfaz más adecuadas son la cera o los lubricantes más gruesos.