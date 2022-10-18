Velocidad del ventilador de la balsa intermedia
====
<!--if cura_version<5.0:Este ajuste configura la velocidad del ventilador mientras se imprime la capa media del raft. La velocidad del ventilador mientras se imprime la capa media puede configurarse por separado de las capas base y superior.-->
<!--if cura_version>=5.0-->Este ajuste configura la velocidad del ventilador mientras se imprimen las capas intermedias del raft. La velocidad del ventilador mientras se imprimen las capas intermedias puede configurarse por separado de las capas base y superior.<!--endif-->

![Dónde se encuentra la capa intermedia en la balsa](../images/raft_dimensions_simplified.svg)

Configurar la velocidad del ventilador para las capas medias <!--if cura_version<5.0:layer--><!--if cura_version>=5.0--> por separado es útil ya que reducir la velocidad del ventilador puede mejorar la adherencia del lecho y reducir el alabeo. El aumento de la velocidad del ventilador puede mejorar la suavidad de la superficie, pero eso no es una preocupación para el medio <!--if cura_version<5.0:layer--><!--if cura_version>=5.0-->layers<!--endif-->. Debido a esto, es útil establecer la velocidad del ventilador un poco más baja que en las capas superiores.