Variación máxima de las capas adaptativas
====
Con este ajuste, puede limitar el rango a partir del cual se permite a las Capas adaptables seleccionar un grosor de capa. No se permite que la altura de la capa se desvíe más de esta variación de la [Altura de la capa] normal (../resolution/layer_height.md).

Por ejemplo, con una altura de capa normal de 0,15 mm y la variación establecida en 0,1 mm, Capas adaptables puede producir capas con un grosor entre 0,05 mm y 0,25 mm.

Este ajuste limita la potencia de la función Capas adaptables. Si el rango de espesores de las capas es demasiado estrecho, el grosor de la capa será siempre muy cercano al grosor de la capa original, tal y como se establece en el ajuste de Altura de la capa. Las capas adaptativas no harán mucho entonces para ahorrar tiempo o mejorar la calidad.

Sin embargo, si el rango es muy amplio, las capas pueden ser muy gruesas o muy finas. Las capas muy gruesas requieren mucho flujo de salida de la boquilla, lo que no siempre es posible debido al tamaño limitado de la boquilla y a la capacidad de fusión de la pista de calentamiento en el cabezal de impresión. Las capas muy finas tampoco son siempre posibles debido a la viscosidad del material o a la imprecisión del eje Z. Por lo tanto, es bueno limitar el rango al que Adaptive Layers puede ajustar el grosor de la capa. De lo contrario, la impresora tendrá dificultades para alcanzar el grosor de capa deseado.

El grosor de la capa nunca puede ser inferior a 0,001 mm, aunque el rango lo permita.