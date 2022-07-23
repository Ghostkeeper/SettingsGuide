Altura de capa
====
La impresora 3D coloca el plástico en capas. La altura de la capa es el grosor de estas capas en milímetros. Es el factor más importante tanto en la calidad visual de su impresión final como en el tiempo de impresión.

<!--screenshot {
"image_path": "layer_height_0.1.png",
"models": [{"script": "plunger_stop.scad"}],
"camera_position": [25, 100, 50],
"settings": {"layer_height": 0.1},
"colours": 32
}-->
<!--screenshot {
"image_path": "layer_height_0.3.png",
"models": [{"script": "plunger_stop.scad"}],
"camera_position": [25, 100, 50],
"settings": {"layer_height": 0.3},
"colours": 32
}-->
![Altura de capa 0.1 mm](../images/layer_height_0.1.png)
![Altura de capa 0.3 mm](../images/layer_height_0.3.png)

La altura de la capa es el ajuste más importante que afecta a la calidad general y, a la inversa, al tiempo de impresión. Estos son algunos de los efectos:
* Tener capas más finas aumentará la calidad visual de la impresión. Como las capas son más finas, el efecto de escalonamiento en los bordes de la capa se reducirá. Además, las capas estarán más juntas y, por tanto, los pliegues entre las capas serán más pequeños, lo que dará lugar a un acabado más suave.
* Tener capas más finas permite a la impresora producir más detalles en la parte superior e inferior de la impresión.
* Tener capas más gruesas tiende a hacer la impresión más fuerte, hasta cierto punto. Habrá menos bordes entre las capas, que tienden a ser un punto débil. Las capas más gruesas no se cortarán tanto.
* Tener capas más gruesas reducirá el tiempo de impresión, porque la boquilla no tendrá que hacer tantos movimientos horizontales.

Altura de las capas frente a los perfiles
----
Muchos ajustes dependen de la altura de la capa. Debido a que la altura de la capa afecta significativamente a la tasa de flujo de material a través de la boquilla, muchos parámetros del proceso de impresión cambiarán. Esto es muy complejo. Por ejemplo, al aumentar la altura de la capa, probablemente deba aumentar ligeramente la temperatura de impresión para compensar la tasa adicional de pérdida de calor. La temperatura afecta entonces a la liquidez del material, lo que afectará a la nitidez de las esquinas y a la refrigeración necesaria, etc. Siempre es aconsejable partir de un perfil de calidad ya disponible en su impresora que tenga una altura de capa cercana a la que usted desea.

Usted puede elegir una altura de capa deseada en el Modo Personalizado, pero los perfiles pre-hechos están disponibles con varias alturas de capa también. Puede elegir entre los perfiles para varias alturas de capa en el Modo Recomendado usando un deslizador o usando el widget desplegable en el Modo Personalizado. Dado que estos perfiles también cambian algunos parámetros que dependen de la altura de la capa, probablemente conseguirás una mejor calidad de esta manera.

Notas adicionales
----
A alturas de capa muy bajas, podrías encontrarte con el límite de resolución de tu eje Z. Busca el tamaño de paso del eje Z de tu impresora y asegúrate de que la altura de capa es un múltiplo de éste. Si no coincide correctamente, algunas capas serán más gruesas que otras, lo que provocará la aparición de bandas.

**Tenga en cuenta que el ajuste de la altura de la capa no es válido para la capa inicial de la impresión o para las capas de balsa, que tienen su propia configuración para ajustar la altura de la capa por separado. Cuando se utilizan capas adaptativas, este ajuste de altura de capa se utilizará como línea de base, pero la altura real de la capa tendrá alguna variación.**