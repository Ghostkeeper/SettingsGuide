Compensación de la contracción del factor de escala
====
<!--if cura_version >= 4.8-->Este ajuste escala efectivamente el modelo antes de cortarlo automáticamente. El objetivo es compensar cualquier encogimiento que ocurra cuando la impresión se enfría a temperatura ambiente. Haciendo la impresión ligeramente más grande de lo deseable, el resultado final podría ser más preciso a las dimensiones originales del modelo de entrada. Este factor de escala se aplica por igual a todas las dimensiones (X, Y y Z).

Toda la escena se escala desde su centro. Cuando se imprimen varios modelos, todos ellos se escalan desde el mismo punto de origen. Esto permite posicionar esos modelos muy juntos, sin que se superpongan en la impresión final. Las áreas de colisión de los modelos se escalan a lo largo, para que puedas ver exactamente dónde terminará tu impresión. Esto también evitará que coloques los modelos en la escena en lugares donde colisionarían con características de la impresión o de la impresora, como la torre de imprimación o los clips de la placa de construcción.

Un factor de 100% no causará ningún escalado. Un factor de escala ligeramente superior al 100% es apropiado para muchos materiales de ingeniería como el ABS o el polipropileno. Un factor de escalado inferior al 100% indicaría que el material crece al enfriarse, como una espuma quizás.

Los datos puramente químicos sobre cuánto se encoge un material entre la temperatura de impresión y la temperatura ambiente no son suficientes para predecir un buen valor para este ajuste, porque el proceso de impresión también influye en la contracción. Cuando se extruye en una línea, el plástico se estira en la dirección de la longitud de la línea, y se encoge más en ese eje. La contracción no es uniforme, pero este ajuste sólo aplica un factor de escala uniforme en todas las direcciones. Para obtener resultados precisos, es necesario aplicar el factor de escala en el eje que sea más importante para su aplicación. Si hay muchas líneas largas y rectas a lo largo de la dimensión más importante, el factor de escala deberá ser mayor.

Si el factor de escala es superior al 100,5% y está imprimiendo algo grande, Cura mostrará una advertencia de que podría empezar a experimentar [warping](../troubleshooting/warping.md).<!--endif-->

<!--si cura_version < 4.8:Este es un ajuste descriptivo, que permite a Cura saber cuánto se encoge el material cuando se enfría desde la temperatura de impresión hasta la temperatura ambiente.

Este ajuste no se utiliza actualmente para el corte. Actualmente sólo se utiliza para mostrar una advertencia al usuario cuando se imprimen cosas grandes si el ratio de encogimiento es superior al 0,5%.
-->
**Este ajuste no es visible en la lista de ajustes. Es sólo un ajuste interno que será sobrescrito por el perfil del material.**