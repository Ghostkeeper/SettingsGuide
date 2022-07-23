Impresión de alambre
====
Este ajuste permite un modo de impresión completamente diferente llamado Impresión de alambre. Cuando se utiliza la impresión de alambre, la impresora no hará un objeto sólido, sino sólo una malla triangular de la forma exterior a partir de alambres finos.

Esta técnica tiene una serie de ventajas:
* Imprime mucho más rápido que un objeto sólido.
* Utiliza sólo una fracción del material que utilizaría la impresión normal.
* Tiene un aspecto especial, como si se hubiera construido manualmente con un bolígrafo de impresión 3D.

Sin embargo, el objeto resultante no es funcional. Tendrá más o menos el tamaño correcto, lo que lo hace útil para crear un prototipo de la sensación de escala de la impresión, aunque el tamaño tampoco será muy exacto. El objeto resultante es extremadamente frágil, no sólo durante la impresión sino también después. Es difícil sacarlo de la placa de impresión sin dañarlo. Además, el modelo perderá la mayor parte de sus detalles.

La impresión por hilo funciona colocando anillos de material con una separación vertical bastante amplia de varios milímetros. Entre estos anillos se dibuja una forma de diente de sierra que permite que el siguiente anillo se apoye sobre el anterior. Donde la superficie del modelo va en horizontal, se utiliza una técnica similar para cerrar la parte superior. En el techo, hay anillos concéntricos unidos por una forma de diente de sierra, cuidadosamente suspendidos en el aire construyendo desde fuera (donde puede apoyarse en una pared) hacia dentro.

La impresión de alambre sólo funciona realmente de forma fiable con formas que son casi completamente verticales, similares al tipo de modelo que funcionaría bien con el [Modo Espiralizar](../blackmagic/magic_spiralize.md). Si la superficie es horizontal en grandes áreas, la técnica de cierre del techo tiene que salvar una distancia extremadamente grande. En ese caso, lo más probable es que falle. Si el modelo continúa hacia arriba a mitad de camino en una superficie horizontal, es casi seguro que se imprimirá en el aire.

**La vista de capas de Cura no mostrará correctamente la impresión de alambre directamente después del corte. Sin embargo, el resultado puede ser previsualizado guardando el g-code en el disco y abriendo ese g-code con Cura de nuevo.**