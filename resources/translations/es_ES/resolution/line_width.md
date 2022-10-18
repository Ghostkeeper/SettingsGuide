Ancho de línea
====
Este es el ancho horizontal de las líneas que la impresora colocará. Normalmente el diámetro de la abertura de la boquilla determina el ancho de sus líneas, pero al extruir más o menos material, la impresora puede variar un poco el ancho de las líneas.

<!--screenshot {
"image_path": "line_width_small.png",
"models": [{"script": "holes_cutout.scad"}],
"camera_position": [17, 39, 61],
"settings": {"line_width": 0.2},
"colours": 64
}-->
<!--screenshot {
"image_path": "line_width_large.png",
"models": [{"script": "holes_cutout.scad"}],
"camera_position": [17, 39, 61],
"settings": {"line_width": 0.6},
"colours": 32
}-->
![Líneas muy finas](../images/line_width_small.png)
![Líneas muy anchas](../images/line_width_large.png)

La reducción del ancho de línea permite a la impresora imprimir más detalles. En particular, también permite que la impresora imprima partes finas. El ancho de línea es uno de los ajustes que más influyen en la impresión. Estos son algunos de los efectos:
* La impresión de líneas más finas permitirá imprimir piezas más finas, ya que incluso puede encajar una línea en las partes más finas.
* Ajustar el ancho de línea a un múltiplo uniforme del grosor de su impresión puede hacer que el objeto sea más fuerte y que el material fluya mejor.
* Un ancho de línea más pequeño hará que su superficie superior se vea más suave.
* Imprimir líneas ligeramente más pequeñas que el tamaño de su boquilla tiende a mejorar la resistencia. Permite que la boquilla fusione las líneas adyacentes cuando hace una segunda pasada ligeramente por encima de la línea anterior.
* La impresión de líneas demasiado anchas provocará una infraextrusión. La impresora intentará extrudir más material, suficiente para llenar el ancho deseado de la línea. Ese material intentará fluir en cualquier dirección que pueda. Sin embargo, en algún momento la presión de retorno será demasiado grande, de manera que el material ya no fluirá hacia el lado de las líneas muy anchas. Esto deja huecos entre las líneas.
* Las líneas de impresión demasiado pequeñas también provocan una subextrusión. Si el material no fluye lo suficientemente rápido a través de la boquilla, la tensión superficial del material hará que se coagule en pequeñas gotas, haciendo que la extrusión sea desigual y dejando huecos entre las gotas.
* La impresión de líneas más finas aumentará considerablemente el tiempo de impresión.

No es aconsejable reducir el ancho de la línea por debajo del 60% del tamaño de la boquilla o por encima del 150%. Ambos pueden fallar en la extrusión de suficiente material.

<!--if cura_version>=5.0-->En piezas finas, el ancho de línea se ajustará automáticamente para que se ajuste al ancho local de la pieza allí. No es necesario asegurarse de que la anchura de la pieza es un múltiplo de la anchura de la línea. El [Ángulo del umbral de transición de la pared](../shell/wall_transition_angle.md) determina dónde se ajusta automáticamente el ancho de línea en las esquinas agudas. El [Ancho mínimo de la línea de la pared](../shell/min_wall_line_width.md) determina hasta dónde se puede ajustar en cada dirección.<!--endif-->

<!--if cura_version<5.0:
Ajuste de los anchos de línea para que quepan suficientes paredes
----
Cuando se imprimen objetos mecánicos que necesitan ser delgados pero fuertes, regularmente se encontrará con el problema de que su pieza no es un múltiplo par limpio del ancho de línea. Si no es un múltiplo par, Cura normalmente reducirá el flujo de algunas de las líneas debido al ajuste [Compensar solapamientos de paredes](../shell/travel_compensate_overlapping_walls_enabled.md). Esto cambia la velocidad de flujo a través de la boquilla, lo que va en detrimento de la calidad visual. Si es un múltiplo limpio de la anchura de la línea pero no un número par, una de las paredes se reducirá a 0.

Producir contornos limpios con líneas pares puede hacer que la impresión sea más fuerte y tenga mejor aspecto. Una habilidad distintiva de cualquier usuario experto de Cura es ser capaz de ajustar el ancho de línea de tal manera que el número deseado de contornos llene la impresión.

![Ancho de línea por defecto, donde los contornos no encajan y algunas líneas son más gruesas que otras](../images/line_width_fit_bad.png)
![Reducir el ancho de la línea hace que se ajuste uniformemente](../images/line_width_fit_good_small.png)
![Aumentar el ancho de línea también funciona](../images/line_width_fit_good_large.png)
-->
Manteniendo el flujo constante
----
Las grandes fluctuaciones de flujo son a veces problemáticas para las impresoras FDM. La cámara de la boquilla mantiene parte del material bajo presión, lo que hace que el flujo real que sale de la boquilla se retrase. El caudal tarda en aumentar o disminuir. Las impresoras con un sistema Bowden para alimentar el filamento también tienen elasticidad en el tubo Bowden, lo que hace que el efecto sea mucho peor. Como resultado de esto, obtendrás una subextrusión cuando cambies a un caudal mayor y una sobreextrusión cuando cambies a un caudal menor. Por lo tanto, es una buena idea mantener el caudal lo más constante posible.

La anchura de la línea influye mucho en el caudal. Es aconsejable mantener la anchura de los conductos cercana y próxima al tamaño de la boquilla. Si ajusta el ancho de línea de forma significativa, podría considerar ajustar también la velocidad de impresión para mantener el caudal más constante. Esto mejorará la precisión dimensional de su impresión.