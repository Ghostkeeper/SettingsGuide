ondulación ('Ringing','Gh
====
El ringing (a veces llamado "ghosting") es un efecto en el que aparecen ondulaciones en superficies que, de otro modo, serían planas, cerca de pequeños detalles en esa superficie. Las ondulaciones comienzan a producirse justo después de imprimir los pequeños detalles.

![Ondulaciones en la superficie](../images/ringing.jpg)

Causas
----
El ringing es causado por las vibraciones de su impresora 3D. Tratar de evitar el ringing es reducir estas vibraciones. Son especialmente pronunciadas si el cabezal de impresión se mueve en una de las frecuencias de resonancia de la estructura de tu impresora.

Es una de estas cosas que las impresoras 3D más caras suelen tratar de evitar con un marco más rígido que vibre menos. Tienen un pórtico más fuerte con barras y varillas de acero endurecido, o proporcionan un marco totalmente cerrado hecho de material muy rígido. Sin embargo, esto es caro, por lo que los modelos de impresoras 3D baratas no tienen los recursos necesarios para evitar el timbre. Las impresoras con una configuración de tubo Bowden tampoco tienen tanto ringing, ya que el cabezal de impresión es mucho más ligero que el de un cabezal de impresión de accionamiento directo (ya que el pesado motor del alimentador se apoya en el cabezal de impresión).

Aunque el timbre se manifiesta horizontalmente, las vibraciones no son siempre horizontales. La vibración de la placa de impresión hacia arriba y hacia abajo con respecto a la boquilla también es un efecto muy importante, ya que el cordón de plástico se aplasta para hacerse más ancho cuando la placa de impresión vibra más cerca, o más fino cuando vibra más lejos.

Soluciones de hardware
----
Antes de ajustar tu impresión en Cura, es una buena idea ver primero si puedes mejorar tu hardware para prevenir el ringing. Esto puede proporcionar mejoras generales de los resultados de la impresión sin tener que sacrificar otras cualidades de la impresión como la fuerza o la productividad. Aquí hay algunas cosas que puede considerar:
* Añadir amortiguadores debajo de su impresora. Puede utilizar pies de goma o simplemente colocar la impresora sobre un bloque de espuma blanda. Esto evitará las vibraciones si la mesa vibra, y evitará que la impresora haga vibrar la mesa también. Reducirá la retroalimentación que la impresora que vibra recibe de la mesa, lo que ayuda a reducir las vibraciones de alta frecuencia.
* Apriete las correas de transmisión del pórtico. Si estas correas no están apretadas, la elasticidad de su goma permite que el cabezal de impresión vibre.
* Si su cabezal de impresión tiene accesorios flexibles, como un tubo Bowden, considere la posibilidad de fijarlos para que no se tambaleen. Las cintas de sujeción funcionan bien para los tubos Bowden si hay algo a lo que se puedan atar.
* Añade más masa a la estructura de tu impresora 3D. Esto hará que sea más difícil mover el marco debido a su mayor inercia, y así será más difícil hacerlo vibrar.
* Aumentar la rigidez del bastidor de la impresora 3D con refuerzos o barras transversales adicionales. Podrías fabricarlas con materiales duraderos como el acero, pero si esto no es una opción, quizás se pueda encontrar algo en una ferretería que se ajuste con mínimos ajustes. También puedes considerar la posibilidad de imprimir en 3D estos tirantes y barras transversales, pero ten en cuenta que la mayoría de los plásticos no soportan bien la aplicación de una fuerza sostenida.

Soluciones de Cura
----
Si las soluciones de hardware no son una opción, también puedes reducir el efecto del timbre mediante algunos ajustes en la configuración de Cura.

Dado que las vibraciones son causadas por la aceleración del cabezal de impresión, las mejoras más destacadas están orientadas a reducir esas aceleraciones.
* Reducir la [velocidad de impresión] máxima(../speed/speed_print.md) reduce la duración de las aceleraciones.
* Reducir la [tasa de aceleración](../speed/acceleration_print.md) reduce directamente la aceleración y reducirá la fuerza de las vibraciones.
* En la impresión 3D, [impulso](../speed/jerk_print.md) es un término de la industria para los cambios de velocidad instantáneos en las curvas. Lo que esto significa es que esencialmente se trata de acelerar infinitamente para evitar tener que frenar demasiado en cada curva. Esto provoca aceleraciones muy elevadas durante cortos periodos de tiempo en cada curva. Reducir el tirón también puede ayudar a reducir las vibraciones. En lugar de una aceleración breve y fuerte, acelerará más lentamente y durante más tiempo, lo que reduce las vibraciones de alta frecuencia pero aumenta las de baja frecuencia.

Estos ajustes harán que su impresión dure más tiempo. Sin embargo, también puede prevenir los anillos de otras maneras, evitando el tipo de movimientos que los causan:
<!--if cura_version<5.0:* Desactive la técnica [gap filling](../shell/fill_perimeter_gaps.md) y no [print thin walls](../shell/fill_outline_gaps.md), ya que estas técnicas a veces utilizan segmentos de línea muy pequeños y movimientos extra de desplazamiento. Si se imprime una pared después, la impresora seguirá vibrando un poco.-->
* Si su impresora mueve la placa de impresión hacia arriba y hacia abajo en lugar del cabezal de impresión, no utilice [Z hops](../travel/retraction_hop_enabled.md). Estos causan que la placa de impresión vibre hacia arriba y hacia abajo mucho después de que se haya completado el salto.

También puede imprimir las [paredes interiores antes de la pared exterior](../shell/outer_inset_first.md). Como la impresión de las paredes no suele causar tantas vibraciones como otras partes, esto permite que la impresora deje de vibrar antes de que se imprima la importantísima pared exterior.

Por último, dependiendo de la geometría de tu pórtico, las vibraciones se absorben a veces de forma diferente en distintas direcciones. Girar la impresión 45 grados también puede ayudar. 