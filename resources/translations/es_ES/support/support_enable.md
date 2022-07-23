Generar soporte
====
Las impresoras 3D con fabricación de filamento fundido funcionan colocando un cordón de plástico fundido en los lugares adecuados. Si este plástico no está soportado, se descolgará, porque es empujado fuera de la boquilla con una fuerza significativa y debido a la gravedad. A menos que el modelo esté debajo para soportar la nueva capa, tendrá que ser apoyado por una estructura de soporte adicional, que se retira y se descarta después de imprimir el modelo.

Este ajuste permite crear estructuras de soporte para apoyar el objeto mientras se imprime. Cura no habilitará este soporte por defecto, pero marcará la superficie del modelo en rojo si piensa que el material allí podría combarse mucho si no se habilita el soporte.

<!--screenshot {
"image_path": "support_enable_prepare_mode.png",
"models": [{"script": "pipe_corner.scad"}],
"camera_position": [77, 197, 40],
"layer": -1
}-->
<!--screenshot {
"image_path": "support_enable.png",
"models": [{"script": "pipe_corner.scad"}],
"camera_position": [77, 197, 40],
"settings": {"support_enable": true},
"colours": 64
}-->
![Marcando en rojo el modelo donde se necesita soporte](../images/support_enable_prepare_mode.png)
![Estructura de soporte (en cian) para soportar el modelo durante la impresión](../images/support_enable.png)

La impresión del soporte requiere una cantidad significativa de tiempo y material. Cuando el soporte toca el modelo, hay que romperlo o cortarlo más tarde, una vez finalizada la impresión. Esto suele dejar una cicatriz en la superficie.

Sin embargo, el soporte es a veces completamente necesario. Por ejemplo, si el modelo tiene una pieza que apunta hacia la placa de impresión, esta pieza quedaría colgada en el aire.

Diseño para evitar el soporte
----

Aunque a veces es necesario, el soporte de impresión debe evitarse en la medida de lo posible. Existen numerosas técnicas para evitar tener que imprimir soportes. Esta es una parte importante del diseño de modelos para la impresión 3D. Aquí hay un par de técnicas mediante las cuales su modelo 3D puede ser alterado para evitar la necesidad de soporte.
* Orientar el modelo de manera que no haya superficies planas más altas que la placa de impresión.
* Evite en lo posible el diseño de voladizos.
* Si hay una superficie justo por encima de su placa de impresión, bájela hasta la placa de impresión.
* Los salientes pequeños pueden ser soportados con un ángulo de inclinación de 45 grados, transfiriendo el saliente al modelo.
* Los salientes más grandes pueden ser puenteados si se apoyan en ambos lados. Cura orientará automáticamente las líneas del lado inferior de ese saliente de forma que vayan en línea recta sobre el puente. Durante la impresión de estas líneas, la boquilla mantendrá la tensión en el cordón para que no se caiga. Esto le da el tiempo suficiente para solidificarse de manera que pueda sostenerse por sí mismo.
* Si hay un hueco en el saliente, se puede diseñar un puente de sacrificio. Se trata de una capa en la que se cierra el hueco. Esto permite un buen puente, de manera que la segunda capa pueda imprimir las paredes adecuadas del hueco en la parte superior. Después de la impresión, el hueco puede abrirse con un cuchillo, ya que sólo tiene una capa de espesor.