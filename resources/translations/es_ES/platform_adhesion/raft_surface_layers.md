Capas superiores de la balsa
====
<!--if cura_version<5.0:Este es el número de capas en la parte superior de la balsa. Siempre habrá una capa base y una capa intermedia, pero puede haber cualquier número de capas superiores. Estas capas superiores son normalmente muy densas, como para producir una superficie suave para imprimir el modelo.-->
<!--if cura_version>=5.0-->Este es el número de capas en la parte superior de la balsa. Siempre habrá una capa base, pero puede haber cualquier número de [capas intermedias](raft_interface_layers.md) y capas superiores. Estas capas superiores son normalmente muy densas, para producir una superficie lisa para imprimir el modelo.

![Dónde se encuentran las capas superiores en la balsa](../images/raft_dimensions_simplified.svg)

Un mayor número de capas hace que la superficie para imprimir el modelo sea más suave, ya que las capas de la base y del medio, escasamente rellenadas, necesitan ser puenteadas. Una superficie más lisa hace que la parte inferior de la impresión se vea mejor y hace que la adhesión entre la balsa y el modelo sea más fuerte.

Sin embargo, un mayor número de capas también requiere mucho más tiempo de impresión.