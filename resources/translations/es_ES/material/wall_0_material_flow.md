Flujo de pared exterior
====
Esta configuración ajusta el caudal sólo para la pared exterior. El caudal de la pared exterior puede ajustarse por separado del caudal de las paredes interiores.

El ajuste del caudal durante la pared exterior es un método de parada para solucionar problemas de velocidad de extrusión o de precisión dimensional. El mismo efecto puede conseguirse también ajustando las opciones [Outer Wall Line Width](../resolution/wall_line_width_0.md) y [Outer Wall Inset](../shell/wall_0_inset.md), pero este ajuste podría ser una forma más intuitiva de afinar inicialmente.

Si hay un problema con la tasa de extrusión sólo durante la pared exterior, es mejor mirar las [velocidades de impresión](../speed/speed_wall_0.md) y [temperatura de impresión](material_print_temperature.md). Tal vez el material no recibe suficiente impulso fuera de la boquilla y una mayor velocidad de impresión podría ayudar. Tal vez las líneas son demasiado finas para extruir correctamente. Tal vez el material está demasiado frío o demasiado caliente.

Si hay un problema con la precisión dimensional, es mejor mirar a [anchos de línea](../resolution/wall_line_width_0.md), [expansión horizontal](../shell/xy_offset.md) y el [orden de impresión](../shell/outer_inset_first.md).