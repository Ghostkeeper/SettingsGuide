Solapamiento ('Aliasing)'
====
Los motores paso a paso giran en pasos discretos. Su capacidad para descansar en una posición entre esos pasos es limitada. El tamaño de los pasos de los motores sirve como límite a la resolución que la impresora puede alcanzar. Cuando se imprimen paredes que están casi, pero no del todo, alineadas con el eje X o Y, esta resolución a veces se muestra como un patrón de líneas.

El patrón de aliasing que se muestra en los lados de este objeto](../images/aliasing.jpg)

La resolución de un motor paso a paso en una típica impresora 3D de consumo está en el rango de 50 a 200 pasos por milímetro. Esto hace que el tamaño de cada paso sea de unos 10 micrómetros. Si se traza una línea casi paralela al otro eje, por ejemplo, a 0,5° de la ortogonal, se producirá un paso de este tipo cada 1,15 mm a lo largo de la línea. Este escalón es demasiado pequeño para ser visible, pero las vibraciones sí lo son, sobre todo si resuenan con la frecuencia natural del cuadro.

Prevención
----
Los motores paso a paso pueden elegir entre varias estrategias para girar su eje, pero es un compromiso entre la resolución, el par y el ruido. Algunos firmware ajustan esto automáticamente basándose en la velocidad de movimiento. Algunos firmware permiten ajustar esto desde el g-code también. Por ejemplo, el comando g-code `M350` puede ser colocado en el g-code de inicio para configurar esto manualmente. Cura (actualmente) no tiene ningún método para configurar esto automáticamente basado en la velocidad o la estructura.

Sin embargo, la forma más fiable de evitar este fenómeno es ajustar el modelo de manera que el aliasing no sea visible. Gire su modelo de manera que el efecto de aliasing no se produzca. Si su modelo tiene una pared (casi) recta, asegúrese de que está completamente alineada con los ejes, o que tiene un ángulo de varios grados.