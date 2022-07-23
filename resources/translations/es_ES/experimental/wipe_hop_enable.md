Limpiar salto en Z
====
Con esta configuración, el procedimiento de limpieza se hará mientras se salta en Z. Esto puede configurarse por separado de los [saltos Z] ordinarios (../travel/retraction_hop_enabled.md).

El procedimiento de limpieza contiene dos movimientos de desplazamiento muy largos que van hasta el lado del volumen de construcción. Durante estos movimientos de desplazamiento, el cabezal de impresión puede adquirir bastante velocidad porque tiene mucho tiempo para acelerar. A grandes velocidades, hay una mayor posibilidad de que el cabezal de impresión golpee accidentalmente las piezas previamente impresas. Por lo tanto, puede querer habilitar los saltos Z incluso si no lo haría para el proceso de impresión ordinario.

El salto Z en este procedimiento se ejecuta independientemente de si [los saltos Z sólo se realizan sobre piezas previamente impresas](../travel/retraction_hop_only_when_collides.md) o si hay piezas impresas en medio.