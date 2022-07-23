Diámetro de la boquilla
====
Este ajuste mide el diámetro de la abertura de la boquilla por la que fluye el material.

![Dimensiones del cabezal de impresión](../images/head_dimensions.svg)

Esta es una dimensión importante en la que otros ajustes pueden basar sus valores por defecto. Lo más importante es que el [Ancho de línea](../resolution/line_width.md) se ajusta normalmente en base al tamaño de la boquilla. Algunos perfiles de impresora limitan la altura de la capa basándose en el tamaño de la boquilla también, ya que el tamaño de la boquilla es el factor más importante en la rapidez con la que se puede extruir el material.

<!--if cura_version < 5.0:El tamaño de la boquilla también se utiliza directamente, para un detalle: Cuando se rellenan [pequeños huecos](../shell/fill_perimeter_gaps.md), los trozos de línea más alejados de dos tamaños de boquilla no se fusionan entre sí.-->

No ajuste el tamaño de la boquilla a menos que modifique la boquilla física. Algunos slicers (incluyendo Cura 15.04 y anteriores) utilizan el término "tamaño de boquilla" para referirse a la anchura de las líneas de la impresión. Cura utiliza el ajuste [Anchura de línea](../resolution/line_width.md) para ello.

**Como se trata de un ajuste de la máquina, este ajuste no suele ser visible en la lista de ajustes. Si su impresora tiene perfiles específicos para las boquillas disponibles, puede seleccionarlos en el menú de configuración de la impresora en la parte superior central de la pantalla. De lo contrario, puede ajustar el diámetro de las boquillas en el diálogo de configuración de la impresora, que se encuentra en la lista de impresoras añadidas en el diálogo de preferencias.**