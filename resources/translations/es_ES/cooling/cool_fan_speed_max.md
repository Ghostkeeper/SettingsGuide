Velocidad máxima del ventilador
====
La velocidad a la que los ventiladores del cabezal de impresión girarán cuando la capa se imprima en el tiempo mínimo de capa. En el tiempo mínimo de capa, querrá enfriar la capa lo más rápido posible para reducir el tiempo que tarda la capa en enfriarse antes de que la impresora ponga la siguiente capa encima.

![Qué velocidad del ventilador se utiliza donde](../images/cool_fan_speed.svg)

Si la impresión de una capa tarda entre los ajustes [Umbral de velocidad del ventilador regular/máxima](cool_min_layer_time_fan_speed_max.md) y el [Tiempo mínimo de la capa](cool_min_layer_time.md), la velocidad del ventilador se interpolará entre la [Velocidad del ventilador regular](cool_fan_speed_min.md) y la [Velocidad del ventilador máxima](cool_fan_speed_max.md). Una vez que se alcanza el Tiempo de Capa Mínimo, también se alcanzará la Velocidad Máxima del Ventilador. De esta forma la impresión se enfriará al máximo para que se enfríe lo más rápido posible antes de que se ponga la siguiente capa encima.