Aceleración de la impresión de la balsa intermedia
====
<!--if cura_version<5.0:Este ajuste configura la tasa de aceleración del cabezal de impresión mientras se imprime la capa media del raft. La aceleración durante la capa media de la balsa puede configurarse por separado de las capas base y superior.-->
<!--if cura_version>=5.0-->Este ajuste configura la tasa de aceleración del cabezal de impresión mientras se imprimen las capas intermedias del raft. La aceleración durante las capas intermedias del raft puede configurarse por separado de las capas base y superior.<!--endif-->

![Dónde se encuentra la capa intermedia en el raft](../images/raft_dimensions_simplified.svg)

Dado que la balsa se compone generalmente de segmentos de línea largos, el aumento de la aceleración normalmente tiene muy poco impacto en el tiempo de impresión. Sin embargo, aumentar la aceleración ahorrará un poco de tiempo al pasar por las esquinas al final de las líneas.

Aumentar la tasa de aceleración causará que la impresora vibre más mientras se imprime el medio <!--if cura_version<5.0:layer--><!--if cura_version>=5.0-->layers<!--endif--> del raft. Esto aumenta ligeramente el riesgo de arrancar la balsa de la placa de construcción.