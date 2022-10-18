Umbral de velocidad regular/máxima del ventilador
====
Este ajuste determina el tiempo de impresión de la capa en el que es tan corto que la velocidad del ventilador comenzará a aumentar hacia la [Velocidad máxima del ventilador](cool_fan_speed_max.md). Las capas que tardan más en imprimirse utilizarán la [Velocidad normal del ventilador](cool_fan_speed_min.md). Las capas que tarden menos en imprimirse tendrán la velocidad del ventilador interpolada entre los ajustes de velocidad del ventilador regular y máxima, hasta el [Tiempo mínimo de la capa](cool_min_layer_time.md) donde la velocidad del ventilador será la máxima.

Qué velocidad del ventilador se utiliza donde](../images/cool_fan_speed.svg)

Efectivamente, reducir este umbral (hacia capas más cortas) hará que el ventilador gire a la velocidad normal del ventilador más a menudo. Aumentar este umbral hará que el ventilador gire a mayor velocidad más a menudo, incluso si las capas no son muy pequeñas.

Es bueno mantener cierta distancia entre el Tiempo Mínimo de Capas y este Umbral de Velocidad Regular/Máxima del Ventilador. Si el umbral se establece en el Tiempo Mínimo de Capa, el ventilador se detendrá bruscamente si las capas quedan ligeramente por debajo del umbral. Esto causa una banda visible a través de la superficie de la impresión, ya que hay un borde duro donde el ventilador se detuvo repentinamente. Si por el contrario hay alguna diferencia entre los dos ajustes, el cambio de velocidad del ventilador será más gradual y el banding no será visible en la impresión.