Velocidad de impresión de la balsa intermedia
====
<!--if cura_version<5.0:Este ajuste configura la velocidad a la que se imprime la capa intermedia del raft. La velocidad de la capa media puede ser configurada por separado de la velocidad de las capas superior y base.-->
<!--if cura_version>=5.0-->Este ajuste configura la velocidad a la que se imprimen las capas intermedias del raft. La velocidad de las capas intermedias puede configurarse por separado de la velocidad de las capas superior y base.<!--endif-->

![Dónde se encuentra la capa intermedia en la balsa](../images/raft_dimensions_simplified.svg)

Imprimiendo la capa intermedia <!--if cura_version<5.0:layer--><!--if cura_version>=5.0-->más lentamente se mantiene el material caliente durante más tiempo, lo que reduce las tensiones internas. Esto reduce la deformación una vez que el material se enfría. Sin embargo, imprimir más lentamente también lleva más tiempo.