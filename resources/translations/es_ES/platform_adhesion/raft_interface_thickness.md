Grosor intermedio de la balsa
====
<!--if cura_version<5.0:Esta configuración ajusta el grosor vertical de la capa media de la balsa.-->
<!--if cura_version>=5.0-->Esta configuración ajusta el grosor vertical de las capas medias de la balsa. Esto es sólo la altura de una capa, por lo que la altura total de las capas medias será este ajuste multiplicado por el valor del ajuste [Capas medias de la balsa](raft_interface_layers.md).<!--endif-->

![Dimensiones relacionadas con la balsa](../images/raft_dimensions.svg)

Tener una capa de balsa más gruesa tiende a hacer la balsa un poco más rígida. Esto evita que se doble, tanto durante la impresión como después de ella. Durante la impresión, se quiere que la balsa sea rígida para que no se deforme, lo que rompe la adhesión a la placa de construcción y hace que la balsa se funda con el modelo. Después de la impresión, se desea que la balsa sea flexible para poder separarla del modelo más fácilmente. Ese es el equilibrio que hay que conseguir para esta configuración.