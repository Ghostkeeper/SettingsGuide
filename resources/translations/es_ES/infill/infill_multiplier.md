Multiplicador de línea de relleno
====
Aumentando este ajuste, Cura colocará más líneas de relleno directamente al lado de las otras líneas de relleno.

<!--screenshot {
"image_path": "infill_multiplier.png",
"models": [{"script": "gear_knurled.scad"}],
"camera_position": [18, 0, 180],
"settings": {
    "top_layers": 0,
    "infill_multiplier": 3
},
"colours": 32
}-->
![Multiplicado por 3](../images/infill_multiplier.png)

Esto aumenta efectivamente la densidad de relleno más allá de lo que especifica el ajuste [Infill Density](infill_sparse_density.md), pero en lugar de espaciar las líneas de relleno de manera uniforme, las líneas se colocan directamente adyacentes entre sí. En comparación con el simple aumento de la densidad de relleno, esto puede aumentar la fuerza del relleno, ya que las líneas de relleno son capaces de apoyarse entre sí para obtener una rigidez adicional.

Cuando se establece un multiplicador impar, las líneas de relleno originales permanecerán en su lugar, pero las líneas de relleno adicionales harán un bucle en los agujeros del patrón de relleno. Cuando se establece un multiplicador par, las líneas de relleno originales se eliminan y los bucles se colocan directamente en su lugar.

En comparación con la alternativa de aumentar la densidad de relleno en el mismo multiplicador, esto tendrá un par de efectos en su impresión.
* El relleno se vuelve más rígido en general, al igual que el aumento de la anchura de la línea de relleno, porque las líneas de relleno son capaces de apoyarse unas en otras cuando se presentan fuerzas de cizallamiento.
* El relleno brillará más a través de la piel, reduciendo la calidad de la superficie.
* Los espacios entre las líneas de relleno son más grandes, ya que las líneas se agrupan más. Esto hace que la piel se hunda más y permite el acolchado.

**Este ajuste no tiene efecto si la densidad del relleno es del 100% o superior.