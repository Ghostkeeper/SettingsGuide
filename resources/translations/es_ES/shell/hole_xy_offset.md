Expansión horizontal de orificios
====
Esta es una medida de compensación para un efecto de impresión en el que los orificios tienden a imprimirse más pequeños de lo previsto. Con este ajuste puede ampliar el tamaño de los agujeros verticales en su impresión. Al igual que con el ajuste ordinario [Expansión horizontal](xy_offset.md), los orificios de su impresión se expandirán en todas las direcciones.

Como el orificio se expande en todas las direcciones, el valor de este ajuste se aplica efectivamente al radio de los orificios, no a su diámetro.

<!--screenshot {
"image_path": "hole_xy_offset_0.png",
"models": [{"script": "rotary_tumbler_motor_lid.scad"}],
"camera_position": [-30, 30, 111],
"settings": {"hole_xy_offset": 0},
"colours": 64
}-->
<!--screenshot {
"image_path": "hole_xy_offset.png",
"models": [{"script": "rotary_tumbler_motor_lid.scad"}],
"camera_position": [-30, 30, 111],
"settings": {"hole_xy_offset": 0.8},
"colours": 64
}-->
![Los orificios de esta impresión necesitan encajar tornillos y ejes, pero se imprimen demasiado pequeños](../images/hole_xy_offset_0.png)
![Los orificios se han hecho más grandes, pero el resto de la forma no ha cambiado](../images/hole_xy_offset.png)

Debido a la viscosidad del material, al imprimir una línea de plástico en una curva, el plástico tiende a ser arrastrado junto con la boquilla en la curva. Esto hace que la curva sea ligeramente más pequeña de lo previsto, ya que la cuerda es arrastrada hacia el interior de la curva. Normalmente esto no es realmente visible, pero cuando se imprimen artículos que necesitan encajar muy exactamente o cuando se imprimen artículos con orificios verticales muy pequeños, esto se vuelve ruinoso para la precisión de su impresión. Los tornillos ya no encajarán, las piezas ya no se deslizarán entre sí de forma limpia, etc.

Este ajuste compensa esto haciendo todos los orificios ligeramente más grandes. A diferencia de [Expansión Horizontal](xy_offset.md) esto sólo afecta a los orificios cerrados. Si hay incluso una pequeña abertura en un lado (horizontalmente, en la misma capa) entonces esa parte no se considerará un orificio y no se verá afectada por este ajuste.

Un valor positivo hará que los orificios sean más grandes. Un valor negativo hará que los orificios sean más pequeños. Cuando se combina con la Expansión Horizontal, los orificios se expanden primero antes de aplicar la expansión horizontal ordinaria. Esto puede hacer que las piezas delgadas desaparezcan por completo antes de que sean expandidas por la expansión horizontal ordinaria.

Tenga en cuenta que este ajuste sólo contempla los orificios en el plano de las capas. Sólo ajusta el tamaño de los orificios en la parte superior o inferior de la impresión. Los orificios de los lados de la impresión no se ajustan. Además, no hay restricciones en cuanto al tamaño o la forma del orificio. Cualquier cavidad que esté completamente rodeada de material en esa capa se expandirá, incluso el interior de un contenedor. Además, esto significa que en cuanto haya una abertura en el lateral de un contenedor de este tipo, el interior ya no estará completamente encerrado en esas capas, por lo que no se expandirá. Esto suele dar lugar a una cresta visible en el interior de un contenedor, exactamente a la altura de una abertura en el lateral, donde el interior no se expande momentáneamente debido a esa abertura.